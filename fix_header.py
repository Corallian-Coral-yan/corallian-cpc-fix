import os
import pathlib
import csv
from colorama import Fore, Style, init

init(autoreset=True)


def process_folder(folder_name, codefile_path):
    # folder_name = input("Enter folder to convert: ")
    # # C:\CPCe_41_inst\OMLC_code-7CAT.txt
    # # C:\CPCe_41_inst\NACRE_SHINE_40 _TUBB.txt
    # codefile_path = input("Enter full path to codefile: ")
    cwd = os.getcwd()

    for (dirpath, _, filenames) in os.walk(folder_name):
        cpc_filenames = filter(lambda fname: pathlib.Path(
            fname).suffix.lower() == ".cpc", filenames)

        for cpc_filename in cpc_filenames:
            full_cpc_filename = os.path.join(dirpath, cpc_filename)

            with open(full_cpc_filename, "r") as f:
                # splitting by "," doesn't work when there are commas in the filename
                reader = csv.reader(f)
                header = next(reader)

                remaining = f.read()

            header[0] = "\"" + codefile_path + "\""
            header[1] = "\"" + \
                os.path.join(cwd, os.path.splitext(
                    full_cpc_filename)[0] + ".JPG") + "\""

            with open(full_cpc_filename, "w") as f:
               f.write(",".join(header) + "\n" + remaining)

    print("Conversion successful for folder: " + folder_name + "\n")


def main():
    print("\nReading input_file.txt...\n")
    with open("input_file.txt", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            codefile_path = row[0].strip().strip('"')
            folder_name = row[1].strip().strip('"')

            print(
                f"Processing folder: {Fore.GREEN}<{folder_name}>{Style.RESET_ALL} with code file: {Fore.GREEN}<{codefile_path}>{Style.RESET_ALL}")
            process_folder(folder_name, codefile_path)

    print("\nProcessing done.")


if __name__ == '__main__':
    main()
