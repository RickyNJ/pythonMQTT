import paho.mqtt.client as mqtt
import random
import time

framesPerSecond = 120
pointsPerFrame = 500
testRuns = 50

# Define the MQTT broker hostname and port number
broker_hostname = "localhost"
broker_port = 1883

# Define the topic to publish the message to
topic = "matten/3"

# Define the message to send
mes = ""

for i in range(0,1600):
    mes += (str(random.randint(0,pointsPerFrame))+ ',')

# Create a new MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker_hostname, broker_port)

start_time = time.time()

for i  in range(120):
# Publish the message to the topic
    client.publish(topic, mes)

end_time = time.time()

# Disconnect from the broker
client.disconnect()

elapsed_time = end_time - start_time
print("producer3: "+ str(elapsed_time))