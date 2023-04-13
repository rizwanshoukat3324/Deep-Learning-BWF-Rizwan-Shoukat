# import libararies
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
# below command is you to find the files which exist in the path we gave to the command
loc = os.listdir(
    "C:\\Users\\World\\OneDrive\\Desktop\\US_Census Data Cleaning")
print(loc)
# below commands is used to read csv file in pandas
riz1 = pd.read_csv('states0.csv')
riz2 = pd.read_csv('states1.csv')
riz3 = pd.read_csv('states2.csv')
riz4 = pd.read_csv('states3.csv')
riz5 = pd.read_csv('states4.csv')
riz6 = pd.read_csv('states5.csv')
riz7 = pd.read_csv('states6.csv')
riz8 = pd.read_csv('states7.csv')
riz9 = pd.read_csv('states8.csv')
riz10 = pd.read_csv('states9.csv')
data = (riz1, riz2, riz3, riz4, riz5, riz6, riz7, riz8, riz9, riz10)
print(data)
# this command is use for merging dataframes in pandas
wholedata = pd.concat(data, axis=0, ignore_index=True)
print(wholedata)
# this command is use for export that merging dataframe with new name
wholedata.to_csv('us_cesus.csv')
path = "C:\\Users\\World\\OneDrive\\Desktop\\US_Census Data Cleaning\\us_cesus.csv"
wholedata1 = pd.read_csv(path)
print(wholedata1.head())
print(type(wholedata1))
# Split "GenderPop" column into two separate columns
genderpop_split = wholedata1['GenderPop'].str.split('_', expand=True)
# Assign "Men" and "Women" columns separately
wholedata1['Men'] = genderpop_split[0]
wholedata1['Women'] = genderpop_split[1]
print(wholedata1)
# this comand is use for replace
wholedata1['Men'] = wholedata1['Men'].str.replace('M', "")
wholedata1['Women'] = wholedata1['Women'].str.replace('F', '')
print(wholedata1)
# this command is use for changing data type
wholedata1['Men'] = wholedata1['Men'].astype('float')
print(wholedata1.info())


# below we use this command for making an an graph using matplotlib
data = pd.read_csv(
    'C:\\Users\\World\\OneDrive\\Desktop\\US_Census Data Cleaning\\Don.csv')
x = data['Women']
y = data['Income']
# Create the scatter plot
plt.plot(x, y)
# Add labels and a title
plt.xlabel('Women')
plt.ylabel('Income')
plt.title('Scatter Plot')
# Show the plot
plt.show()
# this command is use for putting values in null in excel inwhich TotalPop-Men=women
wholedata1['Women'].fillna(wholedata1['TotalPop'] -
                           wholedata1['Men'], inplace=True)
wholedata2 = pd.DataFrame(wholedata1)
print(wholedata2)
wholedata1.drop_duplicates(subset='State', keep='first', inplace=True)
print(wholedata1['State'])
# below we use this command for making histogram graph using matplotlib
data = pd.read_csv(
    'C:\\Users\\World\\OneDrive\\Desktop\\US_Census Data Cleaning\\Don.csv')
x = data['Hispanic']
# Create the Historam
hist_plot = x.hist(bins=20)
# Add labels and a title
hist_plot.set_xlabel('value')
hist_plot.set_ylabel('Frequency')
hist_plot.set_title('Hispanic histogram')
# Show the plot
plt.show()
data = pd.read_csv(
    'C:\\Users\\World\\OneDrive\\Desktop\\US_Census Data Cleaning\\Don.csv')
x = data['White']

# Create the Historam
hist_plot = x.hist(bins=20)
# Add labels and a title
hist_plot.set_xlabel('value')
hist_plot.set_ylabel('Frequency')
hist_plot.set_title('White histogram')
# Show the plot
plt.show()
data = pd.read_csv(
    'C:\\Users\\World\\OneDrive\\Desktop\\US_Census Data Cleaning\\Don.csv')
x = data['Black']

# Create the Historam
hist_plot = x.hist(bins=20)
# Add labels and a title
hist_plot.set_xlabel('value')
hist_plot.set_ylabel('Frequency')
hist_plot.set_title('Black histogram')
# Show the plot
plt.show()
data = pd.read_csv(
    'C:\\Users\\World\\OneDrive\\Desktop\\US_Census Data Cleaning\\Don.csv')
x = data['Native']

# Create the Historam
hist_plot = x.hist(bins=20)
# Add labels and a title
hist_plot.set_xlabel('value')
hist_plot.set_ylabel('Frequency')
hist_plot.set_title('Native histogram')
# Show the plot
plt.show()
data = pd.read_csv(
    'C:\\Users\\World\\OneDrive\\Desktop\\US_Census Data Cleaning\\Don.csv')
x = data['Asian']

# Create the Histogram
hist_plot = x.hist(bins=20)
# Add labels and a title
hist_plot.set_xlabel('value')
hist_plot.set_ylabel('Frequency')
hist_plot.set_title('Asian histogram')
# Show the plot
plt.show()
data = pd.read_csv(
    'C:\\Users\\World\\OneDrive\\Desktop\\US_Census Data Cleaning\\Don.csv')
x = data['Pacific']

# Create theHistogram
hist_plot = x.hist(bins=20)
# Add labels and a title
hist_plot.set_xlabel('value')
hist_plot.set_ylabel('Frequency')
hist_plot.set_title('Pasific histogram')
# Show the plot
plt.show()
