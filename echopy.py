#! /usr/bin/python
#################################################
#        Alexa Skills Kit Hello World            #
#################################################
# Zachary Priddy - 2015                         #
# me@zpriddy.com                                 #
#                                                #
# Features:                                     #
#################################################
#################################################

import os
import echopy_app
import echopy_doc
import echopy_roku as myApp
from flask import Flask, render_template, Response, send_from_directory, request, current_app, redirect, jsonify, json
from OpenSSL import SSL
import socketserver
import sys
import time
from daemon import Daemon

class MyDaemon(Daemon):
        def run(self):
                myApp.data_init()
                run_echopy_app()


app = Flask(__name__)

@app.route("/")
def main():
    return echopy_doc.main_page


@app.route("/EchoPyAPI",methods = ['GET','POST'])
def apicalls():
    if request.method == 'POST':
        data = request.get_json()
        print("POST")
        sessionId = myApp.data_handler(data)
        return sessionId + "\n"




def run_echopy_app():
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    echopy_app.run(app)


if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
            print "usage: %s start|stop|restart" % sys.argv[0]
            sys.exit(2)
