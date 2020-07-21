import pika
import time
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


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
