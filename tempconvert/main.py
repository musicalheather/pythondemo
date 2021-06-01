from flask import Flask
from flask import request
from scipy.constants import convert_temperature

app = Flask(__name__)

@app.route("/")
def index():
# Celsius to Fahrenheit
    celsius = request.args.get("celsius", "")
    fahrenheit = request.args.get("fahrenheit", "")
    kelvin = request.args.get("kelvin", "")
    rankine = request.args.get("rankine", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
        kelvin = kelvin_from(celsius)
        rankine = rankine_from(celsius)
    if fahrenheit:
        celsius = celsius_from(fahrenheit)
        rankine = rankine_from(fahrenheit)
        kelvin = kelvin_from(fahrenheit)
    if kelvin:
        celsius = celsius_from(kelvin)
        fahrenheit = fahrenheit_from(kelvin)
        rankine = rankine_from(kelvin)
    if kelvin:
        rankine = rankine_from(kelvin)
        fahrenheit = fahrenheit_from(kelvin)
        celsius = celsius_from(kelvin)

    return (
        """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit"><br>
                Fahrenheit temperature: <input type="text" name="fahrenheit">
                <input type="submit" value="Convert to Celsius"><br>
                Kelvin temperature: <input type="text" name="Kelvin">
                <input type="submit" value="Convert to Kelvin"><br>
                Rankine temperature: <input type="text" name="Rankine">
                <input type="submit" value="Convert to Rankine"><br>
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
        + "<br>"
        + "Celsius: "
        + celsius
        + "<br>"
        + "Kelvin: "
        + kelvin
        + "<br>"
        + "rankine: "
        + rankine
        + "<br>"
    )

def fahrenheit_from(celsius):
    try:
        fahrenheit = convert_temperature(np.array([celsius, fahrenheit]), 'Celsius', 'Fahrenheit')# Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"
def rankine_from(celsius):
    try:
        rankine = convert_temperature(np.array([rankine, celsius]), 'Rankine', 'Celsius') # Round to three decimal places
        return str(rankine)
    except ValueError:
        return "invalid input"
def kelvin_from(celsius):
    try:
        kelvin = convert_temperature(np.array(kelvin, celsius]), 'Kelvin', 'Celsius') 
        return str(kelvin)
    except ValueError:
        return "invalid input"

def celsius_from(fahrenheit):
    try:
        celsius = convert_temperature(np.array([fahrenheit, celsius]), 'Fahrenheit', 'Celsius') # Round to three decimal places
        return str(celsius)
    except ValueError:
        return "invalid input"
def rankine_from(fahrenheit):
    try:
        rankine = convert_temperature(np.array([rankine, fahrenheit]), 'Rankin', 'Fahrenheit')
        return str(rankine)
    except ValueError:
        return "invalid input"
def kelvin_from(fahrenheit):
    try:
        kelvin = convert_temperature(np.array([kelvin, fahrenheit]), 'Kelvin', 'Fahrenheit') # Round to three decimal places
        return str(kelvin)
    except ValueError:
        return "invalid input"

def celsius_from(kelvin):
    try:
        celsius = convert_temperature(np.array([celsius, kelvin]), 'Celsius', 'Kelvin')
        return str(celsius)
    except ValueError:
        return "invalid input"
def rankine_from(kelvin):
    try:
        rankine = convert_temperature(np.array([rankine, kelvin]), 'Rankine', 'Kelvin')
        return str(rankine)
    except ValueError:
        return "invalid input"
def fahrenheit_from(kelvin):
    try:
        kelvin = convert_temperature(np.array([celsius, fahrenheit]), 'Celsius', 'Fahrenheit')
        return str(kelvin)
    except ValueError:
        return "invalid input"

def celsius_from(rankine):
    try:
        celsius = convert_temperature(np.array([celsius, rankine]), 'Celsius', 'Rankine')
        return str(celsius)
    except ValueError:
        return "invalid input"
def kelvin_from(rankine):
    try:
        kelvin = convert_temperature(np.array([kelvin, rankine]), 'Kelvin', 'Rankine')
        return str(kelvin)
    except ValueError:
        return "invalid input"
def fahrenheit_from(rankine):
    try:
        fahrenheit = convert_temperature(np.array([fahrenheit, rankine]), 'Fahrenheit', 'Rankine')
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)