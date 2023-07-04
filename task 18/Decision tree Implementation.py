#classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
from sklearn import tree

data = pd.read_csv('sample_data.csv')

# Split the data into features and target
X = data.drop('Bought', axis=1)
y = data['Bought']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

decision = DecisionTreeClassifier()

# Train the classifier on the training data
decision.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = decision.predict(X_test)

# Evaluate the performance 
accuracy = metrics.accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

tree.plot_tree(decision)





import graphviz
from sklearn.tree import export_graphviz

# Export the decision tree as a Graphviz dot file
dot_data = export_graphviz(decision, out_file=None, 
                           feature_names=X.columns,  
                           class_names=['No', 'Yes'],  
                           filled=True, rounded=True,  
                           special_characters=True)
graph = graphviz.Source(dot_data)

# Display the decision tree visualization
graph.view()





#regressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd

data = pd.read_csv('sample_data_reg.csv')

X = data.drop('y', axis=1)
y = data['y']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regressor1 = DecisionTreeRegressor(max_depth=3)
regressor2 = DecisionTreeRegressor(max_depth=7)


# Train the regressor on the training data
regressor1.fit(X_train, y_train)

# Make predictions on the testing data
y_pred1 = regressor1.predict(X_test)

# Evaluate the performance 
r2 = r2_score(y_test, y_pred1)
print('R^2 score of 1st regressor', r2)


# Train the regressor on the training data
regressor2.fit(X_train, y_train)

# Make predictions on the testing data
y_pred2 = regressor2.predict(X_test)


# Evaluate the performance 
r2 = r2_score(y_test, y_pred2)
print('R^2 score of 2nd regressor:', r2)