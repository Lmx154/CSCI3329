import pandas as pd

mydict = [['Toyota', 'Sienna', 2018],
          ['Honda', 'Civic', 2004],
          ['Audi', 'A6', 2009],
          ['BMW', 'X5', 2015],
          ['Ford', 'Focus', 2012]]
column_names = ['brand', 'model', 'year']
df = pd.DataFrame(mydict, columns=column_names)
# Save to csv
csv_file_path = 'car.csv'
df.to_csv(csv_file_path, index=False)
# Read csv
df_read = pd.read_csv(csv_file_path)
print("Data in CSV:")
print(df_read)