# Weather_App
Build a Command-Line Interface (CLI) application that retrieves real-time weather information using the OpenWeather API. The application will allow users to search weather data for a city, view temperature in Celsius or Fahrenheit, generate weather alerts based on predefined thresholds, and maintain a searchable history of previous weather queries.
Implementation Plan - Weather_Project

Project Overview

Build a Command-Line Interface (CLI) application that retrieves real-time weather information using the OpenWeather API. The application will allow users to search weather data for a city, view temperature in Celsius or Fahrenheit, generate weather alerts based on predefined thresholds, and maintain a searchable history of previous weather queries.

User Review Required

No major breaking changes are expected as this is a standalone CLI application.

The project will be developed as a Python-based application and will utilize local file storage for maintaining weather search history.

Proposed Changes
[NEW] weather_dashboard.py

Main application entry point.

Responsibilities:

Display interactive CLI menu
Accept user input
Coordinate application workflow
Display weather dashboard
Handle program navigation
[NEW] Weather Data Module

Responsibilities:

Connect to OpenWeather API
Send city-based weather requests
Receive weather data responses
Parse API JSON data
Extract required weather information

Retrieved Data:

City Name
Temperature
Humidity
Weather Condition
Timestamp
[NEW] Alert System

Responsibilities:

Monitor weather conditions
Compare temperature against thresholds
Detect Rain and Snow conditions
Generate warning messages

Alert Conditions:

Temperature > 35°C (95°F)
Temperature < 0°C (32°F)
Weather Condition = Rain
Weather Condition = Snow

Example Alerts:

⚠ High Temperature Alert

⚠ Freezing Temperature Alert

⚠ Rain Warning

⚠ Snow Warning

[NEW] Search History Storage

Responsibilities:

Store successful searches
Maintain local history records
Save search details to history.json

Stored Fields:

City Name
Timestamp
Temperature
Weather Condition
[NEW] History Viewer

Responsibilities:

Read saved history records
Display the most recent five searches
Provide quick access to previously searched weather data
Data Structure

Example History Record:

{
"city": "Chennai",
"timestamp": "2026-06-15 10:30:00",
"temperature": 32,
"condition": "Clear"
}

Verification Plan
Functional Verification
Verify successful weather retrieval for valid cities
Verify Celsius temperature display
Verify Fahrenheit temperature display
Verify weather condition display
Verify humidity display
Verify high temperature alerts
Verify low temperature alerts
Verify rain alerts
Verify snow alerts
Verify history saving functionality
Verify viewing last five searches
Error Handling Verification
