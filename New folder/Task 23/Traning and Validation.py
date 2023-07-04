#Training Set: 
#The training set is the portion of the data that is used to train the machine learning model. It contains labeled data, where the input features and output labels are known. The model is trained on the training set, and its performance is evaluated on the validation and test sets.

#Validation Set: 
#The validation set is a portion of the data that is used to evaluate the performance of the model during the training process. It is used to fine-tune the model's hyperparameters, such as learning rate, regularization, and activation functions, to improve the model's accuracy on the test set.

#Test Set: 
#The test set is the portion of the data that is used to evaluate the performance of the model after training. It is used to simulate real-world scenarios and determine how well the model performs on new, unseen data.

#Hold-Out 
#Validation is a technique used in machine learning to evaluate the performance of a model on unseen data. It involves splitting the available data into a training set and a validation set, where the training set is used to train the model, and the validation set is used to evaluate the model's performance.

import numpy as np
from sklearn.model_selection import train_test_split

# Load any dataset
data = np.load("data.npy")
labels = np.load("labels.npy")
#usually testing set is given sepaarate but if only 1 set is given u can split it in into training validation and testing set

# Split data into training, validation, and test sets
train_data, test_data, train_labels, test_labels = train_test_split(
    data, labels, test_size=0.2, random_state=42)

train_data, val_data, train_labels, val_labels = train_test_split(
    train_data, train_labels, test_size=0.25, random_state=42)

# Train model on training set
model = get_model()
model.fit(train_data, train_labels)

# Evaluate model on validation set
val_score = model.evaluate(val_data, val_labels)

# Tune model based on validation performance
model = tune_model(model)

# Train model on concatenated training and validation sets
train_data = np.concatenate([train_data, val_data])
train_labels = np.concatenate([train_labels, val_labels])
model.fit(train_data, train_labels)

# Evaluate model on test set
test_score = model.evaluate(test_data, test_labels)



#Kfold cross validation

num_validation_samples = 10000
K = 5
validation_scores = []

# Shuffle data
np.random.shuffle(data)

# Split data into K folds and train/evaluate model K times
for fold in range(K):
    # Define validation and training data for current fold
    validation_data = data[num_validation_samples * fold: num_validation_samples * (fold + 1)]
    training_data = np.concatenate([data[:num_validation_samples * fold], 
                                     data[num_validation_samples * (fold + 1):]])
    
    # Train model on training data
    model = get_model()
    model.fit(training_data)
    
    # Evaluate model on validation data
    validation_score = model.evaluate(validation_data)
    validation_scores.append(validation_score)

# Compute average validation score
avg_validation_score = np.mean(validation_scores)
import numpy as np
from sklearn.linear_model import LogisticRegression


# Define (features) and (labels)
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([0, 1, 0, 1, 0])

K = 3

validation_scores = np.zeros(K)

# Shuffle data and split into K folds
indices = np.random.permutation(len(X))
fold_sizes = np.full(K, len(X) // K)
fold_sizes[:len(X) % K] += 1
current = 0


for i in range(K):
    # Define validation and training indices for current fold
    validation_indices = indices[current:current+fold_sizes[i]]
    training_indices = np.concatenate((indices[:current], indices[current+fold_sizes[i]:]))
    
    # Define training and validation data for current fold
    X_train, y_train = X[training_indices], y[training_indices]
    X_val, y_val = X[validation_indices], y[validation_indices]
    
    # Train logistic regression model on training data
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    # Evaluate model on validation data and store validation score
    validation_score = model.score(X_val, y_val)
    validation_scores[i] = validation_score
    
    # Update current index for next fold
    current += fold_sizes[i]

# Compute and print average validation score
avg_validation_score = np.mean(validation_scores)
print("Average validation score:", avg_validation_score)