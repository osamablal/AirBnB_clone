#!/usr/bin/python3
"""
HBNBComand - Tools For AIRBNB Console.
Usage: The Heart of the console.
"""

import cmd
import shlex
import re
import models
from json import loads, dumps
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from datetime import datetime


class HBNBComand(cmd.Cmd):
    """
        The Command Line Classing.
    """
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_create(self, args):
        """
           Creating New Base Model, saving the Basemodel and printing ID.
           Usage: Creating the classname.
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBComand.__classes:
            print("** class doesn't exist **")
        else:
            new_crtd = HBNBComand.__classes[args[0]]()
            models.storage.save()
            print(new_crtd.id)

    def do_show(self, args):
        """
           Printing string present of a specific instance
           Usage: show the classname and id.
        """
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBComand.__classes:
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key_value = strings[0] + '.' + strings[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
           Delete an instance
           Usage: destroy the classname and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            store_all = storage.all()
            for key, value in store_all.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """
           Printing string present for all the instances
           Usage: classname for all.
        """
        args = args.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(str(obj))
            print(new_list)
        elif args[0] not in HBNBComand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(str(obj))
            print(new_list)

    def do_update(self, args):
        """
           updating a specific instanc.
        """
        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBComand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """
        Checking user gived classname and id in stdin or not.
        """
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """
        Checking the class id.
        """
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """
        Finding name of the class.
        """
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBComand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                print("** class doesn't exist **")
                return None

    def do_count(self, cls_name):
        """counts number of instances of a class"""
        count = 0
        store_all = storage.all()
        for k, v in store_all.items():
            class_var = k.split('.')
            if class_var[0] == cls_name:
                count = count + 1
        print(count)

    def do_quit(self):
        """
        For Exiting app.
        """
        return True

    def do_EOF(self):
        """
        Handles the last of the file.
        """
        return True

    def emptyline(self):
        """
           if user at entering new emptyline don't execute anything.
        """


if __name__ == '__main__':
    HBNBComand().cmdloop()
