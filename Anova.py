import pandas as pd 
import statsmodels.api as sm
import statsmodels.formula.api as smf
df = pd.read_csv(r"C:\Users\subra\Downloads\1. Ongoing Stuff\MBA (Data Science and AI)\2. Term-2\MGNM801 - Python\creditriskdata2.csv")
print(sm.stats.anova_lm(smf.ols('Loan_Amount~C(Loan_Status)',df).fit()))
