#!user/bin/env python
# -*- coding: utf-8 -*-
"""This module simplifies the process of unit conversions."""

def convert(fromUnit, toUnit, value): 
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    value = float(value)
    if fromUnit == toUnit:
        value = value
        return value

    if fromUnit == 'celsius':
        if toUnit == 'kelvin':
            value = value + 273.15
            return round(value, 2)

        elif toUnit == 'fahrenheit':
            value = ((value * 1.8) + 32)
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter valid units. \
                                        You entered from {} to {}'.format(fromUnit, toUnit))
    if fromUnit == 'fahrenheit':
        if toUnit == 'celsius':
            value = ((value - 32) * 5 / 9)
            return round(value, 2)
        elif toUnit == 'kelvin':
            value = (value + 459.67) * 5/9
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units. \
                                        You entered from {} to {}'.format(fromUnit, toUnit))
    if fromUnit == 'kelvin':
        if toUnit == 'celsius':
            value = value - 273.15
            return round(value, 2)
        elif toUnit == 'fahrenheit':
            value = (value * 9/5 ) - 459.67
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units. \
                                        You entered from {} to {}'.format(fromUnit, toUnit))
                                        
    if fromUnit == 'miles':
        if toUnit == 'yards':
            value = value * 1760.0
            return round(value, 2)
        elif toUnit == 'meters':
            value = value * 1604.344
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units. \
                                        You entered from {} to {}'.format(fromUnit, toUnit))
                                        
    if fromUnit == 'yards':
        if toUnit == 'meters':
            value = value * 0.9144
            return round(value, 2)
        elif toUnit == 'miles':
            value = value / 1760.0
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units. \
                                        You entered from {} to {}'.format(fromUnit, toUnit))
                                       
    if fromUnit == 'meters':
        if toUnit == 'miles':
            value = value * 0.000621
            return round(value, 2)
        elif toUnit == 'yards':
            value = value * 1.0936
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units. \
                                        You entered from {} to {}'.format(fromUnit, toUnit))

                                        
print convert('fahrenheit','kelvin', 105)
print convert('fahrenheit','celsius', 105)
print convert('celsius','kelvin', 105)
print convert('celsius', 'fahrenheit', 105)
print convert('kelvin', 'celsius', 105)
print convert('kelvin','fahrenheit', 105)

print convert('fahrenheit','fahrenheit', 105)

print convert('miles','yards', 105)
print convert('miles','meters', 105)
print convert('yards','meters', 105)
print convert('yards','miles', 105)
print convert('meters','miles', 105)
print convert('meters','yards', 105)


