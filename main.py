import os
import sys
# Now we import the actual functions from the files we made
from optimizer import find_duplicates
from recovery import recover_files


def main():
    print("=== File System Recovery & Optimization Tool ===")
    print("1. Optimize System (Find Duplicates)")
    print("2. Recover Lost Files")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        directory = input("Enter directory path to scan: ")
        if os.path.exists(directory):
            find_duplicates(directory)
        else:
            print("Error: Directory not found.")

    elif choice == '2':
        source = input("Enter source directory path: ")
        dest = input("Enter destination path for recovered files: ")
        if os.path.exists(source):
            recover_files(source, dest)
        else:
            print("Error: Source directory not found.")

    elif choice == '3':
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()