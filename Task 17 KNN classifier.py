#KNN implementation from scratch

import pandas as pd
import numpy as np

# Load data
train_file = "TrainingSet.xlsx"
test_file = "TestingSet.xlsx"

train_df = pd.read_excel(train_file)
test_df = pd.read_excel(test_file)

# Split data into features and labels
train_features = train_df.iloc[:, :-1].values
train_labels = train_df.iloc[:, -1].astype('category').cat.codes.values
test_features = test_df.iloc[:, :-1].values

# Normalize data
train_features = (train_features - train_features.mean(axis=0)) / train_features.std(axis=0)
test_features = (test_features - train_features.mean(axis=0)) / train_features.std(axis=0)

# Split training data into training set and validation set
num_train = train_features.shape[0]
num_train_valid = int(0.8 * num_train)

train_valid_features = train_features[:num_train_valid, :]
train_valid_labels = train_labels[:num_train_valid]
test_valid_features = train_features[num_train_valid:, :]
test_valid_labels = train_labels[num_train_valid:]

# Define KNN function
def knn(train_features, train_labels, test_features, k):
    distances = np.sum((train_features - test_features)**2, axis=1)
    indices = np.argsort(distances)[:k]
    k_labels = train_labels[indices]
    counts = np.bincount(k_labels)
    predicted_label = np.argmax(counts)
    return predicted_label

# Create a categorical object with the original labels as categories
original_labels = train_df.iloc[:, -1].astype('category').cat.categories

# Evaluate accuracy for different values of k
for k in [3, 5, 7]:
    num_correct = 0
    predicted_labels = []
    for i in range(test_valid_features.shape[0]):
        predicted_label = knn(train_valid_features, train_valid_labels, test_valid_features[i, :], k)
        predicted_labels.append(original_labels[predicted_label])
        if predicted_label == test_valid_labels[i]:
            num_correct += 1
    accuracy = num_correct / test_valid_features.shape[0]
    print("Accuracy for k={}: {:.2f}".format(k, accuracy))
    
    # Store predicted labels and accuracy in Excel sheet
    writer = pd.ExcelWriter("Predicted_labels_k{}.xlsx".format(k))
    results_df = pd.DataFrame({"Predicted Label": predicted_labels, "Accuracy": accuracy})
    results_df.to_excel(writer, sheet_name="Results", index=False)
    writer.save()
    
    
    
#standard implementation

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
train_file = "TrainingSet.xlsx"
test_file = "TestingSet.xlsx"

train_df = pd.read_excel(train_file)
test_df = pd.read_excel(test_file)

# Split data into features and labels
train_features = train_df.iloc[:, :-1].values
train_labels = train_df.iloc[:, -1].values
test_features = test_df.iloc[:, :-1].values

# Normalize data
scaler = StandardScaler()
train_features = scaler.fit_transform(train_features)
test_features = scaler.transform(test_features)

# Split training data into training set and validation set
X_train, X_valid, y_train, y_valid = train_test_split(train_features, train_labels, test_size=0.2, random_state=42)

# Define KNN classifier
knn = KNeighborsClassifier(n_neighbors=7)

# Train classifier on training set
knn.fit(X_train, y_train)

# Predict labels for validation set
y_pred = knn.predict(X_valid)

# Calculate accuracy for different values of k
for k in [3, 5, 7]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_valid)
    accuracy = accuracy_score(y_valid, y_pred)
    print("Accuracy for k={}: {:.2f}".format(k, accuracy))
