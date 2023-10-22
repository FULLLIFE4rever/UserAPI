from os import environ

from dependency_injector import containers, providers
from dotenv import load_dotenv

from database import Database
from getter import QuestionGetter
from repositories import QuestionRepository
from services import QuestionService

load_dotenv()

print(environ["HOME"])
POSTGRES_USER = environ["POSTGRES_USER"]
POSTGRES_PASSWORD = environ["POSTGRES_PASSWORD"]
DB_HOST = environ["DB_HOST"]
DB_PORT = environ["DB_PORT"]
POSTGRES_DB = environ["POSTGRES_DB"]


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["endpoints"])

    db = providers.Singleton(
        Database,
        db_url=f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}",
    )

    getter = providers.Factory(
        QuestionGetter, from_url="https://jservice.io/api/random"
    )

    question_repository = providers.Factory(
        QuestionRepository,
        session_factory=db.provided.session,
    )

    question_service = providers.Factory(
        QuestionService,
        question_repository=question_repository,
    )
