from json import loads
from kafka import KafkaConsumer
from pymongo import MongoClient

my_consumer = KafkaConsumer(
    "rand_numbers_3",#"rand_numbers",
    bootstrap_servers = '192.168.12.101:9092',
    auto_offset_reset = 'earliest',
    group_id = 'counters',
    value_deserializer = lambda x: loads(x.decode('utf-8'))
)
print("starting consumer")
#print(my_consumer.topics())
#my_consumer.subscribe(topics=my_consumer.topics())

for msg in my_consumer:
    msg = msg.value
    print(msg)
