
# EchoRokuPy
A python-based interface to the Roku streaming player and the Amazon Echo.

## Requirements and setup
EchoRokuPy is built using python with flask. Amazon also requires that the server running the code be publicly accessible on port 443 using https. This means that you will either have to host it on a VPS or port forward 443 from your router. 

### Local development environment
Your computer or virtual environment needs the following installed before you go any further:

* Python
* [PIP](https://pip.pypa.io/en/stable/installing.html)

To run EchoRokuPy, you'll need the python packages specified in [requirements.txt](./requirements.txt).

Once you have the above requirements installed on your computer, clone this repository, and run the following from the project root to get the environment setup for running EchoNestPy:

1. `pip install -r requirements.txt`


### Setting Up Server

The Alexa Skills Kit (ASK) requires that the server has an open connection to the internet on port 443 (HTTPS) with a SSL Certificate (self signed is okay). Right now this runs directly in flask with HTTPS.

### Setting Up Alexa Skills Kit on Amazon

The ASK is available at: https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/getting-started-guide 

2. Sign in or Create an Account. 
2. Go to Apps & Services at the top of the page
2. Click on Alexa
2. Click Add New Skill
2. Fill out the first form:
** Name: Anything you want it to be - I use Roku Control
** Invocation Name: The hotword to call the app - I have gotten it working with Player
** Version: 1.0 <- This is hard-coded for now
** Endpoint: https://<domain or ip address\>/alexa/EchoPyAPI
2. Go to the next page and copy the intentSchema.json to the Intent Schema and sampleUtterances.txt to the Sample Utterances
2. Go to the next page and upload the self signed SSL Cert you have.. and hit next..

### Settings for SSL Server
In the echopy_app.py file, there are two variables:

3. PATH\_TO\_CRT
3. PATH\_TO\_KEY

The CRT file should include your CRT file (self-signed is OK). If you are not using a self-signed CRT, then be sure to include the entire CRT chain (Root and Intermediaries) together in one file. Your private key should also be readable.

To disable built-in SSL support, change the port from 443 and remove the ssl_context setting. Both are found in the echopy_app.py file. If you wish to use a proxy server, you can change the port to something other than 443 and point your proxy server to a new port. Simply remove the line "ssl_context=context" to disable SSL. You can also comment out the following lines:

* import ssl
* context = ssl.SSLContext(ssl.PROTOCOL\_TLSv1\_2)
* context.load_cert_chain(PATH\_TO\_CRT, PATH\_TO\_KEY)


## Usage
````
run: python echopy.py
````

At this time you will have to go to your Echo and say 'Alexa, Talk to Player' (Replace Player with what the Invocation Name you set).


