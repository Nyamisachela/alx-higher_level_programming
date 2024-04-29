#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    Represents a Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initilaization of a new rectangle
        Args:
            width (must be an int): The width of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """access current size of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the actual width of the Recatngle"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """sets the actual height of the Rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the actual height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Function that calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Function that calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def my_print(self):
        '''This method prints the rectangle using the #'''
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print("")

    def __str__(self):
        '''Prints a  representaion of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            result += "\n"
        return result.rstrip("\n")
