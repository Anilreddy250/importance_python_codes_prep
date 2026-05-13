def safe_open_file(file_path, mode ="r"):
    #attempts to open a file and handles common os related errors
    try:
        #the with statement ensures the file is properly closed after use
        with open(file_path, mode) as file:
            content = file.read()
            print("File opened successfully")
            return content
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: You do not have the required permissions to access '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None
# Example usage:
# data = safe_open_file("my_data.txt")