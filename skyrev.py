import os
import shutil
import zipfile
from colorama import Fore, Style

def remove_virus_class(jar_file_path, new_jar_file_path):
    temp_directory = "temp_extracted_jar"
    os.makedirs(temp_directory, exist_ok=True)

    try:
        with zipfile.ZipFile(jar_file_path, 'r') as jar_file:
            jar_file.extractall(temp_directory)

        virus_class_files = []
        for root, dirs, files in os.walk(temp_directory):
            for file in files:
                if "L10" in file:
                    virus_class_files.append(os.path.join(root, file))

        if virus_class_files:
            for class_file in virus_class_files:
                os.remove(class_file)

        with zipfile.ZipFile(new_jar_file_path, 'w') as new_jar_file:
            for root, dirs, files in os.walk(temp_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, temp_directory)
                    new_jar_file.write(file_path, arcname=relative_path)

        print(Fore.GREEN + f"{jar_file_path} cleaned successfully!" + Style.RESET_ALL)
    finally:
        shutil.rmtree(temp_directory)

def replace_javassist_directory(jar_file_path, new_jar_file_path):
    temp_directory = "temp_extracted_jar"
    os.makedirs(temp_directory, exist_ok=True)

    try:
        with zipfile.ZipFile(jar_file_path, 'r') as jar_file:
            jar_file.extractall(temp_directory)

        javassist_directory = os.path.join(temp_directory, 'javassist')
        if os.path.exists(os.path.join(javassist_directory, 'A.class')):
            shutil.rmtree(javassist_directory)

        with zipfile.ZipFile(new_jar_file_path, 'w') as new_jar_file:
            for root, dirs, files in os.walk(temp_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, temp_directory)
                    new_jar_file.write(file_path, arcname=relative_path)

        print(Fore.GREEN + f"{jar_file_path} cleaned successfully!" + Style.RESET_ALL)
    finally:
        shutil.rmtree(temp_directory)

def update_jar_files(old_directory, new_directory):
    for root, dirs, files in os.walk(old_directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Check if the file is a JAR file
            if file.endswith('.jar'):
                new_file_name = os.path.basename(file_path)
                new_file_path = os.path.join(new_directory, new_file_name)
                remove_virus_class(file_path, new_file_path)
                replace_javassist_directory(new_file_path, new_file_path)


def check_and_remove_skyrage(directory):
    skyrage_path = os.path.join(directory, 'microsoft-vm-core')

    if os.path.exists(skyrage_path):
        print(Fore.RED + "System is infected. Removing Skyrage..." + Style.RESET_ALL)
        if os.path.isfile(skyrage_path):
            os.remove(skyrage_path)
        elif os.path.isdir(skyrage_path):
            shutil.rmtree(skyrage_path)
    else:
        print(Fore.GREEN + "System is clean." + Style.RESET_ALL)


directory = os.path.join(os.path.expanduser("~"), "AppData", "LocalLow", "Microsoft", "Internet Explorer", "DOMStore")
check_and_remove_skyrage(directory)

old_directory = input("Enter the directory containing the infected JAR files: ")
new_directory = input("Enter a new directory to put the clean JAR files: ")

if not os.path.isdir(old_directory):
    print(f"The directory '{old_directory}' does not exist.")
elif not os.path.isdir(new_directory):
    print(f"The directory '{new_directory}' does not exist.")
else:
    update_jar_files(old_directory, new_directory)

input("Click enter to exit")
