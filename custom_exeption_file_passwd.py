class InsecureFileNameError(Exception):
    #exception raised when a filename contains sensitive keywords
    def __init__(self, filename, message = "Filenames containing 'password' are not permitted for security reasons."):
        self.filename =filename
        self.message = message
        super().__init__(self.message)
def save_file(filename, content):
    #normalize the string to lowercase to catch "Passwrod", "PASSWORD", etc.
    if "password" in filename.lower():
    # if "123456" in filename.lower():

        raise InsecureFileNameError(filename)
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"File'{filename}' saved successfully")
    
    except PermissionError:
        print("permission denied")
    except Exception as e:
        print(f"An error occured:{e}")
    
try:
    save_file("my_password_list.txt", "password")
except InsecureFileNameError as e:
    print(f"Security Alert: {e}")