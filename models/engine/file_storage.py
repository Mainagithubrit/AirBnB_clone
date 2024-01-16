#!/usr/bin/env python3

"""
Defines a program that handles the serialization and deserialization
of objects to and from a JSON file
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes and deserializes objects to and from a JSON file"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        """This gets the class name of the object"""
        class_name = obj.__class__.__name__

        """and then this generates the key using
        the class name and object id
        """
        key = f"{class_name}.{obj.id}"

        """this sets the object in __object with the generated key"""
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
value        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        """This writes the serialized data to the specified file"""
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        serialized_objects = {}

        """This checks if JSON file exists"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:

                """Loads the JSON data from the file"""
                serialized_objects = json.load(file)

        """Iterate through the serialized data and reconstruct"""
        for key, value in serialized_objects.items():
            self.__objects[key] = eval(value['__class__'])(**value)
