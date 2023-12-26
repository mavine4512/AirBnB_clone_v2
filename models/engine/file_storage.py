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

    def all(self, cls=None):
        """A function that returns all dictionary __objects"""
        if cls is None:
            return self.__objects
        elif type(cls):
            return {k: v for k, v in self.__objects.items()
                    if v.__class__.__name__ == cls}
        else:
            return {k: v for k, v in self.__objects.items()
                    if v.__class__.__name__ == cls}

    def new(self, obj):
        """Creates a new key for the object"""
        self.__objects.update(
                {obj.to_dict()['__class'] + '.' + obj.id: obj}
                )

    def save(self):
        """A function that saves objects dictionary to JSON file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        A function that Reloads objects dictionary from the JSON file
        """

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review,
        }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
            for key, val in temp.items():
                self.all[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass


def delete(self, obj=None):
    '''Delete the object obj from the attributes
        __objects if its inside it
    '''
    if obj is None:
        return
    obj_key = obj.to_dict()['__class__'] + '.' + obj.id
    if obj_key in self.__objects.keys():
        del self.__objects[obj_key]


def close(self):
    """Call the reload method"""
    self.reload()
