import pandas as pd
import statsmodels.api as sm 
dt = pd.read_csv(r"C:\Users\subra\Downloads\1. Ongoing Stuff\MBA (Data Science and AI)\2. Term-2\MGNM801 - Python\creditriskdata2.csv")
X = sm.add_constant(dt.select_dtypes("number").drop(columns="Loan_Amount"))
Y = dt["Loan_Amount"]
print(sm.OLS(Y,X, missing='drop').fit().params)
