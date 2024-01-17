import os
from time import time

def remove_directories(directory_list):
    for directory in directory_list:
        try:
            os.rmdir(directory)
            print(f"Removed directory: {directory}")
        except OSError as e:
            print(f"Error removing directory {directory}: {e}")

def main():
    file_path = "arz_names.txt"

    with open(file_path, 'r') as file:
        directories = file.read().split(',')

    batch_size = 10000
    total_directories = len(directories)

    for i in range(0, total_directories, batch_size):
        batch = directories[i:i + batch_size]
        remove_directories(batch)

if __name__ == "__main__":
    start_time = time()
    main()
    end_time = time()
    print(f"{round(end_time-start_time,2)} Seconds.")
