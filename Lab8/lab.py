from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd
import os

def lab():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    csv_path = os.path.join(BASE_DIR, "retain_store_sales.csv")

    df = pd.read_csv(csv_path)

    X = df.drop(columns=["Discount Applied"])  # Feature

    y = df["Discount Applied"]  # Target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
    
    model = RandomForestClassifier(n_estimators = 100, max_features = "sqrt", max_depth = 6, max_leaf_nodes = 6)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(classification_report(y_pred, y_test))