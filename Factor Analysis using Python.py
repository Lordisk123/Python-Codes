import subprocess, sys
for pkg in ['pandas','scikit-learn']:
    try:
        __import__(pkg.replace('-','_'))
    except ImportError:
        subprocess.check_call([sys.executable,"-m","pip","install",pkg])

import pandas as pd
from sklearn.decomposition import FactorAnalysis
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"C:\Users\subra\Downloads\1. Ongoing Stuff\MBA (Data Science and AI)\2. Term-2\MGNM801 - Python\creditriskdata2.csv")
num_df = df.select_dtypes(include='number').dropna()
 
X = StandardScaler().fit_transform(num_df)

fa = FactorAnalysis(n_components=3,random_state=0)

factors = fa.fit_transform(X)

loadings = pd.DataFrame(fa.components_.T,
                        index = num_df.columns, columns = [f'Factor{i+1}' for i in range(3)])

print("\n===FACTOR LOADINGS===")
print(loadings.round(3).to_string())

factor_scores = pd.DataFrame(factors,columns=[f'Factor{i+1}' for i in range(3)])
print("\n===FIRST 5 FACTOR SCORES===")
print(factor_scores.head().round(3).to_string())
