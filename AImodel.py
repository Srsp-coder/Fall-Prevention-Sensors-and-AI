import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
file_path = 'fall-dataset/fall-dataset-raw/Subject1-raw.csv'
df = pd.read_csv(file_path)
x = df[['Pitch', 'Roll', 'Yaw']]
y = df['Fall']

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

# Feature Scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Model Training
lr = LogisticRegression()
lr.fit(x_train, y_train)

# Save model and scaler
joblib.dump(lr, 'fall_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
