from apis.meals_client import MealsClient
from models.recipe import MealSearchResults, Ingredient, Recipe, MealsApiResponse


class MealsService:
    def __init__(self):
        self.client = MealsClient()

    def get_meal_details(self, meal_id: int) -> Recipe:
        """
        Finds the details of a specific meal by its ID and converts it to a Recipe object.
        :param meal_id: The ID of the meal to retrieve.
        :return: A Recipe object containing the details of the specified meal.
        """
        meal_details = self.client._get(f"lookup.php", MealsApiResponse, i=meal_id)
        return self._convert_meal_api_to_recipe(meal_details.meals[0])

    def get_random_meal(self):
        """
        Finds a random meal and converts it to a Recipe object.
        :return: A Recipe object containing the details of a random meal.
        """
        meal_details = self.client.random_meal()
        # fetch the first meal in the list of meals returned by the API and convert it to a Recipe object
        return self._convert_meal_api_to_recipe(meal_details.meals[0])


    def get_meal_by_ingredient(self, ingredient: str) -> MealSearchResults:
        """
        Finds meals that can be made with the specified ingredient.
        :param ingredient: The ingredient to search for.
        :return: A list of meals that can be made with the specified ingredient.
        """
        return self.client.find_by_ingredient(ingredient)

    @staticmethod
    def _convert_meal_api_to_recipe(meal_api: MealsApiResponse) -> Recipe:
        """
        Transforms a MealsApiResponse object into a Recipe object by extracting relevant fields and ingredients.
        :param meal_api: A MealsApiResponse object containing the meal details.
        :return: A Recipe object containing the extracted meal details.
        """
        ingredients = []
        for i in range(1, 21):
            ingredient_name = getattr(meal_api, f'strIngredient{i}')
            measure = getattr(meal_api, f'strMeasure{i}')
            if ingredient_name and ingredient_name.strip():
                ingredients.append(Ingredient(name=ingredient_name.strip(), measure=measure.strip() if measure else ""))

        return Recipe(
            id=int(meal_api.idMeal),
            name=meal_api.strMeal,
            category=meal_api.strCategory,
            region=meal_api.strArea,
            instructions=meal_api.strInstructions,
            thumbnail=meal_api.strMealThumb,
            youtube=meal_api.strYoutube,
            ingredients=ingredients
        )