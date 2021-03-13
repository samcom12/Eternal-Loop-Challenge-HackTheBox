# Eternal Loop Challenge HackTheBox

Walkthough about "Eternal Loop" Misc Challenge from Hack The Box


# Environment

Kali Linux - So we have John The Ripper, Python3 and wordlists like "rockyou" preinstalated. It could be another distribution like Parrot OS.

# Walkthough

You can find this challenge in www.hackthebox.eu

The Eternal Loop challenge will appeas like that:

![](https://i.ibb.co/b6PVDDL/imagen-2021-03-12-202705.png)

So, to get started we have to download the zip from the web.
Now we can execute the script ```Eternal_Loop.py```, the script will unzip all the zips one inside another, the first zip will unzipped with the passwd 'hackthebox' and for the next we discovered that the name of the file inside the zip is the password of the zip itself.

![](https://i.ibb.co/Vj37s78/descarga-3.png)

When the script finish, we'll see this output:

```
The last file is: 6969.zip with file: DoNotTouch
```

Now, after we check that we dont know the password of this zip, we'll need to crack it, I'll use John The Ripper:

To get the hash, use zip2john:

```bash
zip2john 6969.zip > htb.hash  
```

And to get the hash cracked i'll use the wordlist "rockyou", if you are using kali you'll find this file in the route used in the command:

```bash
john htb.hash --wordlist=/usr/share/wordlists/rockyou.txt 
```

![](https://i.ibb.co/qRTMDHZ/descarga-4.png)

Just left unzip the file.

The file will be "DoNotTouch", if we check what type of file it is..

```bash
└─# file DoNotTouch
DoNotTouch: SQLite 3.x database, last written using SQLite version 3021000
```

So, we open the file with a SQLite Reader, we browse the datasheets until we got the flag.

![](https://i.ibb.co/Q8fLWCz/descarga.png)


## Author ✒️

* **Jorge Manuel Lozano Gómez**
