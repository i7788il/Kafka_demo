from kafka import KafkaProducer    
from kafka import KafkaConsumer   
from kafka import TopicPartition 
from kafka.errors import KafkaError 
import json
import time
import datetime



consumer = KafkaConsumer(bootstrap_servers=['9.11.112.245:9092'])

def amount_search():
	#array = []	
	consumer.assign([TopicPartition('json_test',0)])
	i = consumer.position(TopicPartition('json_test',0))
	amount = raw_input("\nPlease input an amount of messages before the current message offset to querry: \n(the latest offset is "+str(i-1)+")\n=>") 
	consumer.seek(TopicPartition('json_test',0),i-int(amount))

	for message in consumer:
		json_message = json.loads(message.value)
		print 'offset = ',message.offset,'\n',json_message ,'\n'
		if message.offset == i-1:
			time.sleep(5)
			break

def time_search():
	times = raw_input("\nPlease input a time period (in seconds) for searching the message to querry: \n(1 day = 86400 s, 1 hr = 3600 s)\n=>")
	consumer.assign([TopicPartition('json_test',0)])
	consumer.seek(TopicPartition('json_test',0),0)
	t = datetime.datetime.now()
	print '\n\ntime period: ',datetime.timedelta(seconds=int(times)),'\n'
	for message in consumer:
		json_message = json.loads(message.value)
		json_message_time = datetime.datetime.strptime(json_message['time'], "%Y-%m-%d %H:%M:%S")		
		
		if t-json_message_time < datetime.timedelta(seconds=int(times)):
			print 'offset = ',message.offset,'\n',json_message ,'\n'
	 		
		
def select():
	choice = input("\nChose an operation:\n\n1.Querrying an amount of messages before the latest message.\n2.Querrying an amount of messages in a specified time period.\n=>")
	if choice == 1:
		amount_search()
	if choice == 2:
		time_search()


if __name__ == '__main__':    
	select()   
	

