# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Optional, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

class ActionCovidSituation(Action):
    def __init__(self):
       pass 
​
    def name(self) -> Text:
        return "action_query_situation"
​
    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        location = tracker.get_slot('location')
        data = tracker.get_slot('data')
        
        if not location:
            location = 'China'
        if not data:
            data = 'infection'
        amount = getdata(location, data)

        dispatcher.utter_message(
                template="utter_covid_situation",
                amount="{amount:.2f}",
                data="{:.2f}",
            )
            return [
                SlotSet("location", location),
                SlotSet("amount", amount),
                SlotSet("data", data),
            ]