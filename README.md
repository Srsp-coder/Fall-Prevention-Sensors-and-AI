# Wearable sensor with Artificial Intelligence for prevention of falls in elderly people

## Abstract:

This project aims to develop a wearable sensor system integrated with artificial intelligence (AI) to prevent falls among elderly individuals. Utilizing the NodeMCU ESP8266 microcontroller and the MPU6050 sensor module, the system monitors the user's Gyroscope and accelerometer values(balance and motion) in real-time. If a potential fall risk is detected, the system alerts the user through a buzzer. If a fall has been detected, the system sends the GPS location to a caretaker via Wi-Fi. By employing AI algorithms to analyze sensor data and predict fall risks, this project provides a proactive solution to enhance safety and independence for the elderly.

## Keywords:

Fall Prevention, Sci-kit learn, pandas, numpy, Logistic Regression, joblib, Flask, HTTP, WiFi, NodeMCU ESP8266, MPU6050

## Introduction:
Falls are the most prevalent causes of injuries, particularly among the aged. Most of these fall accidents end up resulting in major injuries and a lower quality of life. The concept of this project is to create an intelligent wearable device that can predict and prevent falls by constantly monitoring the user's movements and also the orientation of his or her body. It uses an MPU6050 sensor to capture real-time accelerometer and gyroscopic information that is processed by a NodeMCU ESP8266 microcontroller. This data is then stored in a server. From where, the AI model can fetch the data and make predictions. Such a system is really beneficial as integrates AI algorithms for the detection of abnormal movements so that pre-fall warnings may be issued to improve matters appreciably over classical fall-detection systems.

## Methodology:
The core of this project has been designed to capture real-time motion data-the accelerometer and gyroscope dats with the help of a MPU6050 sensor module. The NodeMCU ESP8266 processes the captured data by the sensor and transmits the data over Wi-Fi to a server where a trained AI model analyzes the sensor data based on the detection of patterns using Python libraries- Scikitlearn, and Pandas for fall risks. As soon as the AI model detects the fall, it buzzes the buzzer and sends the location of the user to the assigned caretaker with the help of the Neo 6M GPS module. This system acts as an efficient early warning mechanism that minimizes chances of falls and ensures higher safety for the user.

**Circuit Diagram:**

![circuit diagram]()


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
The Wearable Sensor with AI for Fall Prevention successfully detects high fall-risk situations in real time using motion data from the MPU6050. The AI model accurately predicts fall risks, while the buzzer alerts users to adjust their posture. The system's wireless capabilities make it practical for wearable applications without the need for cumbersome connections. Real-time feedback and GPS integration ensure timely notifications to caregivers in emergencies. This project demonstrates the potential of AI and IoT in enhancing elderly care and safety. Overall, the results show the system is effective, low-cost, and scalable for various environments.

## Conclusion:
The Wearable Sensor with AI for Fall Prevention effectively utilizes real-time sensor data and machine learning to predict and prevent falls in the elderly. It gives immediate feedback and generates wireless alerts ensuring safety and care. It is cost-effective,practical and reliable for various settings. Future improvements could focus on refining model for even more great accuracy.
