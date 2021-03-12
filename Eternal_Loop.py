#!/usr/bin/env python3

from zipfile import ZipFile as zp

##Extracting the first zip
zip_file = 'Eternal_Loop.zip'
passwd = 'hackthebox'

with zp(zip_file,"r") as zf:
    zf.extractall(pwd = bytes(passwd, encoding='utf8'))
zf.close()
###

##Extracting the rest of files, using the file inside as password for the next zip

internal_zip_file = '37366.zip'
passwd_internals = '5900'

while True:
    with zp(internal_zip_file,"r") as zf:
        for name in zf.namelist():
            passwd_internals = name.replace(".zip","")
        
        print(internal_zip_file + " = " + passwd_internals)
        if internal_zip_file == "6969.zip":
            print("The last file is: " + internal_zip_file + " with file: " + passwd_internals)
            break
        zf.extractall(pwd = bytes(passwd_internals, encoding='utf8'))
        internal_zip_file = passwd_internals + ".zip"
        zf.close()