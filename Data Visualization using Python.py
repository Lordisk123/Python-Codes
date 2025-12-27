import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
path = r"C:\Users\subra\Downloads\1. Ongoing Stuff\MBA (Data Science and AI)\2. Term-2\MGNM801 - Python\creditriskdata2.csv"
df = pd.read_csv(path)
print("Columns found in your data:", df.columns.tolist())
plt.figure(figsize=(10, 6))
sns.violinplot(x="Loan_Status", y="Age", data=df)
plt.title("Credit Risk Analysis: Age Distribution by Loan Status")
plt.show()
