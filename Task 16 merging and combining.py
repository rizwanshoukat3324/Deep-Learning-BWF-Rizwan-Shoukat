import pandas as pd
import os

# get list of all files in directory
loc = "C:\\Users\\World\\OneDrive\\Desktop\\US_Census Data Cleaning"
files = os.listdir(loc)

# read all CSV files into separate DataFrames and store in a list
data_frames = []
for file in files:
    if file.endswith(".csv"):
        data_frames.append(pd.read_csv(os.path.join(loc, file)))

# concatenate all DataFrames into a single DataFrame
wholedata = pd.concat(data_frames, axis=0, ignore_index=True)

# save the DataFrame as a CSV file in the specified location
output_file = os.path.join(loc, "output.csv")
wholedata.to_csv(output_file, index=False)

print(f"Output saved to {output_file}")

