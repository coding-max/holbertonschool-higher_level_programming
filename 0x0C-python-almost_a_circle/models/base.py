#!/usr/bin/python3
"""module of 'Base' class"""

import json


class Base:
    """Representation of a Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        list_dict = []
        for i in list_objs:
            list_dict.append(i.to_dictionary())
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as jsonfile:
            jsonfile.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        new_inst = cls(1, 1)
        if new_inst is not None:
            new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(str(cls.__name__) + ".json", "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
