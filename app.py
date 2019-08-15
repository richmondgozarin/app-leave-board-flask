import os
import requests
from http_utility import is_request_valid, get_leaves
from slack_web_client import SlackWebClient
from slack_message_builder import leave_form_message, my_leaves_message
from flask import abort, Flask, jsonify, request, Response


app = Flask(__name__)


@app.route('/leave', methods=['POST'])
def leave():
    if not is_request_valid(request):
        abort(400)

    slack_token = os.environ["SLACK_API_TOKEN"]  
    channel_id = request.form['channel_id']
    
    if request.form['text'] == 'list':
        all_leaves(channel_id)
    else:
        #create a new slack web client()
        client = SlackWebClient(slack_token, channel_id)
        message = leave_form_message()
        client.postMessage(message)
        
        return jsonify(code=200)


def all_leaves(channel_id):
    if not is_request_valid(request):
        abort(400)

    slack_token = os.environ["SLACK_API_TOKEN"]  

    leaves_response = get_leaves()
    
    #create a new slack web client()
    client = SlackWebClient(slack_token, channel_id)
    message = my_leaves_message(leaves_response)
    client.postMessage(message)
    
    return jsonify(code=200)
    