import os
import shutil

path = "Filec2.txt"

try:
    os.remove(path)       # delete a file
    # os.rmdir(path)        delete an empty folder
    # shutil.rmtree(path)   delete a folder containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission")
except OSError:
    print("You can not delete that using that function")
else:
    print(path + " was deleted")