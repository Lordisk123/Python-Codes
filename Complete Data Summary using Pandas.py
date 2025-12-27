import pandas as pd  
import numpy as np
df = pd.read_csv(r"C:\Users\subra\Downloads\1. Ongoing Stuff\MBA (Data Science and AI)\2. Term-2\MGNM801 - Python\creditriskdata2.csv")
dt = df.describe(include="all")
print(dt)
