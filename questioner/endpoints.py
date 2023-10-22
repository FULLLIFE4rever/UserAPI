from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from container import Container
from services import QuestionService
from getter import QuestionGetter

router = APIRouter()


@router.get("/{question_id:int}/{answer:str}/{text:str}")
@inject
def add_question(
        question_id: int,
        answer: str,
        text: str,
        question_service: QuestionService = Depends(Provide[Container.question_service])
):
    question_dict = {'question_id': question_id, 'answer': answer, 'text': text}
    question = question_service.add_question(question=question_dict)
    return question


@router.get("/{question_id:int}")
@inject
def get_question(
        question_id: int,
        question_service: QuestionService = Depends(Provide[Container.question_service])
):
    return question_service.get_question_by_id(question_id=question_id)


@router.get("/add/{questions_num:int}")
@inject
def get_list(
        questions_num: int,
        question_service: QuestionService = Depends(Provide[Container.question_service]),
        getter: QuestionGetter = Depends(Provide[Container.getter])
):
    questions_list_out = []
    while len(questions_list_out) != questions_num:
        question_json: list = getter.get_list(questions_num=questions_num)
        question_ids: list = list(map(lambda x: x['id'], question_json))
        questions_db = question_service.get_imported_questions_by_id(questions_ids=question_ids)
        questions_list_out = [0 for _ in range(questions_num)]
    return question_json


@router.get("/add/")
def get_status():
    return {"status": "OK"}
