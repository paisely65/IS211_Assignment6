#!user/bin/env python
# -*- coding: utf-8 -*-
"""This module outlines basic temperature conversions."""


def convertCelsiusToKelvin(degrees):
    """ This function converts from Celsius to Kelvin.
    Args:
        degrees (float)
    Returns:
        A temperature value in Kelvin.
    Examples:
        >>> convertCelsiusToKelvin(225)
        498.15
   """
    kelvin = degrees + 273.15
    return kelvin


def convertCelsiusToFahrenheit(degrees):
    """This function converts from Celsius to Fahrenheit.
    Args:
        degrees (float)
    Returns:
        A temperature value in Fareheit.
    Examples
    >>> convertCelsiusToFahrenheit(35)
    95.0
    """
    Fahrenheit = (degrees * 1.8) + 32
    return Fahrenheit


def convertFahrenheitToCelsius(degrees):
    """This function converts from Fahrenheit to Celsius.
    Args:
        degrees (float)
    Returns:
        A temperature value in Celcius.
    Examples
    >>> convertFahrenheitToCelsius(80)
    26
    """
    Celsius = (degrees - 32.0) * 5./9
    return Celsius


def convertFahrenheitToKelvin(degrees):
    """This function converts from Fahrenheit to Kelvin.
    Args:
        degrees (float)
    Returns:
        A temperature value in Kelvin.
    Examples:
    >>> convertFahrenheitToKelvin(100)
    310.9277777777778
    """
    Kelvin = ((degrees + 459.67) * 5 / 9)
    return Kelvin

def convertKelvinToCelsius(degrees):
    """This function converts from Kelvin to Celsius.
    Args:
        degrees (float)
    Returns:
        A temperature value in Celsius.
    Examples:
    >>> convertKelvinToCelsius(527)
    253.85000000000002
    """
    Celsius = degrees - 273.15
    return Celsius


def convertKelvinToFahrenheit(degrees):
    """This function converts from Kelvin to Fahrenheit.
    Args:
        degrees (float)
    Returns:
        A temperature value in Fahrenheit.
    Examples:
    >>> convertKelvinToFahrenheit(900)
    1160.3300000000002
    """
    Fahrenheit_A = convertKelvinToCelsius(degrees)
    Fahrenheit = convertCelsiusToFahrenheit(Fahrenheit_A)
    return Fahrenheit

