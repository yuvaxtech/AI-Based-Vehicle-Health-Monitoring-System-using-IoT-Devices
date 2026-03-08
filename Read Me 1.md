AI-Based Vehicle Health Monitoring System using IoT

Project Overview

This project presents an AI-based vehicle health monitoring system designed to monitor critical vehicle parameters in real time using IoT technology. The system collects data from multiple simulated sensors such as temperature, gas level, battery voltage, and vibration using an ESP32 microcontroller. The collected data is transmitted to the ThingSpeak cloud platform for storage and visualization.

A web-based dashboard built with Streamlit displays the real-time vehicle health status. The system analyzes sensor readings using rule-based AI logic and classifies the vehicle condition into three stages: Healthy, Warning, and Critical. Whenever abnormal conditions are detected, the system generates alerts and provides possible causes for the issue to help users understand the problem.

This project demonstrates the integration of IoT, cloud computing, and intelligent monitoring techniques to create a simple yet effective vehicle diagnostic system.

⸻

Key Features
	•	Real-time vehicle parameter monitoring
	•	IoT-based sensor data acquisition using ESP32
	•	Cloud data storage and visualization using ThingSpeak
	•	Web-based dashboard built with Streamlit
	•	Multi-stage vehicle health classification (Healthy / Warning / Critical)
	•	Root cause analysis for detected faults
	•	Smart alert system that triggers notifications when vehicle status changes
	•	Email notification system for critical conditions

⸻

Technologies Used
	•	Programming Language: Python, C++
	•	Microcontroller: ESP32
	•	IoT Simulator: Wokwi
	•	Cloud Platform: ThingSpeak
	•	Dashboard Framework: Streamlit
	•	Communication Protocol: HTTP API

⸻

System Architecture

The system follows a modular IoT architecture:

Sensor Simulation → ESP32 Microcontroller → Cloud Platform (ThingSpeak) → AI Analysis → Dashboard Visualization → Alert System

⸻

Parameters Monitored

The system monitors the following vehicle parameters:
	•	Engine Temperature
	•	Gas Level (Leak Detection)
	•	Battery Voltage
	•	Vibration / Mechanical Instability

These parameters help detect common vehicle issues such as overheating, fuel leakage, battery failure, and abnormal mechanical vibration.

⸻

Vehicle Health Classification

The system classifies vehicle health into three categories:

Healthy:
All parameters are within the normal operating range.

Warning:
One or more parameters exceed the normal threshold but are not yet critical.

Critical:
Severe abnormal conditions detected requiring immediate attention.

⸻

Novelty of the Project

The novelty of this project lies in implementing an explainable AI-based vehicle diagnostic system that not only detects abnormal conditions but also suggests possible causes for the detected fault.

Additionally, the system introduces a state-transition alert mechanism that triggers notifications only when the vehicle status changes, reducing redundant alerts and improving monitoring efficiency.

⸻

Possible Causes Detection

When abnormal conditions are detected, the system provides possible causes such as:

Engine Overheating:
	•	Low coolant level
	•	Radiator blockage
	•	Cooling fan failure
	•	Low engine oil level
	•	Continuous heavy load driving

Gas Leakage:
	•	Fuel pipe leakage
	•	Loose connections
	•	Injector malfunction
	•	Improper combustion

Battery Issues:
	•	Battery aging
	•	Alternator failure
	•	Loose terminals
	•	Charging system fault

This feature improves user understanding and helps in faster diagnosis.

⸻

Applications
	•	Smart vehicle monitoring systems
	•	Fleet management systems
	•	Predictive maintenance platforms
	•	Automotive diagnostics

⸻

Future Improvements

Future enhancements may include:
	•	Integration of real hardware sensors
	•	Machine learning-based fault prediction
	•	Mobile application integration
	•	SMS and push notification alerts
	•	GPS-based vehicle tracking

⸻

Conclusion

This project demonstrates a practical approach for vehicle health monitoring by combining IoT sensors, cloud computing, and AI-based diagnostic logic. The system provides real-time monitoring, intelligent alerts, and root cause analysis, making it a useful solution for improving vehicle maintenance and safety.

⸻
