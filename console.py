#!/usr/bin/python3
"""
Module for command-line interface or interpreter
for Airbnb console
"""
import json
from cmd import Cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from utils import validate_input, validate_class, validate_id
from utils import validate_obj, get_all_obj, tokenize_arg


class HBNBCommand(Cmd):
    """
    class for Airbnb command-line interface or interpreter
    `The Airbnb console`
    """
    prompt = "(hbnb) "
    models = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review,
            }

    def do_quit(self, arg: str) -> None:
        """
        do_quit() -> None:
            Quits program from command interpreter session
        """
        exit()

    def do_EOF(self, arg: str) -> None:
        """
        do_EOF -> None:
            Quits program from command interpreter session
        """
        print("")
        return True

    def emptyline(self) -> None:
        """
        `emptyline():`
            Returns nothing to prevent last command execution
        """
        return

    def do_help(self, arg: str) -> bool | None:
        """
        `arg` -> str:
                Prints show infomation on commands
        """
        return super().do_help(arg)

    def do_create(self, arg: str) -> None:
        """
        Creates object instance and save to file
        in JSON format
        """
        check_input = validate_input(arg)
        if not check_input:
            return

        check_class = validate_class(arg, self.models)
        if not check_class:
            return

        arg = tokenize_arg(arg)
        model_key = arg[0]
        new_object = self.models[model_key]()
        new_object.save()
        print(new_object.id)

    def do_show(self, arg: str) -> None:
        """
        Prints an object string representation
        base on id from `arg`
        """
        check_input = validate_input(arg)
        if not check_input:
            return

        check_class = validate_class(arg, self.models)
        if not check_class:
            return

        check_id = validate_id(arg)
        if not check_id:
            return

        instance_objects = validate_obj(arg, self.models)
        storage.reload()
        try:
            model_object = storage.all[instance_objects]
            model_key = instance_objects.split(".")[0]
            model_object = self.models[model_key](**model_object)
            print(model_object.__str__())
        except KeyError as err:
            print("** no instance found **")

    def do_destroy(self, arg: str) -> None:
        """
        Deletes an object base on id from `arg`
        and update storage
        """
        check_input = validate_input(arg)
        if not check_input:
            return

        check_class = validate_class(arg, self.models)
        if not check_class:
            return

        check_id = validate_id(arg)
        if not check_id:
            return

        instance_objects = validate_obj(arg, self.models)
        storage.reload()
        try:
            model_objects = storage.all
            del model_objects[instance_objects]
            storage.all = model_objects
            storage.save()
        except KeyError as err:
            print("** no instance found **")

    def do_all(self, arg: str) -> None:
        """
        Prints string representation of all objects
        """
        if len(arg.split()) < 1:
            data = get_all_obj(self.models)
            print(data)
            return

        check_class = validate_class(arg, self.models)
        if not check_class:
            return

        arg = tokenize_arg(arg)
        data = get_all_obj({}, self.models[arg[0]])
        print(data)
        return

    def do_update(self, arg: str) -> None:
        """
        Updates object based on id passed in `arg`
        """
        check_input = validate_input(arg)
        if not check_input:
            return

        check_class = validate_class(arg, self.models)
        if not check_class:
            return

        check_id = validate_id(arg)
        if not check_id:
            return

        arg_dup = arg
        arg = tokenize_arg(arg)

        if len(arg) < 3:
            print("** attribute name missing **")
            return

        # check if input arguments are in pairs
        if len(arg) < 4:
            print("** value missing **")
            return

        storage.reload()
        model_objects = storage.all
        obj_key = validate_obj(arg_dup, self.models)
        try:
            obj_data = model_objects[obj_key]
            obj_data[arg[2]] = arg[3]
            new_obj = self.models[arg[0]](**obj_data)
            storage.new(new_obj)
            new_obj.save()
        except KeyError as err:
            print("** no instance found **")

if __name__ == "__main__":
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt as err:
        print()
        exit()