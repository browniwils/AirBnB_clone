"""
Module contains utility or helper functions
"""
from datetime import datetime


def tokenize_arg(arg: str) -> list:
    """
    Returns tokenized string to list
    """
    arg = arg.split()
    tokens = []
    token = ""

    for item in arg:
        if item[0] == "\"" and item[-1] == "\"":
            tokens.append(item[1:-1])
        if item[0] == "'" and item[-1] == "'":
            tokens.append(item[1:-1])
        elif item[0] == "\"" or item[0] == "'":
            token = item[1:]
            continue
        elif item[-1] == "\"" or item[-1] == "'":
            token += " {}".format(item[:-1])
            tokens.append(token)
            token = ""
        else:
            tokens.append(item)

    return tokens


def validate_input(arg: str) -> bool:
    """
    Validate input for valid model name and its existance
    """
    arg = tokenize_arg(arg)
    if len(arg) < 1:
        print("** class name missing **")
        return False
    return True


def validate_class(arg: str, models={}) -> bool:
    """
    Return true if class exist
    """
    arg = tokenize_arg(arg)
    class_name = arg[0]
    for key in models:
        if class_name == key:
            return True

    print("*** class doesn't exist **")
    return False


def validate_id(arg: str) -> bool:
    """
    Validates input `id`
    """
    arg = tokenize_arg(arg)
    if len(arg) < 2:
        print("** instance id missing **")
        return False
    return True


def validate_obj(arg: str, model: dict) -> str:
    """
    Validates input `id` and return string
    combination of model name and id in the
    format `Model.Id`
    """
    arg = tokenize_arg(arg)
    model_key = arg[0]
    instance_id = arg[1]
    model_name = model[model_key]().__class__.__name__
    return "{}.{}".format(model_name, instance_id)


def get_all_obj(models={}, model_name=None) -> list:
    """
    Retrieve objects and returns it as string
    representation in a list
    """
    from models import storage
    data = []
    storage.reload()
    try:
        model_objects = storage.all()
        model_objects_keys = list(model_objects.keys())
        if not model_name:
            for model in models:
                for obj_item in model_objects_keys:
                    obj = model_objects[obj_item]
                    if obj["__class__"] == model:
                        obj_str = models[model](**obj)
                        data.append(obj_str.__str__())
        if not not model_name:
            for obj_item in model_objects_keys:
                obj = model_objects[obj_item]
                if obj["__class__"] == model_name().__class__.__name__:
                    obj_str = model_name(**obj)
                    data.append(obj_str.__str__())
    except KeyError as err:
        pass
    finally:
        return data


def prep_save_to_file(objects, direction="start") -> None:
    """
    Prepares storage objects for saving
    """
    for obj_key, obj_val in objects.items():
        for key, val in obj_val.items():
            if direction == "start":
                if type(val) == datetime:
                    objects[obj_key][key] = val.isoformat()
            if direction == "end":
                if key == "created_at" or key == "updated_at":
                    objects[obj_key][key] = datetime.fromisoformat(val)
