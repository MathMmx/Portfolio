import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    api_key = 'acad1bfd148e53f75d439a984f6fb6eb'  
    location = request.form['location']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_info = {
            'location': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description']
        }
        return jsonify(weather_info)
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), 400

if __name__ == '__main__':
    app.run(debug=True)