from fastmcp import FastMCP

from models import MealSearchResults, Recipe
from service import NoAAService, MealsService

mcp = FastMCP("Demo")
noaas = NoAAService()
meals_service = MealsService()

@mcp.tool(
    name="no_as_a_service",
    description="""
    This tool can be used to provide response or excuse whenever the user needs to
    refuse to do something.
    When called the response should be ALWAYS used as the response to the user.  
    Do not try to interpret it further.
    """
)
async def no_as_a_service(scenario_and_question: str) -> str:
    """
    This tool can be used to provide response or excuse whenever the user needs to
    refuse to do something.
    When called the response should be ALWAYS used as the response to the user.
    Do not try to interpret it further.

    :param scenario_and_question: A string representing the context and the question the user is asking.
    :return: A string containing the determined response to the provided question.
    """
    return noaas.get_reason()

@mcp.tool(
    name="get_meal_details",
    description="""
    Using the provided ID this will look up the details for that specific meal id
    """
)
async def get_meal_details(id: int) -> Recipe:
    """
    Using the provided ID this will look up the details for that specific meal id.
    This can be used when the user suggests a specific meal and we want to provide the details for that meal
    and the lookup id for that meal is known.

    :return: A randomly selected meal.

    """
    return meals_service.get_meal_details(id)

@mcp.tool(
    name="get_random_meal",
    description="""
    This tool will find a random meal.  
    It is useful whenever the user asks for meal ideas but doesn't have a specific ingredient in mind.  
    """
)
async def get_random_meal(description: str) -> Recipe:
    """
    This tool will find a random meal.
    It is useful whenever the user asks for meal ideas but doesn't have a specific ingredient in mind.

    :return: A randomly selected meal.

    """
    return meals_service.get_random_meal()

@mcp.tool(
    name="get_meals_by_ingredient",
    description="""
    This tool will generate a list of meals that can be made with the ingredient provided by the user.  
    It is useful whenever the user asks for meals that can be made with a specific ingredient.  
    """
)
async def get_meals_by_ingredient(ingredient: str) -> MealSearchResults:
    """
    This tool will generate a list of meals that can be made with the ingredient provided by the user.
    It is useful whenever the user asks us to find meals that can be made with a specific ingredient.
    The response should be used as the response to the user.

    :param ingredient: The ingredient to search for meals with
    :return: A list of meals that can be made with the ingredient provided by the user.
    """
    return meals_service.get_meal_by_ingredient(ingredient)

if __name__ == '__main__':
    mcp.run(transport="http", host="0.0.0.0", port=8001)
