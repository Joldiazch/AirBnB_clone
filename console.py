#!/usr/bin/python3
""" import cmd module, BaseModel and storage """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage
import sys

list_classes = ["BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Review",
                "Place"]


class HBNBCommand(cmd.Cmd):
    def do_update(self, arg):
        objs = storage.all()
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] in list_classes:
            if len(args) < 2:
                print("** instance id missing **")
            elif args[1] in [name_id.split(".")[1] for name_id in objs.keys()]:
                name_id = args[0] + "." + args[1]
                obj = objs[name_id]
                if len(args) < 3:
                    print("** attribute name missing **")
                else:
                    if len(args) < 4:
                        print("** value missing **")
                    else:
                        setattr(obj, args[2], args[3].strip('"'))
                        storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation
        of all instances based or not on the class name."""
        objs = storage.all()
        args = arg.split(" ")
        list_out = []
        if len(arg) == 0:
            for obj in objs.values():
                list_out.append(str(obj))
            print(list_out)
        elif args[0] in list_classes:
            for name_id in objs.keys():
                if name_id.split(".")[0] == args[0]:
                    list_out.append(str(objs[name_id]))
            print(list_out)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] in list_classes:
            if len(args) == 2:
                name_id = args[0] + "." + str(args[1])
                objs = storage.all()
                if name_id in objs.keys():
                    del(objs[name_id])
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        and prints the id. Example:\n(hbnb) create BaseModel\n """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] in list_classes:
            obj = eval(args[0] + "()")
            id = getattr(obj, 'id')
            storage.save()
            print(id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg=""):
        """Prints the string representation
        of an instance based on the class name and id"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] in ["BaseModel", "User"]:
            if len(args) >= 2:
                name_id = args[0] + "." + str(args[1])
                objs = storage.all()
                if name_id in objs.keys():
                    obj = objs[name_id]
                    print(obj)
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit command to exit the program \n"""
        storage.all().clear()
        sys.exit(1)

    def do_EOF(self, arg):
        """ EOF SystemExiit """
        print("")
        return True


if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop('Starting prompt...')
