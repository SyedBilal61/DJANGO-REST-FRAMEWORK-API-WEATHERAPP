# DJANGO-REST-FRAMEWORK-API-WEATHERAPP
#**Weather Forecast API**
**Overview**
Weather Forecast API is a RESTful service that provides weather forecasts based on user queries. The API allows users to retrieve current weather information by specifying location, date, and time. It supports the following HTTP methods:

GET: Retrieve weather forecasts.
POST: Submit queries for weather information.
This project also includes a frontend built with Python and Django to interact with the API. The frontend features a user-friendly interface for checking weather forecasts.

**Features**
Weather Forecast Retrieval: Get up-to-date weather information by specifying the city.
Responsive Design: A clean and modern interface using Bootstrap for a great user experience.
Carousel: Showcases weather-related imagery in a sleek, responsive slider.
Weather Details Display: View weather description, temperature, and weather icon in a neatly organized card format.
Getting Started
**Prerequisites**
Python 3.x
Django
Bootstrap (included via CDN)
**Installation**
1.  Clone the repository:
git clone https://github.com/SyedBilal61/DJANGO-REST-FRAMEWORK-API-WEATHERAPP
cd apiproject

2.  Install dependencies:
pip install -r requirements.txt

3.  Run the Django development server:

python manage.py runserver


**Usage**
Checking Weather: Enter the name of a city in the input field and click "Check" to get the current weather forecast.
Viewing Results: The weather information will be displayed below the input form, including a description, icon, temperature, date, and city name.

**API Endpoints**
GET /weather: Retrieve the current weather for a specified city.
POST /weather: Submit a new weather query.

**Project Structure**
index.html: The main HTML file for the frontend interface.
views.py: Contains the logic for handling user requests and interacting with the API.
urls.py: Routes requests to the appropriate view functions.

**Contributing**
Feel free to open issues or submit pull requests if you have suggestions or improvements.


**Contact**
For any questions or feedback, please reach out to bilalkazmi61.bk@gmail.com.

