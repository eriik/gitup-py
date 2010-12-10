# Gitup-py
Gitup in python. [Original ruby-version by David Svensson](https://github.com/standoutdavid/gitup)

Written because I don't use ruby and I'm using windows.

This is for us working with the cmd.exe (not the Git Bash).

## How to use it
[General information on how to use gitup.](https://github.com/standoutdavid/gitup#readme)
### Windows
First, clone:
`git clone git://github.com/eriik/gitup-py.git`

Then you've gotta know what path you're using:
`cd gitup-py`
`echo %cd%`

Add this path to the "enviroment variable path" by right clicking "Computer" -> "Properties" -> "Advanced System Settings" -> Tab "Advanced" -> "Enviroment Variables..."

Scroll down in the System variables to "Path", select it and choose "Edit". Go to the last character, add a semicolon and then your path. Should look something like this: `[...]Program Files\Mercurial\;C:\Program Files\Git\cmd;C:\Temp\gitup-py`

Now, just fire up cmd and use `gitup` and `gitdown` in your git-directories.

###Linux/Mac
Can be possible by making .sh-files just like the .bat files, and maybe using symbolic links from /usr/sbin or something?