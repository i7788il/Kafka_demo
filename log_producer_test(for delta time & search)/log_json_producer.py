# -*- coding: utf-8 -*
import threading
import logging
import time
import json
import random
import datetime
from kafka import KafkaConsumer, KafkaProducer



#test sets
status = ["WORKING","IDLE","MAINTAINING"]
ID = ["v1.1","v1.2","v2.1","v2.2","v2.3","v4.0"]
href = [
"http://156,65,595,654:9999",
"http://156,65,595,754:9999",
"http://156,65,595,854:9999",
"http://156,65,595,954:9999"
]

admin = ["root","USER1","USER2"]


class Producer(threading.Thread):
    daemon = True  #daemon = True: While the main thread stops, it won't check the status of sub thread and shutting down immediatly.
    def run(self):
        producer = KafkaProducer(bootstrap_servers=['9.11.112.245:9092'],
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        while True:
            t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sta_str=random.choice(status)
            ID_str=random.choice(ID)
            href_str=random.choice(href)
            user_str=random.choice(admin)
            producer.send('json_test', {u'status': sta_str, u'id': ID_str, u'href':href_str, u'user': user_str,u'time':t})
            #producer.send('test-logss', {u'status': sta_str, u'id': ID_str, u'href':href_str, u'user': user_str,u'time':t})
	    time.sleep(random.randint(15,20))


class Consumer(threading.Thread):
    daemon = True
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=['9.11.112.245:9092'],
                                 auto_offset_reset='latest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['json_test'])
        for message in consumer:
            print message



def main():
    threads = [
        Producer(),
        Consumer(),
    ]
    
    for t in threads:
        t.start()
    time.sleep(100)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()

