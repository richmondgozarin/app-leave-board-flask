import os
import slack

class SlackWebClient:

    def __init__(self, api_token, channel):
        self.channel = channel
        self.api_token = api_token

    def webClient(self):
        client = slack.WebClient(token=self.api_token)

        return client

    def postMessage(self, message:object): 
        client = self.webClient()
        
        return client.chat_postMessage(channel=self.channel, **message)