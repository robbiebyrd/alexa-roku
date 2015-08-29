#! /usr/bin/python
#################################################
#       Alexa Skills Kit Hello World            #
#################################################
# Zachary Priddy - 2015                         #
# me@zpriddy.com                                #
#                                               #
# Features:                                     #
#################################################
#################################################

PATH_TO_CRT = '/etc/pki/tls/certs/star.robbiebyrd.com.crt'
PATH_TO_KEY = '/etc/pki/tls/certs/star.robbiebyrd.com.key'

def run(app):

    try:
        from OpenSSL import SSL
        import ssl
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain(PATH_TO_CRT, PATH_TO_KEY)
        app.run(debug=True,
                port=443,
                ssl_context=context,
                threaded=True,
                use_reloader=True,
                use_debugger=True,
                host='0.0.0.0'
                )
    finally:
        print("Disconnecting clients")

    print("Done")