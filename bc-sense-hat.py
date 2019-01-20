import paho.mqtt.subscribe as subscribe
from sense_hat import SenseHat

# Sense HAT
sense = SenseHat()

# Change this based on your devices connected to gateway
custom_names = {
    "fridge-monitoring:0": "Kitchen",
    "fridge-monitoring:1": "Bar",
    "fridge-monitoring:2": "Warehouse"
    }


def on_message_print(client, userdata, message):
    topic_parts = message.topic.split("/")

    # Message parser
    if (len(topic_parts) != 5) or (topic_parts[1] not in custom_names):
        return

    if (topic_parts[4] != "temperature"):
        return

    temperature =  float(message.payload)
    print(temperature)
    print(custom_names[topic_parts[1]] + ": " + message.payload.decode("ascii") + " °C")
    sense.show_message(custom_names[topic_parts[1]] + ": " + str(int(temperature)))

# Change hostname to reflect your setup
# If you run it on local computer use "localhost"
subscribe.callback(on_message_print, "#", hostname="localhost")

