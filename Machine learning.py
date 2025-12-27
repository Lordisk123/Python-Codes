import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

path = r"C:\Users\subra\Downloads\1. Ongoing Stuff\MBA (Data Science and AI)\2. Term-2\MGNM801 - Python\creditriskdata2.csv"
df = pd.read_csv(path)

num_df = df.select_dtypes(include='number').fillna(df.median(numeric_only=True))

target_col = 'loan_status' if 'loan_status' in df.columns else df.columns[-1]
X = num_df.drop(columns=[target_col], errors='ignore')
y = df[target_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(max_depth=4, random_state=0, criterion='entropy')
model.fit(X_train, y_train)

print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, model.predict(X_test)))

plt.figure(figsize=(20,10))
plot_tree(model, 
          feature_names=X.columns, 
          class_names=[str(c) for c in model.classes_],
          filled=True, 
          rounded=True, 
          fontsize=10)
plt.title("Credit Risk Decision Tree (Pruned)")
plt.show()
