# Fall-Prevention-Sensors-and-AI

## Abstract:

This project aims to develop a wearable sensor system integrated with artificial intelligence (AI) to prevent falls among elderly individuals. Utilizing the NodeMCU ESP8266 microcontroller and the MPU6050 sensor module, the system monitors the user's Gyroscope and accelerometer values(balance and motion) in real-time. If a potential fall risk is detected, the system alerts the user through a buzzer. If a fall has been detected, the system sends the GPS location to a caretaker via Wi-Fi. By employing AI algorithms to analyze sensor data and predict fall risks, this project provides a proactive solution to enhance safety and independence for the elderly.

## Keywords:

Fall Prevention, Sci-kit learn, pandas, numpy, Logistic Regression, joblib, Flask, HTTP, NodeMCU ESP8266, MPU6050

## Introduction:
Falls are the most prevalent causes of injuries, particularly among the aged. Most of these fall accidents end up resulting in major injuries and a lower quality of life. The concept of this project is to create an intelligent wearable device that can predict and prevent falls by constantly monitoring the user's movements and also the orientation of his or her body. It uses an MPU6050 sensor to capture real-time accelerations and gyroscopic information that is processed by a NodeMCU ESP8266 microcontroller. This data is then stored in a server. From where, the AI model can fetch the data and make predictions. Such a system is really beneficial as integrates AI algorithms for the detection of abnormal movements so that pre-fall warnings may be issued to improve matters appreciably over classical fall-detection systems.

## Methodology:
The core of this project has been designed to capture real-time motion data-the accelerometer and gyroscope dats with the help of a MPU6050 sensor module. The NodeMCU ESP8266 processes the captured data by the sensor and transmits the data over Wi-Fi to a server where a trained AI model analyzes the sensor data based on the detection of patterns using Python libraries- Scikitlearn, and Pandas for fall risks. As soon as the AI model detects the fall, it buzzes the buzzer and sends the location of the user to the assigned caretaker with the help of the Neo 6M GPS module. This system acts as an efficient early warning mechanism that minimizes chances of falls and ensures higher safety for the user.

