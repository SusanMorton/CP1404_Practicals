"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    #print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics\Christmas')

    for directory_name, subdirectories, filenames in os.walk('.'):
       # print("Directory:", directory_name)
       # print("\tcontains subdirectories:", subdirectories)
       # print("\tand files:", filenames)
       # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            current_name = os.path.join(directory_name, filename)
            print(current_name)
            new_file_name = get_fixed_filename(filename)
            #new_name = os.path.join(directory_name, get_fixed_filename(filename))
            #print(new_name)
            #os.rename(current_name, new_name)



def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
