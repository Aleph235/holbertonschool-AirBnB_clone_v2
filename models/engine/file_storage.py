#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import models
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from os import path

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            keyo = {}
            for key, val in FileStorage.__objects.items():
                if type(val) == cls:
                    keyo[key] = val
            return keyo

        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)


    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as AJ:
                dictionary = json.loads(AJ.read())
                for key, value in dictionary.items():
                    self.__objects[key] = eval(value['__class__'])(**value)

    def delete(self, obj=None):
        """Adding a new public instance method
        and delete obj from __objects if it’s inside
        """
        if obj is not None:
            if obj in FileStorage.__objects.values():
                keyo = "{}.{}".format(type(obj).__name__, obj.id)
                del FileStorage.__objects[keyo]

    def close(self):
        """method for deserializing the JSON
        file to objects
        """
        models.storage.reload()