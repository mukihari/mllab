from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics
# Load the Iris dataset (or any other dataset you want to use) 
iris = load_iris()
X = iris.data 
y = iris.target
# Split the dataset into training and testing sets
X_train,	X_test,	y_train,	y_test	=	train_test_split(X,	y,	test_size=0.3, random_state=42)
# Initialize the k-NN classifier
# Set the number of neighbors
model = KNeighborsClassifier(n_neighbors=3)

# Train the classifier on the training data 
model.fit(X_train, y_train)
# Make predictions on the testing data 
predictions = model.predict(X_test)
# Evaluate the performance of the classifier
accuracy = metrics.accuracy_score(y_test, predictions) 
print(f"Accuracy: {accuracy}")
# Classification report and confusion matrix 
print("Classification Report:") 
print(metrics.classification_report(y_test, predictions)) 

print("Confusion Matrix:") 
print(metrics.confusion_matrix(y_test, predictions))
