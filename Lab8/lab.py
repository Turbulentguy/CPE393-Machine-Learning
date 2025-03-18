from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import os
import numpy as np


def preprocess_data(df):
    # Fill missing values
    df["Item"].fillna("Unknown", inplace=True)
    df["Price Per Unit"].fillna(df["Price Per Unit"].median(), inplace=True)
    df["Quantity"].fillna(df["Quantity"].median(), inplace=True)
    df["Total Spent"].fillna(df["Total Spent"].median(), inplace=True)
    df["Discount Applied"].fillna("No Discount", inplace=True)  # Assuming it's categorical
    
    # Convert categorical variables using Label Encoding
    label_encoders = {}
    categorical_columns = ["Category", "Item", "Payment Method", "Location", "Discount Applied"]
    
    for col in categorical_columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    
    return df, label_encoders


def train_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "retain_store_sales.csv")
    df = pd.read_csv(csv_path)
    
    df, label_encoders = preprocess_data(df)
    
    X = df.drop(columns=["Discount Applied", "Transaction ID", "Customer ID", "Transaction Date"])  # Feature set
    y = df["Discount Applied"]  # Target variable
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Hyperparameter tuning using RandomizedSearchCV
    param_dist = {
        "n_estimators": [50, 100, 200],
        "max_depth": [None, 10, 20, 30],
        "max_features": ["sqrt", "log2"],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    }
    
    model = RandomForestClassifier(random_state=42)
    random_search = RandomizedSearchCV(model, param_dist, n_iter=10, cv=3, scoring='accuracy', n_jobs=-1, random_state=42)
    
    random_search.fit(X_train, y_train)
    best_model = random_search.best_estimator_
    
    y_pred = best_model.predict(X_test)
    
    print("Best Parameters:", random_search.best_params_)
    print(classification_report(y_test, y_pred))
    

if __name__ == "__main__":
    train_model()