import requests
import json
from datetime import datetime

API_KEY = "bd5e378503939ddaee76f12ad7a97608"
HISTORY_FILE = "history.json"


# Weather API
def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Network/API Error: {e}")
        return None


# Display Weather
def display_weather(data):
    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\n===== WEATHER DASHBOARD =====")
    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", condition)

    return city, temp, humidity, condition


# Alert System
def check_alerts(temp, condition):
    print("\n===== ALERTS =====")

    if temp > 35:
        print("⚠ High Temperature Alert!")

    elif temp < 0:
        print("⚠ Freezing Temperature Alert!")

    if "rain" in condition.lower():
        print("⚠ Rain Warning!")

    elif "snow" in condition.lower():
        print("⚠ Snow Warning!")


# Save History
def save_history(city, temp, condition):
    record = {
        "city": city,
        "timestamp": str(datetime.now()),
        "temperature": temp,
        "condition": condition
    }

    try:
        with open(HISTORY_FILE, "r") as file:
            data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(record)

    with open(HISTORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


# View History
def view_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            data = json.load(file)

        print("\n===== LAST 5 SEARCHES =====")

        for record in data[-5:]:
            print(
                f"{record['city']} | "
                f"{record['temperature']} °C | "
                f"{record['condition']} | "
                f"{record['timestamp']}"
            )

    except FileNotFoundError:
        print("No history found.")

    except json.JSONDecodeError:
        print("History file is corrupted.")


# Main Menu
def main():
    while True:
        print("\n===== WEATHER APP MENU =====")
        print("1. Search Weather")
        print("2. View History")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            city = input("Enter city name: ")

            data = get_weather(city)

            if data is None:
                continue

            if str(data.get("cod")) != "200":
                print("City not found or API error")
                continue

            city, temp, humidity, condition = display_weather(data)

            check_alerts(temp, condition)

            save_history(city, temp, condition)

        elif choice == "2":
            view_history()

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
