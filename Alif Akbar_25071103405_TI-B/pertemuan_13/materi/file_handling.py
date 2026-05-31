import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("The file has been deleted")
else:
    print("The file does not exist")

os.rmdir("myfolder")