from flask import Flask

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/hello')
def hello():
    # Render the page
    return "Hello Python!"

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)
#class TempConvert(AppConfig):
#    name = 'TempConvert'

#class TempconvertConfig(AppConfig):
#    name = 'tempconvert'

#def convert_temperature(val, old_scale, new_scale):
#    """
#    Convert from a temperature scale to another one among Celsius, Kelvin,
#    Fahrenheit, and Rankine scales.
#    Parameters
#    ----------
#    val : array_like
#        Value(s) of the temperature(s) to be converted expressed in the
#        original scale.
#    old_scale: str
#        Specifies as a string the original scale from which the temperature
#        value(s) will be converted. Supported scales are Celsius ('Celsius',
#        'celsius', 'C' or 'c'), Kelvin ('Kelvin', 'kelvin', 'K', 'k'),
#        Fahrenheit ('Fahrenheit', 'fahrenheit', 'F' or 'f'), and Rankine
#        ('Rankine', 'rankine', 'R', 'r').
#    new_scale: str
#        Specifies as a string the new scale to which the temperature
#        value(s) will be converted. Supported scales are Celsius ('Celsius',
#        'celsius', 'C' or 'c'), Kelvin ('Kelvin', 'kelvin', 'K', 'k'),
#        Fahrenheit ('Fahrenheit', 'fahrenheit', 'F' or 'f'), and Rankine
#        ('Rankine', 'rankine', 'R', 'r').
#    Returns
#    -------
#    res : float or array of floats
#        Value(s) of the converted temperature(s) expressed in the new scale.
#    Notes
#    -----
#    .. versionadded:: 0.18.0
#    Examples
#    --------
#    >>> from scipy.constants import convert_temperature
#    >>> convert_temperature(np.array([-40, 40]), 'Celsius', 'Kelvin')
#    array([ 233.15,  313.15])
#    """
#    # Convert from `old_scale` to Kelvin
#    if old_scale.lower() in ['celsius', 'c']:
#        tempo = _np.asanyarray(val) + zero_Celsius
#    elif old_scale.lower() in ['kelvin', 'k']:
#        tempo = _np.asanyarray(val)
#    elif old_scale.lower() in ['fahrenheit', 'f']:
#        tempo = (_np.asanyarray(val) - 32) * 5 / 9 + zero_Celsius
#    elif old_scale.lower() in ['rankine', 'r']:
#        tempo = _np.asanyarray(val) * 5 / 9
#    else:
#        raise NotImplementedError("%s scale is unsupported: supported scales "
#                                  "are Celsius, Kelvin, Fahrenheit, and "
#                                  "Rankine" % old_scale)
#    # and from Kelvin to `new_scale`.
#    if new_scale.lower() in ['celsius', 'c']:
#        res = tempo - zero_Celsius
#    elif new_scale.lower() in ['kelvin', 'k']:
#        res = tempo
#    elif new_scale.lower() in ['fahrenheit', 'f']:
#        res = (tempo - zero_Celsius) * 9 / 5 + 32
#    elif new_scale.lower() in ['rankine', 'r']:
#        res = tempo * 9 / 5
#    else:
#        raise NotImplementedError("'%s' scale is unsupported: supported "
#                                  "scales are 'Celsius', 'Kelvin', "
#                                  "'Fahrenheit', and 'Rankine'" % new_scale)
#
#    return res

