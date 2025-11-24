src/ml_models/classifier.py  """Machine Learning Classifier Module

Implements KNN and Decision Tree classifiers.
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


class KNNClassifier:
    """K-Nearest Neighbors Classifier."""
    
    def __init__(self, k=5, metric='euclidean'):
        self.k = k
        self.model = KNeighborsClassifier(n_neighbors=k, metric=metric)
        self.is_trained = False
    
    def train(self, X_train, y_train):
        """Train the KNN model."""
        self.model.fit(X_train, y_train)
        self.is_trained = True
    
    def predict(self, X):
        """Make predictions."""
        if not self.is_trained:
            raise ValueError("Model must be trained first")
        return self.model.predict(X)
    
    def evaluate(self, X_test, y_test):
        """Evaluate model performance."""
        predictions = self.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy


class DTClassifier:
    """Decision Tree Classifier."""
    
    def __init__(self, max_depth=None, min_samples_split=2):
        self.model = DecisionTreeClassifier(
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            random_state=42
        )
        self.is_trained = False
    
    def train(self, X_train, y_train):
        """Train the Decision Tree model."""
        self.model.fit(X_train, y_train)
        self.is_trained = True
    
    def predict(self, X):
        """Make predictions."""
        if not self.is_trained:
            raise ValueError("Model must be trained first")
        return self.model.predict(X)
    
    def evaluate(self, X_test, y_test):
        """Evaluate model performance."""
        predictions = self.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions)
        return accuracy, report
