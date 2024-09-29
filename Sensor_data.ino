#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

// Replace with your network credentials
const char* ssid = "Sairam";
const char* password = "pranav12";

// Server URL for data transmission
const char* serverName = "http://192.168.1.7:5000/sensor-data";

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  
  Serial.println("Connected to WiFi");
  
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 sensor!");
    while (1) {
      delay(10);
    }
  }
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  if (WiFi.status() == WL_CONNECTED) { 
    WiFiClient client;
    HTTPClient http;

    http.begin(client, serverName);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    
    // Sending accelerometer and gyroscope data to server
    String postData = "accel_x=" + String(a.acceleration.x) +
                      "&accel_y=" + String(a.acceleration.y) +
                      "&accel_z=" + String(a.acceleration.z) +
                      "&gyro_x=" + String(g.gyro.x) +
                      "&gyro_y=" + String(g.gyro.y) +
                      "&gyro_z=" + String(g.gyro.z);

    int httpResponseCode = http.POST(postData);
    Serial.println("Sensor Data Sent: " + postData);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("HTTP Response code: " + String(httpResponseCode));
      Serial.println("Response: " + response);
    }
    else {
      Serial.println("Error in sending POST: " + String(httpResponseCode));
    }

    http.end();
  }
  else {
    Serial.println("WiFi Disconnected");
  }

  delay(2000); // Send data every 2 seconds
}
