import os
import pathlib
import csv

def main():
    folder_name = input("Enter folder to convert: ")

    # C:\CPCe_41_inst\OMLC_code-7CAT.txt
    codefile_path = input("Enter full path to codefile: ")
    cwd = os.getcwd()
    
    for (dirpath, _, filenames) in os.walk(folder_name):
        cpc_filenames = filter(lambda fname: pathlib.Path(fname).suffix.lower() == ".cpc", filenames)

        for cpc_filename in cpc_filenames:
            full_cpc_filename = os.path.join(dirpath, cpc_filename)

            with open(full_cpc_filename, "r") as f:
                # splitting by "," doesn't work when there are commas in the filename
                reader = csv.reader(f)
                header = next(reader)   

                remaining = f.read()

            header[0] = "\"" + codefile_path + "\""
            header[1] = "\"" + os.path.join(cwd, os.path.splitext(full_cpc_filename)[0] + ".JPG") + "\""
            
            with open(full_cpc_filename, "w") as f:
               f.write(",".join(header) + "\n" + remaining)

    print("Conversion successful")
                


if __name__ == '__main__':
    main()