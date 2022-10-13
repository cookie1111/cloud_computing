from time import sleep
from json import dumps
from kafka import KafkaProducer
from random import randint, seed

# port through which producer clusters metadata this port is not mandatory since its the default
bootstrap_servers = ['192.168.12.101:9092']
# just a function to serialize the data befor sending it off
value_serializer = lambda x: dumps(x).encode('utf-8')

my_producer = KafkaProducer(
    bootstrap_servers = bootstrap_servers,
    value_serializer = value_serializer,
    #partitioner = lambda key_bytes, all_partition, available_partition: 0
)
seed(2022)
if __name__ == '__main__':
    while True:
        my_data = {'num':randint(0,501)}
        print(my_data)
        #my_producer.send('rand_numbers', value = my_data) # one partition
        my_producer.send('rand_numbers_3', value = my_data) # 2 partition sends to random partition each time
        #my_producer.send('rand_numbers_2', value = my_data) # we have added the partitioner
        sleep(5)