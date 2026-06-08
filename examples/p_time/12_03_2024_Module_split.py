import importlib
import inspect

# Prompt the user to input the name of the module
module_name = input("Enter the name of the module: ")

try:
    # Import the module dynamically
    module = importlib.import_module(module_name)

    # Get all members (variables, functions, classes) of the module
    members = inspect.getmembers(module)
    print(type(members))

    # Separate members into variables, functions, and classes
    variables = [member for member in members if not inspect.isfunction(member[1]) and not inspect.isclass(member[1])]
    functions = [member for member in members if inspect.isfunction(member[1])]
    classes = [member for member in members if inspect.isclass(member[1])]

    # Print the results
    print("\nVariables:")
    for var in variables:
        print(var[0])

    print("\nFunctions:")
    for func in functions:
        print(func[0])

    print("\nClasses:")
    for cls in classes:
        print(cls[0])

except ImportError:
    print("Module '{}' not found.".format(module_name))
