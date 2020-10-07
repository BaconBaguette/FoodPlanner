
# Functions
from classes import Meal

def getAvailableMealList(availableMealsFile):
    availableMealList = []
    with open(availableMealsFile, "r") as f:
        for meal in f:
            newMeal = Meal(meal.rstrip())
            availableMealList.append(newMeal)
    return availableMealList


def getUsedMealList(usedMealsFile):
    usedMealList = []
    with open(usedMealsFile, "r") as f:
        for meal in f:
            newMeal = Meal(meal.rstrip())
            usedMealList.append(newMeal)
    return usedMealList