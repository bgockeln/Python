import os
import time

def list_recently_modified_files(dir1, dir2, time_threshold_days=1):
    # Convert the time threshold from days to seconds
    time_threshold_seconds = time_threshold_days * 86400

    # Get the current time
    current_time = time.time()

    recently_modified = []

    def check_recent_modifications(dir_path, other_dir_path):
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                other_file_path = os.path.join(other_dir_path, os.path.relpath(file_path, dir_path))

                if os.path.exists(other_file_path):
                    mod_time = os.path.getmtime(file_path)
                    other_mod_time = os.path.getmtime(other_file_path)

                    # Check if either file has been modified within the threshold
                    if (current_time - mod_time <= time_threshold_seconds or
                        current_time - other_mod_time <= time_threshold_seconds):
                        recently_modified.append((file_path, mod_time, other_mod_time))
                else:
                    mod_time = os.path.getmtime(file_path)
                    if current_time - mod_time <= time_threshold_seconds:
                        recently_modified.append((file_path, mod_time, None))

    # Check both directories
    check_recent_modifications(dir1, dir2)
    check_recent_modifications(dir2, dir1)

    # Print the recently modified files
    print(f"Files modified within the last {time_threshold_days} days in {dir1} and {dir2}:")
    for file_path, mod_time, other_mod_time in recently_modified:
        print(f"File: {file_path}")
        print(f"    Modified: {time.ctime(mod_time)}")
        if other_mod_time:
            print(f"    Corresponding file in the other directory: {time.ctime(other_mod_time)}")
        else:
            print("    No corresponding file in the other directory")

if __name__ == "__main__":
    dir1 = input("Enter the first directory path: ")
    dir2 = input("Enter the second directory path: ")
    days = int(input("Enter the number of days to consider for recent modifications: "))

    if os.path.isdir(dir1) and os.path.isdir(dir2):
        list_recently_modified_files(dir1, dir2, days)
    else:
        print("One or both of the provided paths are not valid directories.")