a = Alexa()
a.register_intent('IntentName', 'Type', 'function', 'application_id')

def incoming_function(request):
    card = AlexaCard('Test', 'Testing one two there')
    to_speak = AlexaSpeak('Test', 'Testing one two there')
    does_this_end = True
    print(AlexaResponse(a, card, to_speak, does_this_end).to_json())

