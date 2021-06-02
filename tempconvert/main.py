from flask import Flask
from flask import request
from scipy.constants import convert_temperature

app = Flask(__name__)

def convert (value, format):
    collector = list()

    for to_format in ("celsius", "fahrenheit", "kelvin", "rankine"):
        collector.append(round(value if format == to_format else convert_temperature(value, format, to_format), 2))
    return collector
@app.route("/")
def index():
# Celsius to Fahrenheit
    try:
        params = [{'format': x[0], 'value': float(x[1])} for x in request.args.items() if x[1]][0]
        celsius, fahrenheit, kelvin, rankine = convert(**params)
    except IndexError:
        celsius = fahrenheit = kelvin = rankine = None

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
    app.run(host="0.0.0.0", port=8000, debug=False)