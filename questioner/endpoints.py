from typing import Dict, Iterator

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response, status
from pydantic import BaseModel

from container import Container
from getter import QuestionGetter
from services import QuestionService

router = APIRouter()


class QuestionModel(BaseModel):
    question_id: int
    text: str
    answer: str


@router.get("/{question_id:int}/{answer:str}/{text:str}")
@inject
def add_question(
    question_id: int,
    answer: str,
    text: str,
    question_service: QuestionService = Depends(
        Provide[Container.question_service]
    ),
) -> Dict:
    question_dict = {
        "question_id": question_id,
        "answer": answer,
        "question": text,
    }
    question = question_service.add_question(question=question_dict)
    return question


@router.get("/{question_id:int}")
@inject
def get_question(
    question_id: int,
    question_service: QuestionService = Depends(
        Provide[Container.question_service]
    ),
) -> QuestionModel:
    return question_service.get_question_by_id(question_id=question_id)


@router.get("/add/{questions_num:int}")
@inject
def get_list(
    questions_num: int,
    question_service: QuestionService = Depends(
        Provide[Container.question_service]
    ),
    getter: QuestionGetter = Depends(Provide[Container.getter]),
) -> list[QuestionModel]:
    questions_list_out = []
    while len(questions_list_out) != questions_num:
        questions_count_to_get = questions_num - len(questions_list_out)
        question_json: list = getter.get_list(
            questions_num=questions_count_to_get
        )
        question_ids: list = list(map(lambda x: x["id"], question_json))
        questions_db = question_service.get_imported_questions_by_id(
            questions_ids=question_ids
        )
        found_id: list = list(map(lambda x: x.id, questions_db))
        for json in question_json:
            if json["id"] not in found_id:
                questions_list_out.append(json)
    question_list = question_service.add_questions(questions_list_out)
    return question_list


@router.get("/add/")
def get_status() -> str:
    return {"status": "OK"}


@router.get("/all")
@inject
def get_all(
    question_service: QuestionService = Depends(
        Provide[Container.question_service]
    ),
) -> list[QuestionModel]:
    return question_service.get_questions()
