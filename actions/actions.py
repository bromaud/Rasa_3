
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_ACCOUNT_NUMBER = re.compile(r'^\d{10}$')
ALLOWED_NAME = ["bright", "chandra", "chinedu", "arulappan", "david"]

class ValidateSimpleBalanceForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_balance_form"

    def validate_account_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `account_number` value."""

        if slot_value.lower() not in ALLOWED_ACCOUNT_NUMBER:
            dispatcher.utter_message(text=f"We only accept 10digits numbers.")
            return {"account_number": None}
        dispatcher.utter_message(text=f"OK! You want to the balance of your account {slot_value} ?")
        return {"account_number": slot_value}

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name` value."""

        if slot_value not in ALLOWED_NAME:
            dispatcher.utter_message(text=f"I don't recognize that name. We only attend to {'/'.join(ALLOWED_NAME)}.")
            return {"name": None}
        dispatcher.utter_message(text=f"OK! You want to the balance of your {slot_value}'s account ?")
        return {"name": slot_value}