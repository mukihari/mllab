"""Install scikit-learn and other libraries:
Install NumPy and pandas (if not installed):
Open a terminal/command prompt.
Type pip install numpy pandas and press Enter. This will install NumPy and pandas, essential libraries for data manipulation and computation.
Install scikit-learn:
In the same terminal/command prompt, type pip install scikit-learn and press Enter. This will install scikit-learn, the machine learning library.
Test the installations:
Open a Python interpreter by typing python or python3 in the terminal.
Import scikit-learn: import sklearn
If there are no errors, scikit-learn is successfully installed and ready for use.
Simple Example:
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 

# Load an example dataset (iris dataset)
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)
# Initialize and train a classifier (K-Nearest Neighbors) 
model = KNeighborsClassifier(n_neighbors=3) 
model.fit(X_train, y_train)
# Evaluate the classifier
accuracy = model.score(X_test, y_test) 
print(f"Accuracy: {accuracy}")
