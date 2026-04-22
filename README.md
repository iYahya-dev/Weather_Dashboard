# Weather Dashboard

A simple Flask web application that displays real-time weather information for any city using the OpenWeatherMap API.

This project was built to practice **Flask development**, **API integration**, **error handling**, and **responsive UI design**.

---

## Features

- Search weather by city name
- Display current temperature in **Celsius**
- Show weather condition with icon
- View **feels-like temperature**, **humidity**, **wind speed**, and **pressure**
- Clean and responsive interface built with **Bootstrap 5**
- Handles invalid city names and failed API requests gracefully

---

## Tech Stack

- **Backend:** Flask, Python
- **Frontend:** HTML, CSS, Bootstrap 5, Jinja2
- **API:** OpenWeatherMap
- **HTTP Client:** requests

---

## Project Structure

```bash
weather_dashboard/
├── weather_app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Overview

The application accepts a city name from the user, sends a request to the OpenWeatherMap API, extracts the required weather details, and displays them in a clean dashboard layout.

The project focuses on building a simple but practical weather app with a clear user interface and straightforward backend logic.

---

## Key Learning Areas

- Building routes and handling form input in Flask
- Working with third-party REST APIs
- Parsing JSON responses in Python
- Displaying dynamic data using Jinja2 templates
- Improving frontend presentation with Bootstrap
- Handling invalid input and request failures cleanly

---


## Credits

- Weather data from **OpenWeatherMap**
- Built with **Flask** and **Bootstrap 5**