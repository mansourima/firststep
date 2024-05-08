import pandas as pd

# Load your dataset into a pandas DataFrame
# Replace 'your_dataset.csv' with the path to your dataset file
df = pd.read_csv('give_feedback_train_data_1.csv')

# Display the current columns in your dataset
print("Current columns:", df.columns)

# Specify the columns you want to delete
columns_to_delete = ['variance_dict', 'max_variance', 'giving_feedback_classifier', 'giving_feedback_classifier_int', 'time_stamp']

# Delete the specified columns from the DataFrame
df.drop(columns=columns_to_delete, inplace=True)

# Display the columns after deletion
print("Columns after deletion:", df.columns)

# Optionally, save the modified DataFrame to a new file
df.to_csv('modified_dataset.csv', index=False)
