import pandas as pd
import joblib

def load_data(file_path):
    df = pd.read_csv(file_path, index_col='date', parse_dates=True)
    return df

def predict(data, model_path):
    model = joblib.load(model_path)
    features = ['short_mavg', 'long_mavg', 'volatility']
    predictions = model.predict(data[features])
    data['predicted_close'] = predictions
    data.to_csv('predicted_stock_data.csv')
    print("Predictions saved to predicted_stock_data.csv")

data = load_data('processed_stock_data.csv')
predict(data, 'trained_model.pkl')
