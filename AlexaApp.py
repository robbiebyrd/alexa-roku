import json
from distutils.util import strtobool
import six

# CONSTANTS
_AMAZON_API_VERSION = '1.0'

def main():
    return

class Alexa():
    
    def __init__():
    
    def 
    


class AlexaApp():

    def __init__(self, incoming_data):

        if 'request' in incoming_data:
            self._request = AlexaRequest(incoming_data['request'])

        if 'session' in incoming_data:
            self._session = AlexaSession(incoming_data['session'])
        print(self._session.session_id)
        print(self._request)

    def _check(self):
        """Checks to make sure required fields are set """
        return True

class AlexaSession():
    """This class stores and returns session data as an object """

    def __init__(self, session_object):

        self._id = str()
        if 'userId'in session_object['user']:

            self._user = AlexaUser(session_object['user']['userId'])
            self._application = AlexaApplication(session_object['application']['applicationId'])
            self.session_id = session_object['sessionId']

        else:
            raise Exception('ValueError')

        if 'new' in session_object:
            self.new = session_object['new']

    @property
    def session_id(self):
        return self._id
    @session_id.setter
    def session_id(self, value):
        self._id = value

    @property
    def new(self):
        return bool(self._new)
    @new.setter
    def new(self, value):
        try:
            self._new = bool(value[0])
        except:
            self._new = True

class AlexaRequest():
    """This class stores and returns request data as an object  """

    def __init__(self, request_object):
        
        ##        VARIABLES           ##
        #          Required
        self._id                = str()
        self._request_type      = str()

        #        Not required
        self._timestamp         = str()
        self._intent            = str()
        if set(('type','requestId')) <= set(request_object):
            self.request_id = request_object['requestId']
            self.request_type = request_object['type']
        else:
            raise Exception('ValueError')

        if 'intent' in request_object:
            self.intent = request_object['intent']['name']

        if 'timestamp' in request_object:
            self.timestamp = request_object['timestamp']

    @property
    def request_id(self):
        return self._id
    @request_id.setter
    def request_id(self, value):
        self._id = value


class AlexaUser():
    """This class stores and returns request data as an object """

    def __init__(self, user_id):
        ##        VARIABLES           ##
        #          Required
        self._id                = str()
        
        if user_id:
            self.user_id = user_id
        else:
            raise Exception('ValueError')

    @property
    def user_id(self):
        return self._id
    @user_id.setter
    def user_id(self, value):
        self._id = value
        
class AlexaApplication():
    """This class stores and returns application data as an object """

    def __init__(self, application_id):
        ##        VARIABLES           ##
        #          Required
        self._id                = str()
        
        if application_id:
            self._id = application_id
        else:
            raise Exception('ValueError')

    @property
    def application_id(self):
        return application_id
    @application_id.setter
    def application_id(self, value):
        self._id = value

### Alexa Content

class AlexaSpeak():
    def __init__(self, content, output_type="PlainText"):
        self.output_type = "PlainText"
        self.content = content

    def obj_return(self):
        response = {
            "outputSpeech": {
                "type": self.output_type,
                "text": str(self.content)
            }
        }

        return response

    def to_json(self):
        return json.dumps(obj_return())

class AlexaReprompt():
    def __init__(self, content, output_type="PlainText"):
        self.output_type = "PlainText"
        self.content = content

    def obj_return(self):
        response = {
            "reprompt":{
            "outputSpeech": {
                "type": self.output_type,
                "text": str(self.content)
            }
        }}

        return response

    def to_json(self):
        return json.dumps(obj_return())

class AlexaCard():
    def __init__(self, title, content, card_type="Simple"):
        self.card_type = "Simple"
        self.title = ""
        self.content = ""

    def obj_return(self):
        response = {
            "card":{
                "type": self.card_type,
                "title": self.title,
                "content": self.content
                }
            }
        return response
    
    def to_json(self):
        return json.dumps(obj_return())


class AlexaResponse():
    def __init__(self, app, card, speak, to_end=True, reprompt=""):
        self._response = {
            "version": _AMAZON_API_VERSION,
            "shouldEndSession": to_end,
            "response":{}
        }
        self._response['response'].update(speak.obj_return())
        self._response['response'].update(card.obj_return())
        if reprompt != "":
            self._response['response'].update(reprompt.obj_return())

    def to_json(self):
        return json.dumps(self._response)
    

if __name__ == '__main__':
    main()
