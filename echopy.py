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
import daemon

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


with daemon.DaemonContext():
    myApp.data_init()
    print('run')
    run_echopy_app()
