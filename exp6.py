import pandas as pd
marks = pd.Series([85, 91, 78, 88, 95], index=list("ABCDE"))
print("--- Pandas Series ---")
print(marks)
df = pd.DataFrame({
    "RollNo": range(101, 106),
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE"],
    "Mark": marks.values,
})
print("\n--- DataFrame ---")
print(df)
print("\nAverage Mark:", round(df["Mark"].mean(), 2))
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])
