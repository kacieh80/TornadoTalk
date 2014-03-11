TornadoTalk
===========

This hits googles maps API to demonstrate the asynchronous abilities of Python Tornado Web Server


##Requirements:

###Google API Key:

* Log in to your google account and go here: https://console.developers.google.com/project
* Create a new project
* Wait for it to create
* Go to APIs and Auth
* Find the 'Google Maps Engine API'
* Click on the title
* Click the off button to turn it on
* Go to the 'Credintials' link under the API link
* Under the Public API access section click "Create New Key"
* Select "Browser Key"
* Click "Create" (Leaving the text box blank)

##Mac/Linux
Now you have an api key that you can put into application/main.py for the api_key variable. If you are on Windows and For the mac and linux users these things are fairly simple to install:

* Python3
* pip
* virturalenv

#Windows users:

####Get Git
http://windows.github.com/

####Get Python
* If you don't already have python scroll to the bottom here: http://www.python.org/download/releases/3.3.5/ 
* Then download the: Windows x86 MSI installer

####Make it run from command line (Windows 8 - if less than Windows 8 find out how to edit your environment variables)
* Search Control Panel for 'environment variables' and click to edit them
* Follow the instructions here to add your Python folder: http://docs.python.org/2/using/windows.html#finding-the-python-executable
* Go ahead and add <your python folder>/Scripts to your environment variables as well
* Verify you have python in your cmd by opening up your command line and typing:

``` 
python -V
```

* Great job!
* Now download the following files into your python/Scripts directory (the same one you added to your environment variables)
* https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
* https://raw.github.com/pypa/pip/master/contrib/get-pip.py
* Use your command line prompt, navigate to the Scripts folder where you saved the files and run 

```
python ez_setup.py
python get-pip.py
```
 
Assuming this all went successful type:

```
pip install virtualenv
```

#Instructions:

Clone this repo letting it make default folder of  TornadoTalk

```
#For Mac and Linux users
virtualenv TornadoTalk
cd TornadoTalk
source bin/activate
pip install tornado
```

```
#For Windows
virtualenv TornadoTalk
cd TornadoTalk
Scripts/activate.bat
pip install tornado
```

Now edit application/main.py to have your api key

To start the application up simply type: 

```
python applicaton/main.py
```

go to localhost:8000


