def secure_copy(source_path, dest_path):
    # 1. Check for insecure filenames before doing any work
    if "password" in dest_path.lower():
        raise InsecureFileNameError(dest_path)

    try:
        # 2. Open both files simultaneously 
        # The 'with' statement handles cleanup for both, regardless of failure
        with open(source_path, 'r') as src, open(dest_path, 'w') as dest:
            for line in src:
                # If an error happens here, both src and dest close automatically
                dest.write(line)
        
        print(f"Successfully copied {source_path} to {dest_path}")

    except FileNotFoundError:
        print(f"Source file '{source_path}' not found.")
    except PermissionError:
        print("Permission denied during copy process.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# secure_copy("source.txt", "backup_data.txt")