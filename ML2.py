"""
Scikit-learn is a widely-used Python library that provides a comprehensive suite of tools and functionalities for machine learning tasks.
Versatility: Scikit-learn offers a wide range of tools and functionalities for various machine learning tasks, including but not limited to:
Supervised Learning: Classification, Regression
Unsupervised Learning: Clustering, Dimensionality Reduction
Model Selection and Evaluation: Cross-validation, Hyperparameter Tuning
Preprocessing: Data cleaning, Feature Engineering
Consistent Interface: It provides a consistent and user-friendly API, making it easy to experiment with different algorithms and techniques without needing to learn new syntax for each.
Integration with Other Libraries: Scikit-learn seamlessly integrates with other Python libraries like NumPy, pandas, and Matplotlib, allowing smooth data manipulation, preprocessing, and visualization.
Ease of Learning: Its well-documented and straightforward interface makes it suitable for both beginners and experienced machine learning practitioners. It's often recommended for educational purposes due to its simplicity.
Performance and Scalability: While focusing on simplicity, scikit-learn also emphasizes performance. It's optimized for efficiency and scalability, making it suitable for handling large datasets and complex models.
Community and Development: As an open-source project, scikit-learn benefits from a vibrant community of developers and contributors. Regular updates, bug fixes, and enhancements ensure it stays relevant and up-to-date with the latest advancements in machine learning.
Application in Industry and Academia: Scikit-learn's robustness and ease of use have made it a go-to choose in various domains, including finance, healthcare, natural language processing, and more. It's widely used in research and production environments.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics
# Load Iris dataset (a popular example dataset in machine learning) iris = load_iris()
X = iris.data # Features
y = iris.target # Target variable
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) 
# Initialize the model (K-Nearest Neighbors Classifier in this case) 
model = KNeighborsClassifier(n_neighbors=3)
# Train the model 
model.fit(X_train, y_train) 
# Make predictions
predictions = model.predict(X_test)
# Evaluate model accuracy
accuracy = metrics.accuracy_score(y_test, predictions) 
print(f"Accuracy: {accuracy}")
