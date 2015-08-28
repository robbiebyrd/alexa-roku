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
        import ssl
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain('/etc/pki/tls/certs/star.robbiebyrd.com.crt', '/etc/pki/tls/private/star.robbiebyrd.com.key')
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