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
def run(app):

    try:
        from OpenSSL import SSL
        context = SSL.Context(SSL.SSLv23_METHOD)
        context.use_privatekey_file('/etc/pki/tls/certs/star.robbiebyrd.com.key')
        context.use_certificate_file('/etc/pki/tls/certs/star.robbiebyrd.com.crt')
        app.run(debug=True,
                port=5000,
                ssl_context=context,
                threaded=True,
                use_reloader=False,
                use_debugger=True,
                host='0.0.0.0'
                )
    finally:
        print("Disconnecting clients")

    print("Done")