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
        """ Save object in a file """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

            lists = cls.to_json_string(list_dic)

            with open(filename, 'w') as f:
                f.write(lists)
