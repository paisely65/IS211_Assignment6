import unittest
from conversions import *


class CelsiusTestCase(unittest.TestCase):
    """Tests for celsius for `conversions.py`."""

    def test_celsius_to_kelvin(self):
        """Is conversion succssful?"""
        self.assertTrue(373.15 == round(convertCelsiusToKelvin(100), 2))
        self.assertTrue(273.15 == round(convertCelsiusToKelvin(0), 2))
        self.assertTrue(173.15 == round(convertCelsiusToKelvin(-100), 2))
        self.assertTrue(328.15 == round(convertCelsiusToKelvin(55), 2))
        self.assertTrue(0 == round(convertCelsiusToKelvin(-273.15), 2))

    def test_celsius_to_fahrenheit(self):
        """Is conversion succssful"""
        self.assertTrue(32 == round(convertCelsiusToFahrenheit(0), 2))
        self.assertTrue(212 == round(convertCelsiusToFahrenheit(100),2))
        self.assertTrue(149 == round(convertCelsiusToFahrenheit(65),2))
        self.assertTrue(-25.6 == round(convertCelsiusToFahrenheit(-32),2))
        self.assertTrue(-459.67 == round(convertCelsiusToFahrenheit(-273.15),2))


class FahrenheitTestCase(unittest.TestCase):
    """Tests for fahrenheit for `conversions.py`."""

    def test_fahrenheit_to_kelvin(self):
        """Is conversion succssful"""
        self.assertTrue(310.93 == round(convertFahrenheitToKelvin(100), 2))
        self.assertTrue(273.15 == round(convertFahrenheitToKelvin(32), 2))
        self.assertTrue(290.93 == round(convertFahrenheitToKelvin(64), 2))
        self.assertTrue(255.37 == round(convertFahrenheitToKelvin(0), 2))
        self.assertTrue(235.93== round(convertFahrenheitToKelvin(-35), 2))

    def test_fahrenheit_to_celcius(self):
        """Is conversion succssful"""
        self.assertTrue(-3.89 == round(convertFahrenheitToCelsius(25), 2))
        self.assertTrue(30.56 == round(convertFahrenheitToCelsius(87), 2))
        self.assertTrue(38.89 == round(convertFahrenheitToCelsius(102), 2))
        self.assertTrue(-17.78 == round(convertFahrenheitToCelsius(0), 2))
        self.assertTrue(-45.56 == round(convertFahrenheitToCelsius(-50), 2))
        

class KelvinTestCase(unittest.TestCase):
    """Tests for kelvin for `conversions.py`."""

    def test_kelvin_to_fahrenheit(self):
        """Is conversion succssful"""
        self.assertTrue(80.33 == round(convertKelvinToFahrenheit(300), 2))
        self.assertTrue(-459.67 == round(convertKelvinToFahrenheit(0), 2))
        self.assertTrue(-369.67 == round(convertKelvinToFahrenheit(50), 2))
        self.assertTrue(-279.67 == round(convertKelvinToFahrenheit(100), 2))
        self.assertTrue(-999.67 == round(convertKelvinToFahrenheit(-300), 2))

    def test_kelvin_to_celsius(self):
        """Is conversion succssful"""
        self.assertTrue(-153.15 == round(convertKelvinToCelsius(120), 2))
        self.assertTrue(-273.15 == round(convertKelvinToCelsius(0), 2))
        self.assertTrue(325.85 == round(convertKelvinToCelsius(599), 2))
        self.assertTrue(-173.15 == round(convertKelvinToCelsius(100), 2))
        self.assertTrue(406.85== round(convertKelvinToCelsius(680), 2))


        
        
if __name__ == '__main__':
    unittest.main()
