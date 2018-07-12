from kafka import KafkaProducer    
from kafka import KafkaConsumer    
from kafka.errors import KafkaError
import random    
import time
import datetime
import json



href = [
"http://156,65,595,54:9999",
"http://156,65,595,154:9999",
"http://156,65,595,254:9999",
"http://156,65,595,354:9999",
"http://156,65,595,454:9999",
"http://156,65,595,554:9999",
"http://156,65,595,654:9999",
"http://156,65,595,754:9999",
"http://156,65,595,854:9999",
"http://156,65,595,954:9999",
""
]



def main():    
	dict = {}
	for p in range(0,300):
		producer = KafkaProducer(bootstrap_servers=['9.11.112.245:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))
	
		for i in range(0,300):
			log = {
			"1":random.choice(href),
			"2":random.choice(href),
			"3":random.choice(href),
			"4":random.choice(href),
			"5":random.choice(href),
			"6":random.choice(href),
			"7":random.choice(href),
			"8":random.choice(href),
			"9":random.choice(href),
			"10":random.choice(href)
			}

			key = 'key'+str(i)
			dict[key]=log
		t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')		
		dict['time'] = t
		for i in range(1,11):
			producer.send("presure_test"+str(i),dict)

		print dict
		time.sleep(10)

	
if __name__ == '__main__':    
    main() 
