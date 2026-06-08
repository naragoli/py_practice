import inspect
import importlib

module_name = input('Enter the module name to review:')
class_info, variable_info, function_info = [],[],[]
try:
    module = importlib.import_module(module_name)



    
    module_members = inspect.getmembers(module)

    for member in module_members:
        if inspect.isclass(member[1]):
            class_info.append(member)
        elif inspect.isfunction(member[1]):
            function_info.append(member)
        else:
            variable_info.append(member)
    #print(class_info[0], function_info[0], variable_info[0], sep='\n')
    if class_info:
        print("Classes:")
        for cls in class_info:
            print(cls[0])
    else:
        print("No classes found.")

    if function_info:
        print("\nFunctions:")
        for func in function_info:
            print(func[0])
    else:
        print("No functions found.")

    if variable_info:
        print("\nVariables:")
        for var in variable_info:
            print(var[0])
    else:
        print("No variables found.")

except ImportError:
    print("Module '{}' not found".format(module_name))

