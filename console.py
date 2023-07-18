#!/usr/bin/python3
"""

"""
import json
from cmd import Cmd
from models import storage
from models.base_model import BaseModel
from utils import validate_input, validate_class
from utils import validate_obj, get_all_obj


class HBNBCommand(Cmd):
    """
    
    """
    prompt = "(hbnb) "
    models = { "BaseModel": BaseModel }

    def do_quit(self, arg) -> None:
        """
        do_quit() -> None:
            Quits program from command interpreter session
        """
        exit()

    def do_EOF(self, arg) -> None:
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
        check_input = validate_input(arg, self.models)
        if not check_input:
            return

        check_class = validate_class(arg, self.models)
        if not check_class:
            return

        arg = arg.split()
        model_key = arg[0]
        new_object = self.models[model_key]()
        new_object.save()
        print(new_object.id)

    def do_show(self, arg: str) -> None:
        """
        Prints an object string representation
        base on id from `arg`
        """
        check_input = validate_input(arg, self.models)
        if not check_input:
            return

        arg = arg.split()
        check_class = validate_class(arg[0], self.models)
        if not check_class:
            return

        instance_objects = validate_obj(arg, self.models)
        if not instance_objects:
            return

        storage.reload()
        try:
            model_object = storage.get_objects[instance_objects]
            model_key = model_object.split(".")[0]
            model_object = self.models[model_key](**model_object)
            print(model_object.__str__())
        except KeyError as err:
            print("** no instance found **")

    def do_destroy(self, arg) -> None:
        """
        Deletes an object base on id from `arg`
        and update storage
        """
        check_input = validate_input(arg, self.models)
        if not check_input:
            return

        arg = arg.split()
        check_class = validate_class(arg[0], self.models)
        if not check_class:
            return

        instance_objects = validate_obj(arg, self.models)
        if not instance_objects:
            return

        storage.reload()
        try:
            model_objects = storage.objects
            del model_objects[instance_objects]
            storage.objects(model_objects).save()
        except KeyError as err:
            print("** no instance found **")

    def do_all(self, arg) -> None:
        """
        Prints string representation of all objects
        """
        arg = arg.split()
        if len(arg) < 1:
            data = get_all_obj(self.models)
            print(data)
            return

        check_class = validate_class(arg[0], self.models)
        if not check_class:
            return

        data = get_all_obj({}, self.models[arg[0]])
        print(data)
        return



if __name__ == "__main__":
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt as err:
        print()
        exit()