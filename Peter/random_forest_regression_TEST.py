# ============================================================
# RANDOM FOREST REGRESSION - PARTICIPANT TEST
# Name: AI/ML    Date: 16/05/2026
#
# INSTRUCTIONS:
# This script has TWO types of challenges mixed together:
#   [BLANK]  - Fill in the missing code
#   [ERROR]  - Find and correct the deliberate mistake
#
# Total challenges: 8
# ============================================================


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd                          # [usman] - What library is imported here and why?
                                 # This librabry is mainly for data that includes table and values


# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values              # [kobo] - Fill in the correct iloc index to select the last column


# Training the Random Forest Regression model on the whole dataset
from sklearn.ensemble import RandomForestClassifier          # [aliyu ERROR 1] - This line has a mistake. Find and fix it.
regressor = RandomForestRegressor(n_estimaters=10, random_state=0)   # [uSMAN ERROR 2] - There is a spelling mistake in this line. Find and fix it.
regressor.fit(X, y)


# Predicting a new result
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd                          # [usman] - What library is imported here and why?


# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values              # [kobo] - Fill in the correct iloc index to select the last column


# Training the Random Forest Regression model on the whole dataset
from sklearn.ensemble import RandomForestClassifier          # [aliyu ERROR 1] - This line has a mistake. Find and fix it.
regressor = RandomForestRegressor(n_estimaters=10, random_state=0)   # [ERROR 2] - There is a spelling mistake in this line. Find and fix it.
regressor.fit(X, y)


# Predicting a new result
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd                          # [usman] - What library is imported here and why?


# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values              # [kobo] - Fill in the correct iloc index to select the last column


# Training the Random Forest Regression model on the whole dataset
from sklearn.ensemble import RandomForestClassifier          # [aliyu ERROR 1] - This line has a mistake. Find and fix it.
regressor = RandomForestRegressor(n_estimaters=10, random_state=0)   # [ERROR 2] - There is a spelling mistake in this line. Find and fix it.
regressor.fit(X, y)


# Predicting a new result
regressor.predict([[6.5]])                   # [idris 3] - Fill in the position level used to make a prediction (hint: it is between 6 and 7)


# Visualising the Random Forest Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), ___)) # [peter 4] - Fill in the correct reshape value to make it a 2D array with 1 column
plt.scatter(X, y, color='blue')             # [usman 3] - The colour used here is wrong. What should it be?
plt.plot(X_grid, regressor.predict(X_grid), color='red')    # [ERROR 4] - The colour used here is wrong. What should it be?
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')                             # [kobo 5] - Fill in the correct label for the y-axis
plt.show()


# ============================================================
# BONUS QUESTION (no code required - written answer): (aliyu, Idris)
#
# Q: What does the n_estimators parameter control in a
#    Random Forest model, and what effect does increasing
#    it have on the model?
#
# Answer:parameter in a Random Forest model controls the number of trees in the forest. Each tree is built from a bootstrap sample of the training data.
# ============================================================                   # [idris 3] - Fill in the position level used to make a prediction (hint: it is between 6 and 7)


# Visualising the Random Forest Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), ___)) # [peter 4] - Fill in the correct reshape value to make it a 2D array with 1 column
plt.scatter(X, y, color='blue')             # [usman 3] - The colour used here is wrong. What should it be?
plt.plot(X_grid, regressor.predict(X_grid), color='red')    # [ERROR 4] - The colour used here is wrong. What should it be?
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')                             # [kobo 5] - Fill in the correct label for the y-axis
plt.show()


# ============================================================
# BONUS QUESTION (no code required - written answer): (aliyu, Idris)
#
# Q: What does the n_estimators parameter control in a
#    Random Forest model, and what effect does increasing
#    it have on the model?
#
# Answer: ___________________________________________________
#         ___________________________________________________
#         ___________________________________________________
# ============================================================                 # [idris 3] - Fill in the position level used to make a prediction (hint: it is between 6 and 7)


# Visualising the Random Forest Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), ___)) # [IDRIS 4] - Fill in the correct reshape value to make it a 2D array with 1 column
plt.scatter(X, y, color='blue')             # [usman 3] - The colour used here is wrong. What should it be?
plt.plot(X_grid, regressor.predict(X_grid), color='red')    # [KOBO ERROR 4] - The colour used here is wrong. What should it be?
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')                             # [kobo 5] - Fill in the correct label for the y-axis
plt.show()


# ============================================================
# BONUS QUESTION (no code required - written answer): (aliyu, Idris)
#
# Q: What does the n_estimators parameter control in a
#    Random Forest model, and what effect does increasing
#    it have on the model?
#
# Answer: ___________________________________________________
#         ___________________________________________________
#         ___________________________________________________
# ============================================================
