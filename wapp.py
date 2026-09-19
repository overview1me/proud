import requests
import streamlit as st

st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ Weather App")
st.write("Enter a city to get the current weather and 7-day forecast.")

city = st.text_input("City", "Bengaluru")

weather_icons = {
    0: "☀️",
    1: "🌤️",
    2: "⛅",
    3: "☁️",
    45: "🌫️",
    48: "🌫️",
    51: "🌦️",
    53: "🌦️",
    55: "🌧️",
    61: "🌧️",
    63: "🌧️",
    65: "🌧️",
    71: "🌨️",
    73: "🌨️",
    75: "❄️",
    80: "🌦️",
    81: "🌦️",
    82: "🌧️",
    95: "⛈️",
    96: "⛈️",
    99: "⛈️"
}

weather_text = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Fog",
    51: "Light drizzle",
    53: "Drizzle",
    55: "Heavy drizzle",
    61: "Light rain",
    63: "Rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Rain showers",
    82: "Heavy rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm + hail",
    99: "Thunderstorm + heavy hail"
}

if st.button("Get Weather"):

    # Find city coordinates
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geo_response = requests.get(geo_url, params=geo_params)

    if geo_response.status_code != 200:
        st.error("Could not connect to the location service.")
        st.stop()

    geo_data = geo_response.json()

    if "results" not in geo_data:
        st.error("City not found.")
        st.stop()

    location = geo_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]
    city_name = location["name"]
    country = location.get("country", "")

    # Get weather
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "precipitation",
            "weather_code",
            "wind_speed_10m"
        ],
        "daily": [
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min"
        ],
        "forecast_days": 7,
        "timezone": "auto"
    }

    response = requests.get(weather_url, params=weather_params)

    if response.status_code != 200:
        st.error("Could not get weather data.")
        st.stop()

    data = response.json()
    current = data["current"]

    st.subheader(f"{city_name}, {country}")

    code = current["weather_code"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Temperature",
            f"{current['temperature_2m']} °C"
        )

    with col2:
        st.metric(
            "Feels Like",
            f"{current['apparent_temperature']} °C"
        )

    st.write(
        f"### {weather_icons.get(code, '🌤️')} "
        f"{weather_text.get(code, 'Unknown')}"
    )

    st.write(
        f"💧 Humidity: {current['relative_humidity_2m']}%"
    )

    st.write(
        f"💨 Wind: {current['wind_speed_10m']} km/h"
    )

    st.write(
        f"🌧️ Precipitation: {current['precipitation']} mm"
    )

    st.divider()

    st.subheader("7-Day Forecast")

    dates = data["daily"]["time"]
    max_temps = data["daily"]["temperature_2m_max"]
    min_temps = data["daily"]["temperature_2m_min"]
    codes = data["daily"]["weather_code"]

    for i in range(7):

        st.write(
            f"**{dates[i]}** — "
            f"{weather_icons.get(codes[i], '🌤️')} "
            f"{weather_text.get(codes[i], 'Unknown')} | "
            f"🌡️ {min_temps[i]}°C → {max_temps[i]}°C"
        )