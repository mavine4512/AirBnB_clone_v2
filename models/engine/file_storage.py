#!/usr/bin/python3
"""
This is a class FileStorage module
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This is the File path to store data"""

    __file_path = 'file.json'
    """A function dict to store objects in a file"""
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """A function that returns all dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Creates a new key for the object"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """A function that saves objects dictionary to JSON file"""
        my_dict = {}
        for key, obj in self.__objects.items():
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        A function that Reloads objects dictionary from the JSON file
        """
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
