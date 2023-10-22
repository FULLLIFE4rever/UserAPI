import logging
from json import loads
from typing import Dict, List

from requests import get

logger = logging.getLogger(__name__)


class QuestionGetter:
    def __init__(self, from_url: str) -> None:
        self._from_url = from_url

    def get_list(self, questions_num: int) -> List[Dict]:
        try:
            response = get(self._from_url, params={"count": questions_num})
            response = loads(response.text)
            return response
        except ConnectionError as e:
            logger.exception(f"Session rollback because of exception {e}")
