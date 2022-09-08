from flask import Flask, render_template,  request, redirect
import pandas as pd
import requests
import simplejson 
import json
import sys
import logging


application = Flask(__name__)


@application.route('/')
def Home():
    return 'Home version 1.1 <a href="/rick">Rick & Morty</a> <a href="/pokemon">Pokemon</a>'

@application.route('/rick')
def rick():
    uri = "https://rickandmortyapi.com/api/character?limit=500"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    return render_template('rick.html',  data=data)

@application.route('/pokemon')
def pokemon():
    uri = "https://pokeapi.co/api/v2/pokemon?limit=654"

    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    return render_template('pokemon.html',  data=data)



@application.route('/button')
def button_clicked():
    print('Hello world!', file=sys.stderr)
    return redirect('/')

@application.route('/print')
def printMsg():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info('testing info log')
    print('This is error output', file=sys.stderr)
    print('This is standard output', file=sys.stdout)
    return "Check your console"


@application.route("/test_rick")
def test_rick():
    uri = "https://rickandmortyapi.com/api/character"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    return data

@application.route("/test_pokemon")
def test_pokemon():
    uri = "https://pokeapi.co/api/v2/pokemon?limit=654"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    return data

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80, debug=True)
