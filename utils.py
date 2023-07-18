"""
"""
from models import storage


def validate_input(arg) -> bool:
    """
    Validate input for valid model name and its existance
    """
    arg = arg.split()

    if len(arg) < 1:
        print("** class name missing **")
        return False
    return True

def validate_class(class_name, models={}) -> bool:
    """
    Return true if class exist
    """
    for key in models:
        if class_name == key:
            return True

    print("*** class doesn't exist **")
    return False
    
def validate_obj(arg, model) -> bool | str:
    """
    Validates input `id` and return string
    combination of model name and id in the
    format `Model.Id`
    """
    arg = arg.split()
    if len(arg) < 2:
        print("** instance id missing **")
        return False
    
    model_key = arg[0]
    instance_id = arg[1]
    model_name = model[model_key]().__class__.__name__
    return "{}.{}".format(model_name, instance_id)

def get_all_obj(models={}, model_name=None) -> list:
    data = []
    storage.reload()
    try:
        model_objects = storage.objects
        obj_str
        if not model_name:
            for model in models:
                for obj in model_objects:
                    obj_str = model(**obj)
        if not not model_name:
            obj_str = model_name(**obj)
        data.append(obj_str.__str__())
    except KeyError as err:
        pass
    finally:
        return data