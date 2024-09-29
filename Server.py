from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

app = Flask(__name__)

# Load the pre-trained model and scaler
model = joblib.load('fall_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/sensor-data', methods=['POST'])
def receive_data():
    # Extract sensor data from the POST request
    accel_x = float(request.form['accel_x'])
    accel_y = float(request.form['accel_y'])
    accel_z = float(request.form['accel_z'])
    gyro_x = float(request.form['gyro_x'])
    gyro_y = float(request.form['gyro_y'])
    gyro_z = float(request.form['gyro_z'])

    # Calculate Pitch, Roll, and Yaw (assuming simple transformations)
    pitch = np.arctan2(accel_y, np.sqrt(accel_x**2 + accel_z**2)) * 180 / np.pi
    roll = np.arctan2(-accel_x, accel_z) * 180 / np.pi
    yaw = np.arctan2(accel_z, np.sqrt(accel_x**2 + accel_y**2)) * 180 / np.pi

    # Prepare the data for prediction
    input_data = np.array([[pitch, roll, yaw]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)

    # Determine if there is a risk of falling
    fall_risk = "Fall Detected" if prediction[0] == 1 else "No Fall"

    # Send response back to client
    return jsonify({"fall_risk": fall_risk})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
