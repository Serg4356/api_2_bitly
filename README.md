# BITLY LINK CUTTER
This script provides simple interface to create short links on bit.ly and to get count of redirects of your shortenned link from console.

# HOW TO INSTALL

python has to be installed on your system. Use pip (or pip3 if there is conflict with Python 2) to install dependences.
```
pip install -r requirements.txt
```
It is recommended to use virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) to isolate your project

# QUICKSTART

After installation type into console:
```
$python bitly.py https://your_long_link.com/something
```
The script takes only 1 argument - link. If it is short bit.ly link - script returnes it's count of redirects. In case it's new link, you want to make shorter and control - script returns new processed link from bit.ly. In case of error you will recieve warning message.  


# PROJECT GOALS
Project was created for educational purposes. Training course for web-developers - [dvmn.org](https://dvmn.org) 
