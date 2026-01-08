# Weather App

A simple desktop weather application built with Python and Tkinter that fetches real-time weather data using the OpenWeatherMap API.

## Features

- **Real-time Weather**: Get current temperature, weather conditions, humidity, and wind speed.
- **Graphical Interface**: User-friendly GUI built with Tkinter.
- **Search by City**: Easily look up weather for any city worldwide.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository** (if applicable) or download the source code.

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Get Weather**:
   - Enter a city name in the input field (e.g., "London", "Tokyo").
   - Click the "Get Weather" button.
   - View the current weather details displayed on the screen.

## Configuration

The application currently uses a hardcoded API key for OpenWeatherMap. 
To use your own API key, edit `main.py` and replace the `api_key` variable value:

```python
api_key = "YOUR_API_KEY_HERE"
```

## Dependencies

- `requests`: For making HTTP requests to the weather API.
- `urllib3`: Dependency for requests.
- `pyOpenSSL`: For SSL/TLS support.
