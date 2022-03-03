# Privacy-Lept System

Privacy-Lept System is a play on words where the system will literally zero your privacy where it will show when you are online and from which device you are connecting to the internet. Why I built this? No clue; I just wanted to show anyone who visits my personal website https://niweera.gq that I am online or offline. Also, I just wanted to try to do something I've never done 😂. 

Privacy-Lept System is consisted with three components.

![image](https://i.imgur.com/5FpSJKb.jpg)

1. [Privacy-Lept-Desktop](https://github.com/Niweera/privacy-lept-desktop) (Windows service)

2. [Privacy-Lept-Mobile](https://github.com/Niweera/privacy-lept-app) (Android application)

3. [Privacy-Lept-API](https://github.com/Niweera/privacy-lept-api) (Socket.io NodeJS Express App)

When I'm online, from Desktop and Mobile, it will notify the Privacy-Lept-API and the Privacy-Lept-API will notify my website using [socket.io](https://socket.io/). 


## Privacy-Lept-Desktop 

This is the desktop host Windows service for the Privacy-Lept system.

### Setup

All the setup methods should be done in an Administrator prompt.

```bash
$ pip install -r requirements.txt

# Install service
$ python WindowsService.py install

# Update service
$ python WindowsService.py update

# Remove service
$ python WindowsService.py remove
```