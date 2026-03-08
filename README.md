# AI-Based-Vehicle-Health-Monitoring-System-using-IoT-Devices
Project Overview

This project presents an AI-based vehicle health monitoring system designed to monitor important vehicle parameters in real time using IoT technology. The system collects data from simulated sensors such as temperature, gas level, battery voltage, and vibration using an ESP32 microcontroller.

The sensor data is transmitted to the ThingSpeak cloud platform where it is stored and visualized. A web-based dashboard built with Streamlit retrieves the cloud data and displays the vehicle health status in real time.

The system uses rule-based AI logic to analyze sensor readings and classify vehicle conditions into three stages: Healthy, Warning, and Critical. When abnormal conditions occur, the system generates alerts and provides possible causes for the detected issue. This helps users understand the problem and take appropriate maintenance actions.

This project demonstrates the integration of IoT devices, cloud computing, and intelligent monitoring techniques to create an effective vehicle diagnostic system.

⸻

Key Features
	•	Real-time monitoring of vehicle parameters
	•	IoT-based sensor data acquisition using ESP32
	•	Cloud data storage and visualization using ThingSpeak
	•	Real-time dashboard built using Streamlit
	•	Multi-stage vehicle health classification (Healthy / Warning / Critical)
	•	Root cause analysis for detected faults
	•	Smart alert mechanism triggered when system status changes
	•	Email alert notification system
	•	Explainable AI-based diagnostic logic

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

Sensor Simulation → ESP32 → ThingSpeak Cloud → AI Analysis → Streamlit Dashboard → Alert System

⸻

Parameters Monitored

The system monitors several important vehicle parameters including:
	•	Engine Temperature
	•	Gas Level (Leak Detection)
	•	Battery Voltage
	•	Vibration / Mechanical Instability

These parameters help identify potential issues such as overheating, gas leakage, battery failure, and abnormal mechanical vibrations.

⸻

Vehicle Health Classification

Healthy

All vehicle parameters are within the normal operating range.

Warning

One or more parameters exceed the normal range but are not yet critical.

Critical

Severe abnormal conditions detected that require immediate attention.

⸻

Novelty of the Project

The novelty of this project lies in implementing an Explainable AI-based vehicle diagnostic system that not only detects abnormal conditions but also provides possible causes for the detected issue.

The system also introduces a state-transition alert mechanism, where alerts are triggered only when the vehicle health status changes. This prevents unnecessary notifications and improves monitoring efficiency.

⸻

Possible Cause Detection

Engine Overheating

Possible causes may include:
	•	Low coolant level
	•	Radiator blockage
	•	Cooling fan failure
	•	Low engine oil level
	•	Continuous heavy load driving

Gas Leakage

Possible causes may include:
	•	Fuel pipe leakage
	•	Loose gas pipe connections
	•	Fuel injector malfunction
	•	Improper combustion

Battery Issues

Possible causes may include:
	•	Battery aging
	•	Alternator failure
	•	Loose battery terminals
	•	Charging system malfunction

This diagnostic reasoning helps users understand the possible source of the problem.

⸻

Applications
	•	Smart vehicle monitoring systems
	•	Fleet management systems
	•	Predictive maintenance platforms
	•	Automotive diagnostics

⸻

Future Improvements

Future improvements for this project may include:
	•	Integration with real hardware sensors
	•	Machine learning based predictive maintenance
	•	Mobile application integration
	•	SMS and push notification alerts
	•	GPS-based vehicle tracking
