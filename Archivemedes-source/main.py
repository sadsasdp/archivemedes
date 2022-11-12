from outputUtils import ask,error,info,success,cls,divisor,exitScript
from encryptUtils import genKey,encrypt
import threading
from os import getcwd
from os.path import join as joinPath
from os.path import exists as fileExists
from os.path import isdir as fileIsDirectory
from os.path import basename as fileBasename
from os import walk as fileWalk
from os import rename as fileRename
from os import remove as fileRemove
from pathlib import Path as pathlibPath
cls()

key = None
cwd = getcwd()
custom_extension = ".archivemedes"
folders_to_encrypt = []

# Start message
success("""
   |--------------------|
   | Archivemedes v1.1  |
   |     Rewritten      |
   |--------------------|
""")
ask("Press enter to continue...\n\n")

# Key generation phase
divisor()

info("Starting to generate encryption key...")
while key == None:
   key = genKey() 
success("Successfully generated an encryption key!")

info("\nStarting to save the key in the path "+joinPath(cwd,"archivemedes_key.akf"))

# Check if a key-file already exists
if fileExists(joinPath(cwd,"archivemedes_key.akf")) == True:
   response = ask("\nDANGER: Another key-file has been found, if you continue this file will be deleted permanently.\nContinue? y/n\n").upper()
   if response == "Y":
      try:
         fileRemove(joinPath(cwd,"archivemedes_key.akf"))
         success("Deleted key-file successfully!")
      except:
         error("Error ocurred while deleting key-file, please restart.")
         exitScript()
   else:
      error("Ok, closing program.")
      exitScript()

# Creating key-file
try:
   with open(joinPath(cwd,"archivemedes_key.akf"),"wb") as key_file:
      key_file.write(key)
   success("Successfully created and writed key-file!")
except:
   error("Error ocurred while writing key-file, please restart.")
   exitScript()

# Folder selection phase
divisor()

info("Starting to select folders to encrypt...")

# Asking for folder/s
def AskForFolders():
   finished_asking = False
   while finished_asking == False:
      folder_to_add = ask("\nWhat folder do you want to encrypt?\n(Ex: C://Users//USERNAME//Desktop//FOLDER)\n")

      # Check for duplicates
      duplicate = False
      for folder in folders_to_encrypt:
            if folder == folder_to_add:
               error('Folder with path "'+folder_to_add+'" is already on the list. Skipping...')
               duplicate = True
               break
      if duplicate == True:
         continue
      
      # Adding the folder
      try:
            folders_to_encrypt.append(folder_to_add)
            success('Successfully added folder with path "'+folder_to_add+'"!')
      except:
         error('Error ocurred while adding folder with path "'+folder_to_add+'". Skipping...')
      able_to_repeat = ask("\nDo you want to add another folder?\ny/n\n").upper()
      if able_to_repeat == "Y":
         finished_asking = False
      else:
         finished_asking = True
AskForFolders()

# Checking folders
info("\nStarting to check entered folder/s...\n")
for folder in folders_to_encrypt:
   # Checking if folder exists
   if fileExists(folder) == False:
      error('Deleting folder with path "'+folder+'" from the list... (Path doesnt exists)')
      folders_to_encrypt.remove(folder)
   # Checking if folder is actually a folder
   elif fileIsDirectory(folder) == False:
      error('Deleting folder with path "'+folder+'" from the list... (Path isnt a folder)')
      folders_to_encrypt.remove(folder)
info("Finished checking entered folder/s...")
ask("\nPress enter to start encrypting the folders...")

# Extension phase
divisor()

able_to_make_new_extension = ask("Do you want to add a custom file-extension for the encrypted files? y/n\n").upper()
if able_to_make_new_extension == "Y":
   new_extension = ask("Please enter new extension.\n(Ex: new_extension_file)\n")
   new_extension = new_extension.replace(" ","")
   new_extension = new_extension.replace(".","")
   new_extension = new_extension.replace("!","")
   new_extension = new_extension.replace("?","")
   custom_extension = new_extension
   info("\nCurrent extension: "+custom_extension)
else:
   info("\nCurrent extension: "+custom_extension)


# Encryption phase
divisor()

info("Starting to encrypt folder/s...\n")

# Indexing entered folders
for folder in folders_to_encrypt:
   info('Encrypting '+folder)
   files_to_encrypt = []

   # Gathering files to encrypt
   for root, dirs, folder_files in fileWalk(folder,topdown=True):
      for file in folder_files:
         files_to_encrypt.append(joinPath(root,file))

   # Encrypting files
   
   for file in files_to_encrypt:
      content = None
      content = None
      try:
         # Extracting file content
         with open(file,"rb") as file_content:
            content = file_content.read()
         content = encrypt(content,key)
         if content == None:
            content = encrypt(content,key)
         if content == None:
            error('  Error ocurred while enctronoososdof file with path "'+fileBasename(file)+'". Skipping...')
            # Writing encrypted content
         with open(file,"wb") as file_content:
            file_content.write(content)
         file_parent = pathlibPath(file).parent.absolute()
         fileRename(file,joinPath(file_parent,fileBasename(file)+"."+custom_extension))
         success("   "+fileBasename(file)+" was encrypted successfully!")
      except:
         error('  Error ocurred while encrypting file with path "'+fileBasename(file)+'". Skipping...')
   info("Finished encrypting "+folder+"\n")

# Final phase
divisor()

info('''
Finished encrypting folders

''')

exitScript()