##### Walkthrough Document WAP\_4



Project Overview

This application retrieves real-time weather data from OpenWeather API and stores search history

Prerequisites

\- Python 3.x

\- requests library

\- OpenWeather API key

Installation Steps



1\. Install Python on your system.

2\. Open Command Prompt/Terminal.

3\. Install required package: pip install requests

4\. Create a file named weather\_app.py.

5\. Copy and paste the weather app code into the file.

6\. Save the file.

7\. Run the program using: python weather\_app.py

8\. Use the menu to search weather, view history, or exit.





Running the Application



1\. Open Command Prompt/Terminal.

2\. Navigate to the project folder.

3\. Ensure Python and requests are installed.

4\. Run the command: python weather\_app.py

5\. The Weather App menu will be displayed.

6\. Select option 1 to search for weather details.

7\. Enter the city name when prompted.

8\. View the weather information, alerts, and history.



Application Features



1\. Fetches real-time weather data using OpenWeather API.

2\. Displays temperature, humidity, and weather conditions.

3\. Provides weather alerts for extreme conditions.

4\. Stores search history in a JSON file.

5\. Allows users to view previous searches.

6\. Handles invalid city names gracefully.

7\. Includes a menu-driven interface.

8\. Supports continuous weather searches until exit.



User Workflow



1\. Start the Weather Application.

2\. Select an option from the main menu.

3\. Enter a city name to search weather details.

4\. Application fetches data from the API.

5\. Weather information is displayed.

6\. Alerts are shown if conditions match criteria.

7\. Search details are saved to history.

8\. User can view history or exit the application.

Expected Output

1. Main menu is displayed on startup.

2\. User enters a valid city name.

3\. Weather details are retrieved successfully.

4\. Temperature is displayed in Celsius.

5\. Humidity percentage is shown.

6\. Weather condition description is displayed.

7\. Alerts appear when necessary.

8\. Search history is stored and accessible.



Error Handling



1\. Checks for invalid city names.

2\. Handles HTTP request errors.

3\. Handles network connectivity issues.

4\. Prevents application crashes on API failures.

5\. Detects missing history files.

6\. Handles corrupted JSON history files.

7\. Displays meaningful error messages.

8\. Allows the user to continue using the application.





