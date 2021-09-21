#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    return (a+b+c)/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return math.radians(angle_degs + angle_mins/60 + angle_secs/3600)


def to_degrees(angle_rads: float) -> tuple:

    degrees = int(angle_rads*180/math.pi)
    deg_remainder = angle_rads*180/math.pi - int(angle_rads*180/math.pi)
    full_minutes = deg_remainder*60
    minutes = int(full_minutes)
    min_remainder = full_minutes - int(deg_remainder*60)
    seconds = int(min_remainder*60) # Not sure if they want int here

    return int(degrees), int(minutes), int(seconds)

    # degrees = angle_rads*180/3.14159 - (angle_rads * 180) % 3.14159
    # minutes = (angle_rads*180%3.14159)*60 - (angle_rads)
    # seconds = (angle_rads*180%3.14159)*60 - (angle_rads)
    # return int(degrees), int(minutes), int(seconds)

# Solution alternative: Utiliser divmod sous la forme
#    minutes, degrees = divmod((angle_rads*180/3.14159), 60)
#    print(divmod((angle_rads*180/3.14159), 60))
#    minutes *= 60
#    seconds, minutes = divmod(minutes, 60)

#    return int(degrees), int(minutes), int(seconds)

def to_celsius(temperature: float) -> float:
    return (temperature-32)*(5/9)


def to_farenheit(temperature: float) -> float:
    return temperature*(9/5) + 32


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
