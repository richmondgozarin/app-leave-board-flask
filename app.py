import os
import requests
from http_utility import is_request_valid, get_leaves
from slack_web_client import SlackWebClient
from slack_message_builder import leave_form_message, my_leaves_message
from flask import abort, Flask, jsonify, request, Response


app = Flask(__name__)

#create a new slack web client()
slack_token = os.environ["SLACK_API_TOKEN"]  
client = SlackWebClient(slack_token)

@app.route('/leave', methods=['POST'])
def leave():
    if not is_request_valid(request):
        abort(400)

    channel_id = request.form['channel_id']
    
    if request.form['text'] == 'list':
        all_leaves(channel_id)
    else:
        message = leave_form_message()
        client.postMessage(channel_id, message)
        
        return jsonify(code=200)


def all_leaves(channel_id):
    if not is_request_valid(request):
        abort(400)

    leaves_response = get_leaves()
    
    message = my_leaves_message(leaves_response)
    client.postMessage(channel_id, message)
    
    return jsonify(code=200)
    

if __name__ == "__main__":
    app.run(debug=True)
    