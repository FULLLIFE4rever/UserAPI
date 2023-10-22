from typing import Iterator

from repositories import QuestionRepository
from models import Question


class QuestionService:

    def __init__(self, question_repository: QuestionRepository) -> None:
        self._repository: QuestionRepository = question_repository

    def get_questions(self) -> Iterator[QuestionRepository]:
        return self._repository.get_all()

    def get_question_by_id(self, question_id: int) -> Question:
        return self._repository.get_by_id(question_id)

    def add_questions(self, question_ids) -> None:
        return self._repository.add_questions_list(question_ids)

    def add_question(self, question: dict) -> None:
        return self._repository.add_question(answer=question['answer'],text=question['text'],question_id=question['question_id'])

    def get_imported_questions_by_id(self, questions_ids: list) -> list:
        return self._repository.get_all_by_id(questions_ids)
