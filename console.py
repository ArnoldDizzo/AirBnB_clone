#!/usr/bin/python3
"""command line interpreter to test my work"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models import storage


class HBNBCommand(cmd.Cmd):
    """created the class to use for cmd"""

    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "Amenity": Amenity,
        "Place": Place,
        "User": User,
        "State": State,
        "Review": Review,
        "City": City
    }

    def do_quit(self, line):
        """quit commmand - used to quit the console"""
        return True

    def do_EOF(self, line):
        """EOF command - quits console with ctrl + d"""
        return True

    def emptyline(self):
        """command for an empty line"""
        pass

    def do_create(self, line):
        """creates a new class instance of basemodel"""
        line.split(" ")
        if len(line) == 0:
            print("** class name missing **")

        elif line not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        else:
            insta = HBNBCommand.classes[line]()
            insta.save()
            print(insta.id)

    def do_show(self, line):
        """Show the string representation of an instance of a class created"""
        k = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")

        elif k[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(k) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(k[0], k[1]) not in storage.all().keys():
            print("** no instance found **")

        else:
            g = storage.all()["{}.{}".format(k[0], k[1])]
            print(g)

    def do_destroy(self, line):
        """Destroys the Instance of a class created"""
        k = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")

        elif k[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(k) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(k[0], k[1]) not in storage.all().keys():
            print("** no instance found **")

        else:
            del(storage.all()["{}.{}".format(k[0], k[1])])
            storage.save()

    def do_all(self, line):
        """Show all instances of classes created by class or not"""
        k = line.split(" ")
        objs = storage.all()
        lists = []
        if len(line) == 0:
            for key, val in objs.items():
                lists.append(val.__str__())
        elif k[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        else:
            for key, val in objs.items():
                j = key.split(".")
                if k[0] == j[0]:
                    lists.append(val.__str__())
        print(lists)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
