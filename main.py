
from functions import getAvailableMealList, getUsedMealList, moveToUsedMeals, resetMealLists, getAvailableMealLabels, getDinner
import tkinter as tk

AVAILABLEMEALSFILE = "availableMealList.txt"
USEDMEALSFILE = "usedMealList.txt"

# root = tk.Tk()

# mainFrame = tk.Frame(root)
# mainFrame.grid(column=0, row=0)

# titleLabel = tk.Label(mainFrame, text="Food Planner")
# titleLabel.grid(column=0, row=0)

# showAvailableMealsButton = tk.Button(mainFrame, text="What's for dinner?", command=lambda: displayFrame())
# showAvailableMealsButton.grid(column=0, row=1)

# root.mainloop()

print(getDinner(AVAILABLEMEALSFILE, USEDMEALSFILE))