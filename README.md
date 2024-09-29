# Fall-Prevention-Sensors-and-AI

## Abstract:

This project aims to develop a wearable sensor system integrated with artificial intelligence (AI) to prevent falls among elderly individuals. Utilizing the NodeMCU ESP8266 microcontroller and the MPU6050 sensor module, the system monitors the user's Gyroscope and accelerometer values(balance and motion) in real-time. If a potential fall risk is detected, the system alerts the user through a buzzer. If a fall has been detected, the system sends the GPS location to a caretaker via Wi-Fi. By employing AI algorithms to analyze sensor data and predict fall risks, this project provides a proactive solution to enhance safety and independence for the elderly.

## Keywords:

Fall Prevention, Sci-kit learn, pandas, numpy, Logistic Regression, joblib, Flask, HTTP, NodeMCU ESP8266, MPU6050

## Introduction:
Falls are the most prevalent causes of injuries, particularly among the aged. Most of these fall accidents end up resulting in major injuries and a lower quality of life. The concept of this project is to create an intelligent wearable device that can predict and prevent falls by constantly monitoring the user's movements and also the orientation of his or her body. It uses an MPU6050 sensor to capture real-time accelerations and gyroscopic information that is processed by a NodeMCU ESP8266 microcontroller. This data is then stored in a server. From where, the AI model can fetch the data and make predictions. Such a system is really beneficial as integrates AI algorithms for the detection of abnormal movements so that pre-fall warnings may be issued to improve matters appreciably over classical fall-detection systems.

## Methodology:
The core of this project has been designed to capture real-time motion data-the accelerometer and gyroscope dats with the help of a MPU6050 sensor module. The NodeMCU ESP8266 processes the captured data by the sensor and transmits the data over Wi-Fi to a server where a trained AI model analyzes the sensor data based on the detection of patterns using Python libraries- Scikitlearn, and Pandas for fall risks. As soon as the AI model detects the fall, it buzzes the buzzer and sends the location of the user to the assigned caretaker with the help of the Neo 6M GPS module. This system acts as an efficient early warning mechanism that minimizes chances of falls and ensures higher safety for the user.

![Workflow](https://github.com/Srsp-coder/Fall-Prevention-Sensors-and-AI/blob/main/images/workflow.jpg?raw=true)

## Authors and Co-Authors:
|Institute ID|
|------------|
|U-1153|
---

| Role                | Student Name      |
| ------------------- | ----------------- |
|     Team Leader     | Tharun TV         |
| Team Member         | Sree Sai Raghav C |
| Team Member         | Sai Pranav SR     |
| Team Member         | Srri Hari TR      |
| Team Member         |Harish Raghavendra M|
| Team Member         |Shirley Claire S   |

--- 

## Results and Discussion:
The Wearable Sensor with Artificial Intelligence for Fall Prevention system successfully prevents falls in real time and in elderly patients. Real-time motion data are collected by NodeMCU ESP8266 combined with the MPU6050 sensor, then processed using an AI model to determine the possibility of a fall. Based on the acceleration and angular velocity (pitch, roll, and yaw) that are analyzed accurately, the system identifies situations where the risk of a fall is high. The integration of a buzzer allows for instant feedback to the user as they adjust their posture before the actual fall could occur.

The use of the logistic regression model trained from sensor data makes sure of proper and accurate estimation of fall risk. With proper training and fine-tuning, the model shows reliability in its performance, and so the system can be very effectively deployed in various environments such as homes, elderly care facilities, and hospitals. The GPS module includes the facility for immediate notification to caregivers in case of emergencies along with the exact location of the user.

This project may, by demonstration, show the full potential of IoT merged with AI in increasing safety opportunities for at-risk populations while sharply reducing fall-related injuries. The system relies on inexpensive, ready-availability hardware components alongside machine learning algorithms, hence indicating a cost-effective and efficient solution to preventing falls. Results yield that through continued monitoring and real-time feedback, falls could indeed be prevented and bring peace of mind to not only users but also caregivers.

All the features ensure wireless data transfer from the system, which therefore makes it fit for wearable applications. At large, the proposed system depicts AI-powered wearables revolutionizing elderly care as it actively reduces fall risks and alerts caregivers in critical situations.

## Conclusion:
The Wearable Sensor with AI for Fall Prevention effectively utilizes real-time sensor data and machine learning to predict and prevent falls in the elderly. It gives immediate feedback and generates wireless alerts ensuring safety and care. It is cost-effective,practical and reliable for various settings. Future improvements could focus on refining model for even more great accuracy.
