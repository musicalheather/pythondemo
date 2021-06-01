from flask import Flask
from flask import request
from scipy.constants import convert_temperature

app = Flask(__name__)

@app.route("/")
def index():
# Celsius to Fahrenheit
    celsius = request.args.get('celsius', type=int)
    fahrenheit = request.args.get('fahrenheit', type=int)
    kelvin = request.args.get('kelvin', type=int)
    rankine = request.args.get('rankine', type=int)

    if celsius:
        fahrenheit = float(convert_temperature(celsius, 'Celsius', 'Fahrenheit'))
        kelvin = float(convert_temperature(celsius, 'Celsius', 'Kelvin'))
        rankine = float(convert_temperature(celsius, 'Celsius', 'Rankine'))
    if fahrenheit:
        celsius = float(convert_temperature(fahrenheit, 'Fahrenheit', 'Celsius'))
        rankine = float(convert_temperature(fahrenheit, 'Fahrenheit', 'Rankine'))
        kelvin = float(convert_temperature(fahrenheit, 'Fahrenheit', 'Kelvin'))
    if kelvin:
        celsius = float(convert_temperature(kelvin, 'Kelvin', 'Celsius'))
        fahrenheit = float(convert_temperature(kelvin, 'Kelvin', 'Fahrenheit'))
        rankine = float(convert_temperature(kelvin, 'Kelvin', 'Rankine'))
    if rankine:
        kelvin = float(convert_temperature(rankine, 'Rankine', 'Kelvin'))
        fahrenheit = float(convert_temperature(rankine, 'Rankine', 'Fahrenheit'))
        celsius = float(convert_temperature(rankine, 'Rankine', 'Fahrenheit'))

    return (
        """<form action="" method="get">
                Celsius temperature: <input type=text name="celsius">
                <input type="submit" value="Convert to Fahrenheit"><br>
                Fahrenheit temperature: <input type=text name="fahrenheit">
                <input type="submit" value="Convert to Celsius"><br>
                Kelvin temperature: <input type=text name="Kelvin">
                <input type="submit" value="Convert to Kelvin"><br>
                Rankine temperature: <input type=text name="Rankine">
                <input type="submit" value="Convert to Rankine"><br>
            </form>"""
        + "Fahrenheit: "
        + str(fahrenheit)
        + "<br>"
        + "Celsius: "
        + str(celsius)
        + "<br>"
        + "Kelvin: "
        + str(kelvin)
        + "<br>"
        + "rankine: "
        + str(rankine)
        + "<br>"
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)