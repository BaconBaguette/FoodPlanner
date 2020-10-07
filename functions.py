
# Functions
from classes import Meal
import tkinter as tk
from random import randint

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


def moveToUsedMeals(availableMealsFile, usedMealsFile, mealToMove):
    mealsStillAvailable = ""
    with open(availableMealsFile, "r") as f:
        for meal in f:
            if meal.rstrip() == mealToMove:
                pass
            else:
                mealsStillAvailable += meal
    with open(availableMealsFile, "w") as f:
        f.write(mealsStillAvailable)
    with open(usedMealsFile, "a") as f:
        f.write(f"{mealToMove}\n")


def resetMealLists(availableMealsFile, usedMealsFile):
    mealsString = ""
    with open(availableMealsFile, "r") as f:
        for meal in f:
            mealsString += meal
    with open(usedMealsFile, "r") as f:
        for meal in f:
            mealsString += meal
    with open(usedMealsFile, "w") as f:
        f.write("")
    with open(availableMealsFile, "w") as f:
        f.write(mealsString)


def getAvailableMealLabels(availableMealsFile, usedMealsFile, root):
    availableMealList = getAvailableMealList(availableMealsFile)
    availableMealLabels = []
    for meal in availableMealList:
        availableMealLabels.append(tk.Label(root, text=meal.desc))
    return availableMealLabels


def getDinner(availableMealsFile, usedMealsFile):
    availableMeals = getAvailableMealList(availableMealsFile)
    dinner = availableMeals[randint(0, len(availableMeals)-1)].desc
    return dinner
