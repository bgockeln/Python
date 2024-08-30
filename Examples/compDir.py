import os
import filecmp

def compare_directories(dir1, dir2):
    # Compare the directories using filecmp.dircmp
    comparison = filecmp.dircmp(dir1, dir2)

    # Report the differences
    print(f"Comparing {dir1} and {dir2}")
    if comparison.left_only:
        print("Files only in", dir1, ":", comparison.left_only)
    if comparison.right_only:
        print("Files only in", dir2, ":", comparison.right_only)
    if comparison.diff_files:
        print("Differing files:", comparison.diff_files)
    if comparison.funny_files:
        print("Trouble with files:", comparison.funny_files)

    # Recursively compare subdirectories
    for sub_dir in comparison.common_dirs:
        compare_directories(os.path.join(dir1, sub_dir), os.path.join(dir2, sub_dir))

if __name__ == "__main__":
    dir1 = input("Enter the first directory path: ")
    dir2 = input("Enter the second directory path: ")

    if os.path.isdir(dir1) and os.path.isdir(dir2):
        compare_directories(dir1, dir2)
    else:
        print("One or both of the provided paths are not valid directories.")