from kafka import KafkaProducer    
from kafka import KafkaConsumer   
from kafka import TopicPartition 
from kafka.errors import KafkaError 
import json
import time
import datetime


consumer = KafkaConsumer('json_test',bootstrap_servers=['9.11.112.245:9092'],auto_offset_reset='smallest')
 

def start():
    status = []
    user = []
    href = []
    ID = []
    timestamp = []

    for message in consumer:
        json_message = json.loads(message.value)  # extract the json message
	
        global g_status 
	status.append(json_message["status"])
	g_status = status
        global g_user
	user.append(json_message["user"])
	g_user = user
        global g_href 
	href.append(json_message["href"])
	g_href = href
        global g_id 
	ID.append(json_message["id"])
	g_id = ID
        global g_timestamp 
	timestamp.append(json_message["time"])
	g_timestamp = timestamp
	strr = "\n\tOffset range is -> "+str(message.offset-1)+"~"+str(message.offset)+"\n"
	print strr
	print "new message ->" ,json_message
	if len(status) >= 2:
		s1=judge_status()
		interval=status[len(status)-1]
		status = []
		status.append(interval)
		if s1==1:
			print "status is unchanged->"+interval
		else :
			print "status is changed to->"+interval
	if len(user) >= 2:
		u2=judge_user()
		interval=user[len(user)-1]
		user = []
		user.append(interval)
		if u2==1:
			print "user is unchanged->"+interval
		else :
			print "user is changed to->"+interval
	if len(href) >= 2:
		h3=judge_href()
		interval=href[len(href)-1]
		href = []
		href.append(interval)
		if h3==1:
			print "href is unchanged->"+interval
		else :
			print "href is changed to->"+interval
	if len(ID) >= 2:
		I4=judge_ID()
		interval=ID[len(ID)-1]
		ID = []
		ID.append(interval)
		if I4==1:
			print "id is unchanged->"+interval
		else :
			print "id is changed to->"+interval
	if len(timestamp) >= 2:
		t5=judge_timestamp()
		interval=timestamp[len(timestamp)-1]
		timestamp = []
		timestamp.append(interval)
		if t5:
			print "Time interval is->",t5


def judge_status():

	d1 = g_status[0]
	d2 = g_status[1]
		

	if d1 == d2:
		return 1
	else :
		return 2


def judge_user():
	
	d1 = g_user[0]
	d2 = g_user[1]
		

	if d1 == d2:
		return 1
	else :
		return 2

def judge_href():

	d1 = g_href[0]
	d2 = g_href[1]
		

	if d1 == d2:
		return 1
	else :
		return 2

def judge_ID():
	

	d1 = g_id[0]
	d2 = g_id[1]
		

	if d1 == d2:
		return 1
	else :
		return 2

def judge_timestamp():
	d1 = datetime.datetime.strptime(g_timestamp[0], "%Y-%m-%d %H:%M:%S")
	d2 = datetime.datetime.strptime(g_timestamp[1], "%Y-%m-%d %H:%M:%S")
	dt = d2 - d1
	return dt
	

if __name__ == '__main__':    
	start()   
	

