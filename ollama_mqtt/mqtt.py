import requests
import paho.mqtt.client as mqtt
import json
import re

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "phi3"

MQTT_BROKER = "localhost"
TOPIC_Kitchen = "light/Kitchen"
TOPIC_Cup = "light/Cupboard"
TOPIC_Desk = "light/Desk"


client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)


def ask_ollama(user_input):
    prompt = f"""
You are a smart home assistant.

Convert the user request into ONE name of a light and one of the two state options in the format [lightname,state]. Else return ONLY [NONE]:
Names: Kitchen, Cupboard, Desk
State: ON, OFF

User: {user_input}

Return only two words. The first word is one name of the given names for the right light. The second word is the state of the given lamp. In the format [lightname,state].
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
    )

    return response.json()["message"]["content"].strip()


def run():
    print("AI Smart Home \nTell me how you want to configure your lights\n(type exit to quit)")

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            break

        s = ask_ollama(user)
        print(s)
        
        match = re.search(r"\[(.*?),(.*?)\]", s)

        if match:       
            lightname, state = match.groups()

            if "Kitchen" == lightname:
                client.publish(TOPIC_Kitchen, state)
                print("Kitchen: "+ lightname + " " + state)

            elif "Cupboard" == lightname:
                client.publish(TOPIC_Cup, state)
                print("Cupboard: "+ lightname + " " + state)

            elif "Desk"== lightname:
                client.publish(TOPIC_Desk, state)
                print("Desk: "+ lightname + " " + state)

            else:
                print("nothing changed")

if __name__ == "__main__":
    run()