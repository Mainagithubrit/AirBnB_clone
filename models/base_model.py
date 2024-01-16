#!/usr/bin/python3
"""defines a class"""
from datetime import datetime
import uuid


class BaseModel:

    """a class called BaseModel"""
    def __init__(self, *args, **kwargs):

        """Initialises a new instance of a class

        Args:
        id(str): the unique id when an instance is created
        created_at(datetime): the current datetime when an instance is created
        updated_at(datetime): the current datetime when an instance is created
        and it will be updated every time you change your object


        *args: unused
        **Kwargs: Key and value attributes
        """
        now = datetime.now()
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())

            self.created_at = now
            self.updated_at = now
            storage.new(self)

    def __str__(self):
        """returns a string representation of the BaseModel"""

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """

        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()

        return inst_dict
