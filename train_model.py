import pandas as pd
data = pd.read_csv("personal_finance_tracker_dataset.csv")
print(data.head())
print(data.columns)
print(data.info())
print(data.shape)
data = data.dropna()
print(data.shape)
data = data.drop_duplicates()
print(data.shape)
print(data.head())
print(data.columns)
X = data[['monthly_income',
          'monthly_expense_total',
          'credit_score',
          'loan_payment',
          'investment_amount',
          'actual_savings']]
y = data['savings_goal_met']
print(X.head())
print(y.head())
import pandas as pd

data = pd.read_csv("personal_finance_tracker_dataset.csv")

print(data.head())
print(data.columns)
print(data.info())
print(data.shape)

data = data.dropna()
data = data.drop_duplicates()
X = data[['monthly_income',
          'monthly_expense_total',
          'credit_score',
          'loan_payment',
          'investment_amount',
          'actual_savings']]
y = data['savings_goal_met']
print(X.head())
print(y.head())
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print(X_train.shape)
print(X_test.shape)
model = RandomForestClassifier()
model.fit(X_train, y_train)
print("Model trained successfully!")
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)
import joblib
joblib.dump(model, "model.pkl")
print("Model saved successfully!")
