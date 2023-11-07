import os
import shutil


def main():
    source_path = ""
    destinate_path = ""
    # Input the souce directory and check if is valid or not
    # Check if the directory is correct.
    while True:
        source_path = input("From(please enter a valid directory): ")  # target directory
        if os.path.isdir(source_path):
            print("Valid directory!" + "\n")
            break
        else:
            print("Please check if the directory is correct!")

    # Input the destinate directory and check if is valid or not
    # Check if the directory is correct.
    while True:
        destinate_path = input("To(please enter a valid directory): ")
        os.path.isdir(destinate_path)
        if os.path.isdir(destinate_path):
            print("Valid directory!")
            break
        if not os.path.exists(destinate_path):
            pass
        else:
            print("Please check if the directory is correct!")

    # access the move_files_from_folder function to move the files inside the folder
    move_files_from_folder(source_path, destinate_path)


def move_files_from_folder(src_path: str, dest_path: str):
    folder_list = os.listdir(src_path)  # Scan folders in the source directory
    is_folder_list = []  # create a list to store the folder names

    # look for folders
    for item in folder_list:
        if os.path.isdir(src_path + "\\" + (item)):
            if (src_path + "\\" + item) == dest_path:
                # print(src_path + "\\" + item) # Debug
                continue
            else:
                is_folder_list.append(item)
                # print(is_folder_list) # Debug

    # for loop to look for files
    for item in is_folder_list:
        file_list = os.listdir(src_path + "\\" + str(item))
        # print(file_list)  # Debug

        # for loop to move files to destinate directory
        for file in file_list:
            file_path = src_path + "\\" + item + "\\" + file
            # print(file_path)  # Debug
            # print(dest_path)  # Debug

            # Copy files to destinate directory
            shutil.move(file_path, dest_path)
            print(file_path + "-- File Moved!")


if __name__ == "__main__":
    main()

