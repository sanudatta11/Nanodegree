import os
def rename_files():
    #Opening each files
    list = os.listdir(r"H:\Nanodegree\Secret Message - Mini Project\prank")
    os.chdir(r"H:\Nanodegree\Secret Message - Mini Project\prank")
    #Renaming files
    for file_name in list:
        
        new_name = os.rename(file_name, file_name.translate(None, "0123456789"))
    

rename_files()
