#TASK
import numpy as np

# Define the data as an array
data = np.array([
    ["Sales", "31...35", "46K...50K", "Senior"],
    ["Sales", "26...30", "26K...30K", "Junior"],
    ["Sales", "31...35", "31K...35K", "Junior"],
    ["systems", "21...25", "46K...50K", "Junior"],
    ["systems", "31...35", "66K...70K", "Senior"],
    ["systems", "26...30", "46K...50K", "Junior"],
    ["systems", "41...45", "66K...70K", "Senior"],
    ["Marketing", "36...40", "46K...50K", "Senior"],
    ["Marketing", "31...35", "41K...45K", "Junior"],
    ["secretary", "46...50", "36K...40K", "Senior"],
    ["secretary", "26...30", "26K...30K", "Junior"]
])

# Calculate the total number of instances
total_instances = len(data)

# Calculate the prior probability of each class
# Get the unique values and their frequency for the status column
num_status = np.unique(data[:, 3], return_counts=True)

# Calculate the prior probability of each status class
prior_prob_status = num_status[1] / total_instances


# Calculate the conditional probability of each attribute for each class 
# with Laplace smoothing
unique_departments = np.unique(data[:, 0])
unique_ages = np.unique(data[:, 1])
unique_salaries = np.unique(data[:, 2])

num_department = len(unique_departments)
num_age = len(unique_ages)
num_salary = len(unique_salaries)

cond_prob_department = {}
cond_prob_age = {}
cond_prob_salary = {}

for status in num_status[0]:
    cond_prob_department[status] = {}
    cond_prob_age[status] = {}
    cond_prob_salary[status] = {}
    
    #conditional probability of department given a status
    for department in unique_departments:
        # Count the number of instances with the given department and status
        count = len(data[(data[:, 0] == department) & (data[:, 3] == status)])
        # conditional probability of department given a status with Laplace smoothing
        cond_prob_department[status][department] = (count + 1) / (num_status[1][np.where(num_status[0] == status)][0] + num_department)
    
    #conditional probability of age given a status
    for age in unique_ages:
        # Count the number of instances with the given age and status
        count = len(data[(data[:, 1] == age) & (data[:, 3] == status)])
        # conditional probability of age given a status with Laplace smoothi
        cond_prob_age[status][age] = (count + 1) / (num_status[1][np.where(num_status[0] == status)][0] + num_age)
    
    #conditional probability of salary given a status
    for salary in unique_salaries:
        # Count the number of instances with the given salary and status
        count = len(data[(data[:, 2] == salary) & (data[:, 3] == status)])
        #conditional probability of salary given a status with Laplace smoothi
        cond_prob_salary[status][salary] = (count + 1) / (num_status[1][np.where(num_status[0] == status)][0] + num_salary)

        
def NaiveBayesClassifier(department, age, salary):
    # Initialize variables to keep track of maximum probability and predicted class
    max_prob = -1
    pred_status = None
    for status in num_status[0]:
        # Calculate the probability using the Naive Bayes formula (prior * likelihood)
        prob = prior_prob_status[np.where(num_status[0] == status)][0] * cond_prob_department[status][department] * cond_prob_age[status][age] * cond_prob_salary[status][salary]
        # Check if this probability is greater than the current maximum probability
        if prob > max_prob:
            # If it is, update the maximum probability and predicted class
            max_prob = prob
            pred_status = status
    # Return the predicted class with the highest probability
    return pred_status

# Test the classifier on unseen instances
print("The status for:\na) Marketing", "31...35", "46K...50K is: ")
print("                                 ", NaiveBayesClassifier("Marketing", "31...35", "46K...50K"))

print("b) Sales, 31...35, 66K...70K is:               ")
print("                                 ", NaiveBayesClassifier("Sales", "31...35" , "66K...70K")) 