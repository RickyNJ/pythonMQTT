import threading
import time
import random
import paho.mqtt.client as mqtt
from matplotlib import pyplot as plt

def loop1():
    for i in range(framesPerSecond):
        # client1.connect(broker_hostname, broker_port)
        client1.publish(topic1, mes)
        time.sleep(0.005)

        # client1.disconnect()

def loop2():
    for i in range(framesPerSecond):
        # client2.connect(broker_hostname, broker_port)
        client2.publish(topic2, mes)
        time.sleep(0.005)

        # client2.disconnect()

def loop3():
    for i in range(framesPerSecond):
        # client3.connect(broker_hostname, broker_port)
        client3.publish(topic3, mes)
        time.sleep(0.005)

        # client3.disconnect()

def loop4():
    for i in range(framesPerSecond):
        # client4.connect(broker_hostname, broker_port)
        client4.publish(topic4, mes)
        time.sleep(0.005)

        # client4.disconnect()


#!###########################
#! Plaats hier je test parameters!
#Aantal berichten die per testrun worden verstuurd
framesPerSecond = 120

#Aantal test runs
testRuns = 100

#De drempel waarde van tijd waar een test run niet boven mag liggen
drempelwaarde = 0.04

#!###########################

times = []
timesOverLimit = 0
sum = 0

mes = ""
for i in range(0,1600):
    mes += (str(random.randint(0,500))+ ',')


# Define the MQTT broker hostname and port number
broker_hostname = "localhost"
broker_port = 1883

# Define the topic to publish the message to
topic1 = "matten/1"
topic2 = "matten/2"
topic3 = "matten/3"
topic4 = "matten/4"

# Create a new MQTT client instance
client1 = mqtt.Client()
client2 = mqtt.Client()
client3 = mqtt.Client()
client4 = mqtt.Client()

# Connect to the broker
client1.connect(broker_hostname, broker_port)
client2.connect(broker_hostname, broker_port)
client3.connect(broker_hostname, broker_port)
client4.connect(broker_hostname, broker_port)



for i in range(testRuns):
    start_time = time.time()

    t1 = threading.Thread(target=loop1)
    t2 = threading.Thread(target=loop2)
    t3 = threading.Thread(target=loop3)
    t4 = threading.Thread(target=loop4)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()   

    end_time = time.time()
    elapsed = end_time - start_time
    print(elapsed)
    times.append(elapsed)
    

for ele in times:
    if ele > drempelwaarde:
        timesOverLimit +=1
    sum += ele
res = sum / testRuns
print(str(timesOverLimit)+ " keer over drempelwaarde.")

fig, ax = plt.subplots()
line = ax.plot(times)
ax.axhline(y=drempelwaarde, color='r')
ax.set_ylim(0,drempelwaarde*2)
plt.show()