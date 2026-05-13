def process_large_file(file_path):
    word_count = 0
    try:
        with open(file_path, 'r', encoding='utf=8') as file :
            for line in file:
                words = line.split()
                word_count +=len(words)

        print(f"processing complete.")
        print(f"Total estimated words: {word_count:,}")
    except FileExistsError:
        print(f"Error: the file was not found please check the path")

    except Exception as e :
        print(f"An unexpected error occured:{e}")

if __name__ == "__main__":
    process_large_file("/home/mirafra/sys.txt")

