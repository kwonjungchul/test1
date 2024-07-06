import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def train_model(file_path):
    print(f"Reading data from {file_path}...")
    data = pd.read_csv(file_path)
    print("Data read successfully.")
    
    features = ['short_mavg', 'long_mavg', 'volatility']
    target = 'signal'
    
    # Fill missing values
    data = data.fillna(0)

    print("Splitting data into training and test sets...")
    X = data[features]
    y = data[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training the model...")
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    print("Evaluating the model...")
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)
    
    return model

# Train the model using the augmented data
model = train_model('augmented_strategy_processed_stock_data.csv')
