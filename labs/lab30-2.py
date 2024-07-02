import pandas as pd

csv_file = 'jobs.csv'
df_read = pd.read_csv(csv_file)
print("Data in CSV:")
print(df_read)

# Remove under 20
csv_new = df_read[df_read['age'] >= 20]

new_jobs = 'jobs_new.csv'
csv_new.to_csv(new_jobs, index=False)
print("New Data:")
print(csv_new)
