from outputThings import ask,success,info,error,cls,setTitle
from encryptionThings import genKey,encrypt
from time import sleep as wait
from pathlib import Path as PathCheck
import os.path
from os import getcwd,remove
from os import walk as oswalk
setTitle("Archivemedes")
cls()

# Startup messages
info("""
 -------------------  
|                   |
|                   |
| Archivemedes v1.0 |
|                   |
|                   |
 -------------------
""")
ask("Press enter to continue...\n")
wait(0.5)
cls()
info("Starting...")

# Setting main variables
folders_to_encrypt = []
key = None
cwd = getcwd()

# Ask if the user wants to add more folders to the list
def startAskingForFolders():
    finished = False
    while finished == False:
        folder = ask("Wich FOLDER do you want to encrypt? (Enter things like C://Users/USERNAME/Desktop/Folder)\n")
        for a in folders_to_encrypt:
            if a == folder:
                error("Folder already in the list, pleas enter another folder...")
                finished = False
                continue
        folders_to_encrypt.append(folder)
        success("Folder named "+folder+" added successfully...")
        able_to_continue = ask ("Do you want to add another folder to the list? y/n\n").upper()
        if able_to_continue == "Y":
            finished = False
        else:
            finished = True
startAskingForFolders()
cls()

# Check folders
info("Starting to check entered folders...")
for folder in folders_to_encrypt:
    if os.path.exists(folder) == False:
        error("Folder named "+folder+" doesn't exists, deleting...")
        folders_to_encrypt.remove(folder)
        continue
    if os.path.isdir(folder) == False:
        error("Folder named "+folder+" is not a folder, deleting...")
        folders_to_encrypt.remove(folder)
success("Finished checking entered folders...")
wait(1)

info("Creating encryption key...")
while key == None:
    wait(0.5)
    key = genKey()
info("Key created successfully, saving it to "+cwd+"/archivemedes_key.txt...")
if os.path.exists(cwd+"/archivemedes_key.txt") == True:
    if ask(cwd+"/archivemedes_key.txt already exists, this means that the key of another encryption will be deleted, do you want to continue? y/n\n").upper() == "Y":
        remove(cwd+"/archivemedes_key.txt")
    else:
        exit()
try:
    with open(cwd+"/archivemedes_key.txt","wb") as keyfile:
        keyfile.write(key)
    success("Successfully created and wrote the key in the file named "+cwd+"/archivemedes_key.txt...")
except:
    error("Error ocurred while writing the key in the file named "+cwd+"/archivemedes_key.txt, exiting in 5 seconds...")
    wait(5)
    exit()
ask("Press enter to start encrypting...\n")
cls()

# Starting to encrypt
for folder in folders_to_encrypt:
    folder_files = []
    # Get directory files (subdirectories included)
    for (dir_path, dir_names, file_names) in oswalk(folder,topdown=True):
        for file in file_names:
            folder_files.append(os.path.join(dir_path, file))

    # Indexing every file obtained from the folder and encrypting the content
    for file in folder_files:
        file_content = None

        # Open the file and extract the content in binary
        try:
            with open(file,"rb") as fileContent:
                file_content = fileContent.read()
        except:
            error("Error ocurred while opening file named "+file+". Skipping...")
            continue
        
        # Encrypt the content
        try:
            file_content = encrypt(file_content,key)
        except:
            error("Error ocurred while encrypting file named "+file+". Skipping...")
            continue
        
        # Write encrypted content in the file
        try:
            with open(file,"wb") as fileContent:
                fileContent.write(file_content)
        except:
            error("Error ocurred while writing file named "+file+". Skipping...")
            continue

        success("Successfully encrypted file named "+file+"...")


success("\nFinished encrypting\n")
ask("Enter to close Archivemedes")