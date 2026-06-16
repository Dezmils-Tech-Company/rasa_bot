# This file contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime


class ActionServiceInfo(Action):
    """Provides information about Dezmils Tech Company services"""

    def name(self) -> Text:
        return "action_service_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        service_type = tracker.get_slot("service_type") or "general"

        if service_type == "software":
            dispatcher.utter_message(text="We specialize in custom software solutions including website development, mobile apps, AI assistants, and enterprise software. Our team uses modern technologies to deliver scalable, secure applications tailored to your business needs.")
        elif service_type == "kra":
            dispatcher.utter_message(text="Our KRA services include tax return filing, PIN registration, tax compliance advisory, and help with tax disputes. We ensure your tax filings are accurate and submitted on time to avoid penalties.")
        elif service_type == "cyber":
            dispatcher.utter_message(text="Our cyber services cover printing, binding, photocopying, scanning, lamination, CV writing, and online application assistance for HELB, jobs, and other services. We offer high-quality, fast turnaround services at competitive prices.")
        elif service_type == "installation":
            dispatcher.utter_message(text="We provide professional installation services for WiFi networks, CCTV security systems, and DSTV satellite installations. Our certified technicians ensure proper setup and configuration for optimal performance.")
        elif service_type == "design":
            dispatcher.utter_message(text="Our design services include logo design, business cards, flyers, posters, banners, and brand identity development. We create visually appealing designs that effectively communicate your message and brand.")
        else:
            dispatcher.utter_message(text="We offer a variety of services including website development, mobile apps, software solutions, KRA tax filing, cyber services (printing, binding, etc.), installation services (WiFi, CCTV, DSTV), design services, and appointment booking. Which service are you interested in?")

        return []


class ActionCheckStatus(Action):
    """Checks the status of a customer's request or order"""

    def name(self) -> Text:
        return "action_check_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # In a real implementation, this would query a database
        # For now, we'll provide a mock response
        name = tracker.get_slot("name") or "there"
        dispatcher.utter_message(text=f"Hi {name}, I'd be happy to check the status of your request. However, I'll need your reference number or order ID to look up the specific details in our system. Could you please provide that information?")

        return []


class ActionProcessPayment(Action):
    """Provides payment information and processes payment requests"""

    def name(self) -> Text:
        return "action_process_payment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="We accept payments via M-Pesa. Our paybill number is 123456 and till number is 789012. To make a payment:\n1. Go to M-Pesa Menu\n2. Select Lipa na M-Pesa\n3. Choose Pay Bill\n4. Enter our paybill number: 123456\n5. Enter your account number (your name or reference)\n6. Enter the amount\n7. Enter your M-Pesa PIN\n8. Confirm the payment\n\nWould you like to proceed with a payment?")

        return []


class ActionRequestHumanAgent(Action):
    """Handles requests to speak with a human agent"""

    def name(self) -> Text:
        return "action_request_human_agent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Sure, let me connect you to a human agent. Please hold on while I transfer you to one of our customer service representatives who will be able to assist you further.")

        # In a real implementation, this might trigger a webhook or API call
        # to actually transfer to a human agent

        return []


class ActionHandleComplaint(Action):
    """Handles customer complaints"""

    def name(self) -> Text:
        return "action_handle_complaint"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I'm sorry to hear that you're not satisfied with our service. Please provide more details about your concern so I can escalate it to the appropriate team for resolution. Your feedback helps us improve our services.")

        return []


class ActionDefaultFallback(Action):
    """Handles fallback when NLU confidence is low"""

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I'm sorry, I didn't quite understand that. Could you please rephrase your question or let me know how I can help you with our services?")

        return []