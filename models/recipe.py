from typing import List, Optional
from pydantic import BaseModel


class MealApi(BaseModel):
    idMeal: str
    strMeal: str
    strMealAlternate: Optional[str] = None
    strCategory: str
    strArea: Optional[str] = None
    strCountry: str
    strInstructions: str
    strMealThumb: str
    strTags: Optional[str] = None
    strYoutube: Optional[str] = None
    strIngredient1: Optional[str] = ""
    strIngredient2: Optional[str] = ""
    strIngredient3: Optional[str] = ""
    strIngredient4: Optional[str] = ""
    strIngredient5: Optional[str] = ""
    strIngredient6: Optional[str] = ""
    strIngredient7: Optional[str] = ""
    strIngredient8: Optional[str] = ""
    strIngredient9: Optional[str] = ""
    strIngredient10: Optional[str] = ""
    strIngredient11: Optional[str] = ""
    strIngredient12: Optional[str] = ""
    strIngredient13: Optional[str] = ""
    strIngredient14: Optional[str] = ""
    strIngredient15: Optional[str] = ""
    strIngredient16: Optional[str] = ""
    strIngredient17: Optional[str] = ""
    strIngredient18: Optional[str] = ""
    strIngredient19: Optional[str] = ""
    strIngredient20: Optional[str] = ""
    strMeasure1: Optional[str] = ""
    strMeasure2: Optional[str] = ""
    strMeasure3: Optional[str] = ""
    strMeasure4: Optional[str] = ""
    strMeasure5: Optional[str] = ""
    strMeasure6: Optional[str] = ""
    strMeasure7: Optional[str] = ""
    strMeasure8: Optional[str] = ""
    strMeasure9: Optional[str] = ""
    strMeasure10: Optional[str] = ""
    strMeasure11: Optional[str] = ""
    strMeasure12: Optional[str] = ""
    strMeasure13: Optional[str] = ""
    strMeasure14: Optional[str] = ""
    strMeasure15: Optional[str] = ""
    strMeasure16: Optional[str] = ""
    strMeasure17: Optional[str] = ""
    strMeasure18: Optional[str] = ""
    strMeasure19: Optional[str] = ""
    strMeasure20: Optional[str] = ""
    strSource: Optional[str] = None
    strImageSource: Optional[str] = None
    strCreativeCommonsConfirmed: Optional[str] = None
    dateModified: Optional[str] = None


class MealsApiResponse(BaseModel):
    meals: List[MealApi]

class MealMetadata(BaseModel):
    """Represents a single featured recipe card."""
    strMeal: str
    strMealThumb: str
    idMeal: str
    strArea: Optional[str] = None  # Can be null in the JSON, so it is optional
    strCountry: str


# --- Outer Model: The complete response structure ---
class MealSearchResults(BaseModel):
    """Wraps the list of meals returned from the API."""
    meals: List[MealMetadata]


class Ingredient(BaseModel):
    name: str
    measure: str

class Recipe(BaseModel):
    id: int
    name: str       # strMeal
    category: str   # strCategory
    region: str       # strArea
    instructions: str   #strInstructions
    thumbnail: str      # strMealThumb
    youtube: Optional[str] = None  # strYoutube
    ingredients: List[Ingredient] = []

