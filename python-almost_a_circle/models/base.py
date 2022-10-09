#!/usr/bin/python3
""" Module that contains class Base """


from fileinput import filename
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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file"""
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Square":
            list_keys = ['id', 'size', 'x', 'y']
        else:
            list_keys = ['id', 'width', 'height', 'x', 'y']
        
