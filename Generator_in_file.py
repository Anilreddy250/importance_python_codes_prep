import time
def read_large_file(file_path):
    #A generator function to read a file line - by line
    try : 
        with open(file_path, "r", encoding = "utf=8") as file :
            for line in file :
                yield line.strip()
                time.sleep(1)
    except FileNotFoundError:
        print("The file was not found")
#usage
file_gen = read_large_file('/home/mirafra/sys.txt')

for line in file_gen:
    print(f"processing:{line}")
    