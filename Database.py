import pandas as pd
df = pd.read_csv(r"C:\Users\subra\Downloads\1. Ongoing Stuff\MBA (Data Science and AI)\2. Term-2\MGNM801 - Python\creditriskdata2.csv", encoding = "latin")
print("Data Loaded:")
print(df.head())
if 'Net_Profit' in df.columns:
    latest_profit = df['Net_Profit'].iloc[-1]
    if latest_profit > 0:
        print("Axis Bank reported a PROFIT in the lastest year.")
    else:
        print("Axis Bank reported a LOSS in the lastest year.")
else:
    print("The column 'Net_profit' was not found. Please check the CSV column names.")
