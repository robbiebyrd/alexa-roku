#! /usr/bin/python
import json
import roku
appVersion = 1.0

ROKU_IP = '72.182.86.27'

def data_init():
    global MyDataStore
    MyDataStore = DataStore()

    global roku
    roku = roku.Roku(ROKU_IP)



def data_handler(rawdata):
    global MyDataStore
    print(rawdata)
    currentSession = MyDataStore.getSession(rawdata['session'])
    currentUser = MyDataStore.getUser(rawdata['session'])
    currentRequest = rawdata['request']
    response = request_handler(currentSession, currentUser, currentRequest)


    #print json.dumps({"version":appVersion,"response":response},sort_keys=True,indent=4)

    return json.dumps({"version":appVersion,"response":response},indent=2,sort_keys=True)


def request_handler(session, user, request):
    requestType = request['type']
    
    if requestType == "LaunchRequest":
        return launch_request(session, user, request)
    elif requestType == "IntentRequest":
        return intent_request(session, user, request)


def launch_request(session, user, request):
    output_speech = "Welcome to Roku Control App. Please say a command."
    output_type = "PlainText"

    card_type = "Simple"
    card_title = "Roku Control App - Welcome"
    card_content = "Welcome to the Roku Control app. Please say a command to get started."

    response = {"outputSpeech": {"type":output_type,"text":output_speech},"card":{"type":card_type,"title":card_title,"content":card_content},'shouldEndSession':False}

    return response

def intent_request(session, user, request):
    global roku
    print("intent_request")

    if request['intent']['name'] ==  "RokuPlay":
        output_speech = "Play"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.play()

        return response

    elif request['intent']['name'] ==  "RokuReverse":
        output_speech = "Rewind"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.reverse()

        return response

    elif request['intent']['name'] ==  "RokuForward":
        output_speech = "Fast Forward"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.forward()

        return response

    elif request['intent']['name'] ==  "RokuHome":
        output_speech = "Home"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.home()

        return response
    
    elif request['intent']['name'] ==  "RokuSelect":
        output_speech = "Select"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.select()

        return response

    elif request['intent']['name'] ==  "RokuLeft":
        output_speech = "Left"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.left()

        return response

    elif request['intent']['name'] ==  "RokuRight":
        output_speech = "Right"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.right()

        return response

    elif request['intent']['name'] ==  "RokuDown":
        output_speech = "Down"
        output_type = "PlainText"

        roku.down()

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        return response

    elif request['intent']['name'] ==  "RokuUp":
        output_speech = "Up"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.up()

        return response

    elif request['intent']['name'] ==  "RokuBack":
        output_speech = "Back"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.back()

        return response

    elif request['intent']['name'] ==  "RokuReplay":
        output_speech = "Replay"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.replay()

        return response

    elif request['intent']['name'] ==  "RokuInfo":
        output_speech = "Info"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.info()

        return response

    elif request['intent']['name'] ==  "RokuBackspace":
        output_speech = "Backspace"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.backspace()

        return response

    elif request['intent']['name'] ==  "RokuEnter":
        output_speech = "Enter"
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.enter()

        return response

    elif request['intent']['name'] ==  "RokuSearch":
        search_value = request['intent']['slots']['Search']['value']
        output_speech = "Searching for " + str(search_value)
        output_type = "PlainText"

        response = {"outputSpeech": {"type":output_type, "text":output_speech}, 'shouldEndSession':True}

        roku.home()
        roku.search()
        roku.left()
        roku.select()
        roku.literal('  ' + str(search_value))

        return response

    elif request['intent']['name'] ==  "HelpIntent":
        output_speech = "This is the Nest control app. You can tell me to set temperature to 74 degrees fahrenheit. You can also say that you are too hot or too cold and I will adjust the temperature by two degrees."
        output_type = "PlainText"

        card_type = "Simple"
        card_title = "Roku Control - Help"
        card_content = "Say: Pause, Play, Next, Select, Left, Right, Up, Down, Replay, Backspace and Search."

        response = {"outputSpeech": {"type":output_type,"text":output_speech},"card":{"type":card_type,"title":card_title,"content":card_content},'shouldEndSession':False}

        return response

    else:
        return launch_request(session, user, request) ##Just do the same thing as launch request


class Session:
    def __init__(self,sessionData):
        self.sessionId = sessionData['sessionId']


    def getSessionID(self):
        return self.sessionId

class User:
    def __init__(self,userId):
        self.userId = userId
        self.settings = {}

    def getUserId(self):
        return self.userId

class DataStore:
    def __init__(self):
        self.sessions = {}
        self.users = {}

    def getSession(self,session):
        if session['new'] is True or session['sessionId'] not in self.sessions:
            self.sessions[session['sessionId']] = Session(session)

        return self.sessions[session['sessionId']]

    def getUser(self,session):
        userId = session['user']['userId']
        if userId not in self.users:
            self.users[userId] = User(userId)

        return self.users[userId]
