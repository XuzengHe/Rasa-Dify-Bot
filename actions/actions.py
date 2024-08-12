# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionDifyIntegration(Action):

    def name(self) -> Text:
        return "action_dify_integration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']
        dify_response = self.query_dify(user_message)

        dispatcher.utter_message(text=dify_response)
        return []

    def query_dify(self, message: Text) -> Text:
        # Replace with your Dify API endpoint and API key
        
        # TODO: SWITCH TO THE NEW USER-SPECIFIC DIFY WORKFLOW
        url = "https://dev-soma.securezebra.com/v1/chat-messages"
        headers = {
            "Authorization": "Bearer app-fmkFJlUo2V4BuV3R9vym9NP6",
            "Content-Type": "application/json"
        }
        data = {
    		"inputs": {},
    		"query": message,
    		"response_mode": "blocking",
    		"conversation_id": "",
    		"user": "admin",
    		"files": []
		}
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get('answer', 'Sorry, I did not get that.')
        else:
            return "Error connecting to Dify"


