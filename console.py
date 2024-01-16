#!/usr/bin/python3
"""defines a command line interpreter"""
import cmd
import models.base_model
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """a class that inherits from the Cmd class"""

    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place"
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """ a method that exits the command line interpreter
        """

        return True

    def do_EOF(self, arg):
        """ a EOF method that exits the command interpreter
        """

        print("")
        return True

    def emptyline(self):
        """ method called when an empty line is
        entered in response to the prompt
        """
        pass

    def do_create(self, arg):
        """ creates a new instance of a class,
        saves it and prints the id
        """

        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            print(eval(arg)().id)
            strorage.save()

    def do_show(self, arg):
        """ prints the string representation of an instance
        based on the class name and id
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            class_obj = args[0]
            class_id = args[1]
            key = "{}.{}".format(class_obj, class_id)
            if key not in storage.all():
                print("** no instance found **")
                return
            instance = storage.all()[key]
            print(instance)

    def do_destroy(self, arg):
        """ deletes an instance based on the class name and id
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            class_obj = args[0]
            class_id = args[1]
            key = "{}.{}".format(class_obj, class_id)
            if key not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """ prints all string representation of all instances
        based or not on the same class name
        """

        if not arg:
            insts = storage.all().values()
        else:
            if arg not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            insts = [inst for inst in storage.all().values()
                     if inst.__class__.__name__ == arg]
        print([str(inst) for inst in insts])

    def do_update(self, arg):
        """ updates an instance based on the class name
        and id by adding or updating attribute
        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_obj = args[0]
        class_id = args[1]
        key = "{}.{}".format(class_obj, class_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) == 3:
            print("** value missing **")
            return
        attr_value_str = args[3]
        if len(args) == 4:
            inst = storage.all()[key]
            attr_type = type(getattr(inst, attr_name))
            attr_value = attr_type(attr_value_str)
            setattr(inst, attr_name, attr_value)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
