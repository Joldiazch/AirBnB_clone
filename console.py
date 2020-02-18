#!/usr/bin/python3
""" import cmd module, BaseModel and storage """
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import sys

class HBNBCommand(cmd.Cmd):
    def do_update(self, arg):
        objs = storage.all()
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] == "BaseModel":
            if len(args) < 2:
                print("** instance id missing **")
            elif args[1] in [name_id.split(".")[1] for name_id in objs.keys()]:
                name_id = "BaseModel." + args[1]
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
        """Prints all string representation of all instances based or not on the class name."""
        objs = storage.all()
        args = arg.split(" ")
        list_out = []
        if len(arg) == 0:
            for obj in objs.values():
                list_out.append(str(obj))
            print(list_out)
        elif args[0] == "BaseModel":
            for name_id in objs.keys():
                if name_id.split(".")[0] == "BaseModel":
                    list_out.append(str(objs[name_id]))
            print(list_out)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] == "BaseModel":
            if len(args) == 2:
                name_id = "BaseModel." + str(args[1])
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
        """Creates a new instance of BaseModel and prints the id. Example:\n(hbnb) create BaseModel\n """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in ["BaseModel", "User"]:
            if (arg == "BaseModel"):
                obj = BaseModel()
                storage.save()
                print(getattr(obj, 'id'))
            elif (arg == "User"):
                obj = User()
                storage.save()
                print(getattr(obj, 'id'))
        else:
            print("** class doesn't exist **")

    def do_show(self, arg=""):
        """Prints the string representation of an instance based on the class name and id"""
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
        raise SystemExit


if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb)'
    prompt.cmdloop('Starting prompt...')