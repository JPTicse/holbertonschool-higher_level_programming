#!/usr/bin/python3
""" Module that contains class Base """


import json


class Base:
    """ Class Base """
    __nbobjects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nbobjects += 1

            self.id = Base.__nbobjects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list to JSON string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
