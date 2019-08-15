import os
import requests

def is_request_valid(request):
    
    is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
    is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']

    return is_token_valid and is_team_id_valid

def get_leaves():
    GET_LEAVE_URL = "https://0o8rskfyfd.execute-api.us-east-1.amazonaws.com/dev/leaves"
    response = requests.get(GET_LEAVE_URL)
    return response.json()['leaves']['allLeaves']['data']
