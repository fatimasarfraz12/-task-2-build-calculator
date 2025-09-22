import os   # Import the os module to interact with the operating system

def print_directory(path='/'):
    """
    Print the contents of a directory.
    Default path '.' means current working directory.
    """
    try:
        # Get a list of all files and folders in the given directory
        entries = os.listdir(path)

        print(f"Contents of '{path}':")
        # Loop through the list and print each item
        for entry in entries:
            print(entry)

    # Handle case where the directory is not found
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")

    # Handle case where the given path is not actually a directory
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")

    # Handle case where access is denied
    except PermissionError:
        print(f"Error: Permission denied accessing '{path}'.")

# Example usage:
print_directory()   # Prints contents of the current directory
# print_directory("C:/Users/YourName/Documents")   # You can give a custom path here
