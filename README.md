# Purpose of this code
I have to control my time, but also I have big problems with willpower. So, this code is a solvation willpower problem.
It's stops problematic apps, and gives me to remember about important steps of self control.
Hope that no one else need this stuff.


# How to start it 
You must edit ExecPath in .sevice file. After that just create symlink to it.
```shell
#sudo ln -s /path/to/serice/dir/willpower.service  /usr/lib/systemd/system/willpower.service
```
And run this.
```shell
sudo systemctl daemon-reload
sudo systemctl start willpower.service
```


# Settings
Script takes settings from .ENV file.
```
APPS=telegram,chrome  #list of application name
USE_TTS=True          #using Text-to-Speech 
TTS_STRING=Stop it right now! #string to say. Language hardcoded in main.py. Sorry, guys
APP_WT=18,21,6,21     #list of allowed time for each app (so two values per app)
```
