# What FileSearching is all about -
Well FileSearcing program provide you the better way to search your files( based on extension ) from anywhere in the system. 

It also provide a copy of searched items in a newly created directory along with a file which consist of paths. Here path referred to that location where those items exist.

User need to provide the file extension and Location in order to search item and in return user have names/paths of searched items, and able to copy searched items.

For example : 

    input -> mp3
             location (/home/Downloads , /usr/bin)
             
    output -> Names/Paths of mp3 files 
                    or
              Copy files to a newly created directory

# How This Works - 
-> OS - https://docs.python.org/3/library/os.html

-> Shutil - https://docs.python.org/3/library/shutil.html

-> Regex - https://docs.python.org/3/library/re.html

-> Sys - https://docs.python.org/3/library/sys.html

    # -> os.walk()
    os.walk() helps me to iterate over a list of folders, subfolders, files .
    Using os.walk(path) we assume three variables in the for loop one for directory path, second for list of sub-directory and third                  for list of files and we only need to search files nor any directory or sub-directory.

    now, what we gonna do is iterate through every element inside the list of files (k) and use regex pattern matching there .
  
    # -> Regex Pattern
    for searching a file from a list of files, We can do file.endswith(string) but this provide only a limited scope. So, We're         using Regex Pattern to make our searching more effective and Accurate and we can append more pattern here which can't be done in    file.endswith(string) function 

    # -> shutil.copy()
    This function helps me to copy files from source path to destination path .
  
Well i use more diff-diff. functions which have their own functionality in the program but these three is like a blueprint so that a end-user can understand how FileSearching works without even check every line of the code
