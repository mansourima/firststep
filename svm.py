import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the dataset from the CSV file
feedback_data = pd.read_csv("feedback_data.csv")

# Extract features (X) and labels (y) from the dataset
X = feedback_data.drop(columns=['_id', 'userId'])  # Assuming '_id' and 'userId' are not features
y = feedback_data['userId']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the SVM classifier
clf = SVC(kernel='linear')

# Train the SVM classifier
clf.fit(X_train, y_train)

# Predict the labels for the test set
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
