import tkinter as tk
import requests

API_KEY = "b491dd24ce4d44b5bc1135059250707"

def get_weather():
    city = city_entry.get()
    url = f"https://api.weatherapi.com/v1/current.json?key=b491dd24ce4d44b5bc1135059250707&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["current"]["temp_f"]
        description = data["current"]["condition"]["text"]

        result_label.config(
            text=f"{city.title()}:\n{temp}°F\n{description.title()}"
        )
    else:
        result_label.config(text="City not found. Try again.")

# -------------------- GUI ---------------------
window = tk.Tk()
window.title("Weather App")
window.geometry("300x150")

city_entry = tk.Entry(window, width=25)
city_entry.pack(pady=5)
city_entry.insert(0, "Enter a city")

get_button = tk.Button(window, text="Get Weather", command=get_weather)
get_button.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

window.mainloop()