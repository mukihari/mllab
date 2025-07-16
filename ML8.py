from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree 
import matplotlib.pyplot as plt

# Load the Iris dataset iris = load_iris()
X = iris.data y = iris.target
class_names = [str(name) for name in iris.target_names]

# Initialize the Decision Tree Classifier 
model = DecisionTreeClassifier()

# Train the classifier on the entire dataset 
model.fit(X, y)

# Visualize the Decision Tree 
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=iris.feature_names, class_names=class_names) 
plt.title("Decision Tree Visualization")
plt.show()
