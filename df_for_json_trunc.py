#truncate the JSON Data
import pandas as pd
import os

#set current working directory
current_directory = os.getcwd()
print('verify your current wd: ', current_directory)

# Specify the file name
raw_json_file = 'raw_nyc_phil.json'
ingest_full_path = os.path.join(current_directory,raw_json_file)


# Read the file using the 'with' statement
with open(raw_json_file, 'r') as raw_json:
    # Load the data into a Pandas DataFrame
    df = pd.read_json(raw_json)

#print data frame shape
print('Original Dataframe:\n', df.shape)
df = df.head(5)
print('Truncated_Dataframe:\n', df.shape)

truncated_json_file = 'truncated_nyc_phil.json'
export_full_path = os.path.join(current_directory, truncated_json_file)
df.to_json(export_full_path, orient='records', lines=True)
