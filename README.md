# Kafka_demo

## [Ⅰ. kafka_presure_test](https://github.ibm.com/huangjy/Kafka_demo/tree/master/kafka_presure_test)
**This module is for user to test the performance of your kafka cluster.<br>** 
### producer
&nbsp;&nbsp;&nbsp;&nbsp;As you execute the **[presure_test_producer.py](https://github.ibm.com/huangjy/Kafka_demo/blob/master/kafka_presure_test/presure_test_producer.py)**, it will generate 300 key-value pairs and send to topic ("presure_test1~10", please create them in advance) every 60s automatically. Contents in each value is like the following:
```
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
```
<br><br>
### consumer
&nbsp;&nbsp;&nbsp;&nbsp;Using the **[presure_test_consumer.py.template](https://github.ibm.com/huangjy/Kafka_demo/blob/master/kafka_presure_test/presure_test_consumer.py.template)** to moniter every topic status. Also noteworthy there are always four messages in each topic will be persistanced in consumer's ram. It's for testing the persistance and extensibility.
```	
consumer.seek(TopicPartition('presure_test',0),i-4)
	for message in consumer:
		json_message = json.loads(message.value)
		array.append(json_message)
		if (len(array) == 5):
			array = array[1:]
			print array[3]
```

## <br><br>[Ⅱ.log_producer_test(for delta time & search)](https://github.ibm.com/huangjy/Kafka_demo/tree/master/log_producer_test(for%20delta%20time%20%26%20search))
**This module is for user to compare each of messages and query messages in specific quantity or time interval .<br>** 

### producer
&nbsp;&nbsp;&nbsp;&nbsp; As you execute the **[log_json_producer.py](https://github.ibm.com/huangjy/Kafka_demo/blob/master/log_producer_test(for%20delta%20time%20%26%20search)/log_json_producer.py)**, it will generate message in json format in random time interval, then send to topic "json_test" automatically. Contents in each value is like the following:
```
{u'status': u'MAINTAINING', u'user': u'USER2', u'href': u'http://156,65,595,954:9999', u'id': u'v2.2', u'time': u'2018-07-02 03:05:30'}

```
<br><br>
### consumer1
&nbsp;&nbsp;&nbsp;&nbsp;Using the **[message_delta_consumer.py](https://github.ibm.com/huangjy/Kafka_demo/blob/master/log_producer_test(for%20delta%20time%20%26%20search)/message_delta_consumer.py)** to compare the difference between each message in specific topic. It's a real time monitor.
```	
Offset range is -> 4~5

new message -> {u'status': u'MAINTAINING', u'user': u'USER2', u'href': u'http://156,65,595,854:9999', u'id': u'v4.0', u'time': u'2018-07-02 03:05:14'}
status is unchanged->MAINTAINING
user is unchanged->USER2
href is changed to->http://156,65,595,854:9999
id is changed to->v4.0
Time interval is-> 0:01:38

	Offset range is -> 5~6

new message -> {u'status': u'MAINTAINING', u'user': u'USER2', u'href': u'http://156,65,595,954:9999', u'id': u'v2.2', u'time': u'2018-07-02 03:05:30'}
status is unchanged->MAINTAINING
user is unchanged->USER2
href is changed to->http://156,65,595,954:9999
id is changed to->v2.2
Time interval is-> 0:00:16

```
<br><br>
### consumer2
&nbsp;&nbsp;&nbsp;&nbsp;Using the **[search_by_amount&timeperiod_consumer.py](https://github.ibm.com/huangjy/Kafka_demo/blob/master/log_producer_test(for%20delta%20time%20%26%20search)/search_by_amount%26timeperiod_consumer.py)** to query kafka messages in specific quantity or time interval.
<br><br>
#### By quantity

```
Chose an operation:

1.Querrying an amount of messages before the latest message.
2.Querrying an amount of messages in a specified time period.
=>1        

Please input an amount of messages before the current message offset to querry: 
(the latest offset is 6)
=>2
offset =  5 
{u'status': u'MAINTAINING', u'user': u'USER2', u'href': u'http://156,65,595,854:9999', u'id': u'v4.0', u'time': u'2018-07-02 03:05:14'} 

offset =  6 
{u'status': u'MAINTAINING', u'user': u'USER2', u'href': u'http://156,65,595,954:9999', u'id': u'v2.2', u'time': u'2018-07-02 03:05:30'} 

```

<br><br>
#### By time interval

```
Chose an operation:

1.Querrying an amount of messages before the latest message.
2.Querrying an amount of messages in a specified time period.
=>2

Please input a time period (in seconds) for searching the message to querry: 
(1 day = 86400 s, 1 hr = 3600 s)
=>7200


time period:  2:00:00 

offset =  0 
{u'status': u'WORKING', u'user': u'USER2', u'href': u'http://156,65,595,854:9999', u'id': u'v1.1', u'time': u'2018-07-02 02:58:10'} 

offset =  1 
{u'status': u'WORKING', u'user': u'root', u'href': u'http://156,65,595,954:9999', u'id': u'v2.1', u'time': u'2018-07-02 03:02:40'} 

offset =  2 
{u'status': u'IDLE', u'user': u'root', u'href': u'http://156,65,595,954:9999', u'id': u'v1.1', u'time': u'2018-07-02 03:02:57'} 

offset =  3 
{u'status': u'WORKING', u'user': u'root', u'href': u'http://156,65,595,654:9999', u'id': u'v2.1', u'time': u'2018-07-02 03:03:16'} 

offset =  4 
{u'status': u'MAINTAINING', u'user': u'USER2', u'href': u'http://156,65,595,754:9999', u'id': u'v2.1', u'time': u'2018-07-02 03:03:36'} 

offset =  5 
{u'status': u'MAINTAINING', u'user': u'USER2', u'href': u'http://156,65,595,854:9999', u'id': u'v4.0', u'time': u'2018-07-02 03:05:14'} 

offset =  6 
{u'status': u'MAINTAINING', u'user': u'USER2', u'href': u'http://156,65,595,954:9999', u'id': u'v2.2', u'time': u'2018-07-02 03:05:30'} 

```
