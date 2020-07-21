import time
import pika
import requests


## wait for 
while True:
    try:
        response = requests.get('http://rabbitmq:15672', auth=requests.auth.HTTPBasicAuth('guest', 'guest'))
        if response.status_code == 200:
            print(response.status_code)
            break
    except Exception as e:
        print(e)
        time.sleep(3)


connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='hello')

num = 0
while 1:
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World! {}'.format(num))
    num += 1
    print(" [x] Sent 'Hello World!'")

connection.close()
