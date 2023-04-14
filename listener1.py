import paho.mqtt.client as mqtt

# Define the MQTT broker and topic to subscribe to
broker_address = "localhost"
topic = "matten/1"

# Define a variable to keep track of the message count
message_count = 0

# Define a callback function to handle incoming messages
def on_message(client, userdata, message):
    global message_count
    message_count += 1

# Create an MQTT client and connect to the broker
client = mqtt.Client()
client.connect(broker_address)

# Subscribe to the topic and start listening for messages
client.subscribe(topic)
client.on_message = on_message
client.loop_start()

# Wait for the user to stop the application
input("Press Enter to stop the application...\n")

# Disconnect the client and print the message count
client.loop_stop()
client.disconnect()
print("Messages received:", message_count)
