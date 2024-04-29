#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    Represents a Rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initilaization of a new rectangle
        Args:
            width (must be an int): The width of the rectangle.
            height (must be an int): The height of the rectangle.
            number_of_instances: increments number of members of the
            rectangle class when one is created
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        '''prints the string representation of a rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            result += "\n"
        return result.rstrip("\n")

    def __repr__(self):
        '''returns the string representation of a rectangle'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''
        deletes the instance of a rectangle and
        reduces the number of instances by one'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
