from flask import Flask
from flask import request

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
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"
def rankine_from(celsius):
    try:
        rankine = float(celsius) * 9 / 5 + 32
        rankine = round(rankine, 3)  # Round to three decimal places
        return str(rankine)
    except ValueError:
        return "invalid input"
def kelvin_from(celsius):
    try:
        kelvin = float(celsius) + 273.15
        kelvin = round(kelvin, 3)  # Round to three decimal places
        return str(kelvin)
    except ValueError:
        return "invalid input"

def celsius_from(fahrenheit):
    try:
        celsius = float(fahrenheit) * 5 / 9 - 32
        celsius = round(celsius, 3)  # Round to three decimal places
        return str(celsius)
    except ValueError:
        return "invalid input"
def rankine_from(fahrenheit):
    try:
        rankine = float(fahrenheit) * 9 / 5 + 32
        rankine = round(rankine, 3)  # Round to three decimal places
        return str(rankine)
    except ValueError:
        return "invalid input"
def kelvin_from(fahrenheit):
    try:
        kelvin = float(fahrenheit) + 273.15
        kelvin = round(kelvin, 3)  # Round to three decimal places
        return str(kelvin)
    except ValueError:
        return "invalid input"

def celsius_from(kelvin):
    try:
        celsius = float(fahrenheit) * 5 / 9 - 32
        celsius = round(celsius, 3)  # Round to three decimal places
        return str(celsius)
    except ValueError:
        return "invalid input"
def rankine_from(kelvin):
    try:
        rankine = float(fahrenheit) * 9 / 5 + 32
        rankine = round(rankine, 3)  # Round to three decimal places
        return str(rankine)
    except ValueError:
        return "invalid input"
def fahrenheit_from(kelvin):
    try:
        kelvin = float(kelvin) + 273.15
        kelvin = round(kelvin, 3)  # Round to three decimal places
        return str(kelvin)
    except ValueError:
        return "invalid input"

def celsius_from(rankine):
    try:
        celsius = float(fahrenheit) * 5 / 9 - 32
        celsius = round(celsius, 3)  # Round to three decimal places
        return str(celsius)
    except ValueError:
        return "invalid input"
def kelvin_from(rankine):
    try:
        kelvin = float(rankine) * 9 / 5 + 32
        kelvin = round(rankine, 3)  # Round to three decimal places
        return str(kelvin)
    except ValueError:
        return "invalid input"
def fahrenheit_from(rankine):
    try:
        fahrenheit = float(rankine) + 273.15
        fahrenheit = round(rankine, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)