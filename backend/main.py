import pandas as pd

print("Running Pandas version " + str(pd.__version__))

df = pd.read_csv('libraries-computers-available-csv.csv')

numColumns = len(df.iloc[0, :])

colNumIndexes = int(input(f"How many columns would you like printed? There are {numColumns} in this dataset. "))
if colNumIndexes == 1:
    columnIndex = int(input("What column would you like printed? \n"))
    print(df.iloc[:, columnIndex])  # prints the column using iloc
elif colNumIndexes == numColumns:
    print(df.to_string())
elif colNumIndexes >= 1:
    columnIndex1 = int(input(f"What is column number {colNumIndexes - (colNumIndexes - 1)}? "))  # TODO: replace
    columnIndex2 = int(input(f"What is column number {colNumIndexes - (colNumIndexes - 2)}? "))
    print(df.iloc[:, [columnIndex1, columnIndex2]])  # prints the column using iloc

else:
    print("Please choose a positive integer within the range")
