#!/usr/bin/python3
""" Module that contains class Base """


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
