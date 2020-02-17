#!/usr/bin/python3
""" import cmd module, BaseModel and storage """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    def do_create(self, arg):
        """Creates a new instance of BaseModel and prints the id. Example:\n(hbnb) create BaseModel\n """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(getattr(obj, 'id'))
        else:
            print("** class doesn't exist **")
    
    def do_show(self, arg=""):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] == "BaseModel":
            if len(args) == 2:
                name_id = "BaseModel." + str(args[1])
                objs = storage.all()
                if name_id in objs.keys():
                    print(BaseModel(objs[name_id]))
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **") 


    def do_quit(self, arg):
        """Quit command to exit the program \n"""
        raise SystemExit

    def do_EOF(self, arg):
        """ EOF SystemExiit """
        raise SystemExit


if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb)'
    prompt.cmdloop('Starting prompt...')