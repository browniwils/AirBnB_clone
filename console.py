#!/usr/bin/python3
"""
Command-line interface or interpreter `Airbnb console`.
Used to interact with Airbnb project for debugging and testing
"""
import cmd, json
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


class HBNBCommand(cmd.Cmd):
    """
    Object for Airbnb command-line interface or interpreter.
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

    def do_quit(self, arg: str):
        """
        Exits interpreter session
        """
        exit()

    def do_EOF(self, arg: str):
        """
        Prints nothing
        """
        print("")
        return True

    def emptyline(self):
        """
        Immediately returns to prevent
        last command execution
        """
        return

    def do_help(self, arg: str):
        """
        Prints or show infomation on active
        commands
        """
        return super().do_help(arg)

    def do_create(self, arg: str):
        """
        Creates object instance base on model's name `arg`
        and save to file in JSON format
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

    def do_show(self, arg: str):
        """
        Shows an object string representation
        base on model and object's id from `arg`
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
            model_object = storage.all()[instance_objects]
            model_key = instance_objects.split(".")[0]
            model_object = self.models[model_key](**model_object)
            print(model_object.__str__())
        except KeyError as err:
            print("** no instance found **")

    def do_destroy(self, arg: str):
        """
        Deletes an object base on model name and id 
        from `arg` and update storage
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
            model_objects = storage.all()
            del model_objects[instance_objects]
            storage.save()
        except KeyError as err:
            print("** no instance found **")

    def do_all(self, arg: str):
        """
        Shows all objects string representation
        base on or not model name from `arg`
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

    def do_update(self, arg: str):
        """
        Update object based on id and model name from `arg`
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
        model_objects = storage.all()
        obj_key = validate_obj(arg_dup, self.models)
        try:
            obj_data = model_objects[obj_key]
            for i in range(2, len(arg), 2):
                obj_data[arg[i]] = arg[i+1]
            new_obj = self.models[arg[0]](**obj_data)
            storage.new(new_obj)
            new_obj.save()
        except KeyError as err:
            print("** no instance found **")

    def do_count(self, arg):
        """
        Counts number of objects base no model name
        """
        data = get_all_obj({}, self.models[arg[0]])
        print(len(data))

    def default(self, line: str):
        if "(" not in line or ")" not in line:
            print("** missing parentesis **")
            return

        line = line.split(".")
        arg_model = line[0]

        if arg_model not in self.models:
            print("*** unknown model **")
            return

        line = line[1].replace(")", "")
        line = line.split("(")

        cmd_method = line[0]
        if cmd_method == "count":
            self.do_count([arg_model])
            return

        if cmd_method == "all":
            self.do_all(arg_model)
            return

        data = line[1].split(", ", 1)
        id = data[0]

        if cmd_method == "show":
            self.do_show("{} {}".format(arg_model, id))
            return

        if cmd_method == "destroy":
            self.do_destroy("{} {}".format(arg_model, id))
            return

        if cmd_method == "update":
            attr = data[1]
            arg_str = "{} {}".format(arg_model, id)
            if "{" in attr and "}" in attr:
                attr = attr.replace("{", "").replace("}", "")
                attr = attr.replace(":", "").replace(",", "")
            else:
                attr = attr.replace(", ", " ")

            self.do_update("{} {}".format(arg_str, attr))
            return

        print("** unknown command **")
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
