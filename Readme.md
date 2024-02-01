# App backup in python

This app is for backup some files that you want to save. When you setup and launch it, it will create .tar files with all the thing that you want to save. You can save it on your machine or on a remote machine with ssh. The app create a backup every day.

# How to install 

First you need to clone the repo in /usr/local/bin/ with this command ```sudo git clone https://github.com/matastrals/App-backup-python.git```.
After that, you need to move into the repo and to install pip and two libs python. You can run the file with this command ```sudo bash requirement.sh```.
Then, you need to give some perm at some files and dir. 
Run ```sudo bash init.sh```.

And there we go ! The app is running !

If you need to change the directory where you want to put backup or the directory that you want to save, you can do it in backup.json by changing the "path".
You can also set the ssh method in the same file. 
