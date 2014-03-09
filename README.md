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

Now you have an api key that you can put into application/main.py for the api_key variable. You will also need to have:

* Python3
* pip
* virturalenv

##Instructions:

* Clone this repo letting it make default folder of  TornadoTalk
* Then 'virtualenv  TornadoTalk'
* cd  TornadoTalk
* source bin/activate
* pip install tornado
* edit application/main.py to have your api key

To start the application up simply type: python applicaton/main.py

go to localhost:8000
