import requests
from pydantic import BaseModel

from models.recipe import MealsApiResponse, MealSearchResults


class MealsClient:
    """Fetches data from TheMealDB and maps responses to Pydantic models."""

    def __init__(self, base_url: str = "https://themealdb.com/api/json/v1/1"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def _get(self, endpoint: str, model: type[BaseModel], **params) -> BaseModel:
        response = self.session.get(
            f"{self.base_url}/{endpoint}", params=params, timeout=30
        )
        response.raise_for_status()
        return model.model_validate(response.json())

    def random_meal(self) -> MealsApiResponse:
        return self._get("random.php", MealsApiResponse)

    def find_by_ingredient(self, ingredient: str) -> MealSearchResults:
        return self._get(f"filter.php", MealSearchResults, i=ingredient)