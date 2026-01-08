import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name.")
        return


    api_key = "64615e6a8c6c4e41a8a5980db3108ac7" 
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' # Use metric units (Celsius)
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Raise an exception for HTTP errors
        data = response.json()

        # Parse data
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Update labels
        result_label.config(text=f"Weather in {city_name}, {country} 🌍:\n"
                                 f"Temperature: {temp}°C 🌡️\n"
                                 f"Condition: {description.capitalize()} 🌤️\n"
                                 f"Humidity: {humidity}% 💧\n"
                                 f"Wind Speed: {wind_speed} m/s 💨")

    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            messagebox.showerror("Error", "City not found.")
        elif response.status_code == 401:
             messagebox.showerror("Error", "Invalid API Key. Please check your code.")
        else:
            messagebox.showerror("Error", f"HTTP Error: {err}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error connecting to API: {e}")
    except KeyError:
        messagebox.showerror("Error", "Unexpected data format received.")


# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

# Title Label
title_label = tk.Label(root, text="Weather Forecast", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

# City Entry
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

city_label = tk.Label(input_frame, text="Enter City:")
city_label.pack(side=tk.LEFT, padx=5)

city_entry = tk.Entry(input_frame, width=20)
city_entry.pack(side=tk.LEFT, padx=5)

# Search Button
search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify=tk.LEFT)
result_label.pack(pady=20)

# Run the app
if __name__ == "__main__":
    root.mainloop()
