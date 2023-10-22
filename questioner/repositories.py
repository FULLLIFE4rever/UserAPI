from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy import insert
from sqlalchemy.orm import Session

from models import Question


class QuestionRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Question]:
        with self.session_factory() as session:
            return session.query(Question).all()

    def get_by_id(self, question_id: int) -> Question:
        with self.session_factory() as session:
            question = session.query(Question).filter(Question.id == question_id).first()
            if not question:
                raise QuestionNotFoundError(question_id)
            return question

    def get_all_by_id(self, question_ids: list) -> Iterator[Question]:
        with self.session_factory() as session:
            question = session.query(Question).filter(Question.question_id.in_(question_ids))
            return question

    def add_questions_list(self, questions: Iterator[Question]) -> Iterator[Question]:
        with self.session_factory() as session:
            questions_added = []
            new_question = None
            for question in questions:
                new_question = Question(question_id=question['id'], text=question['question'], answer=question['answer'])
                session.add(new_question)
                # session.flush()
                # session.refresh(new_question)
                questions_added.append(new_question)
            session.commit()
            #return questions_added
            return [{'question_id': item.question_id, 'text': item.text, 'answer': item.answer} for item in questions_added]

    def add_question(self, question_id: int, text: str, answer: str) -> Iterator[Question]:
        with self.session_factory() as session:
            question = Question(question_id=question_id, text=text, answer=answer)
            session.add(question)
            session.commit()
            session.refresh(question)
            return question


class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class QuestionNotFoundError(NotFoundError):

    entity_name: str = "question_id"
