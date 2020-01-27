from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.structs import TopicPartition
import time

bootstrap_servers = []
class OperateKafka:
    def init(self,bootstrap_servers,topic):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic

"""生产者"""
def produce(self):
    producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)
    for i in range(4):
        msg = "msg%d" %i
        producer.send(self.topic,key=str(i),value=msg)
    producer.close()

"""一个消费者消费一个topic"""
def consume(self):
    consumer = KafkaConsumer(self.topic,bootstrap_servers=self.bootstrap_servers)
    print (consumer.partitions_for_topic(self.topic))  #获取test主题的分区信息
    print (consumer.topics() ) #获取主题列表
    print (consumer.subscription() ) #获取当前消费者订阅的主题
    print (consumer.assignment() ) #获取当前消费者topic、分区信息
    print (consumer.beginning_offsets(consumer.assignment())) #获取当前消费者可消费的偏移量
    consumer.seek(TopicPartition(topic=self.topic, partition=0), 1)  #重置偏移量，从第1个偏移量消费
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s"
        % (message.topic,message.partition,message.offset, message.key,message.value))

"""一个消费者订阅多个topic """
def consume2(self):
    consumer = KafkaConsumer(bootstrap_servers=['192.168.124.201:9092'])
    consumer.subscribe(topics=('TEST','TEST2'))  #订阅要消费的主题
    print (consumer.topics())
    print (consumer.position(TopicPartition(topic='TEST', partition=0))) #获取当前主题的最新偏移量
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                      message.offset, message.key,
                                      message.value))
"""消费者(手动拉取消息)"""
def consume3(self):
    consumer = KafkaConsumer(group_id="mygroup",max_poll_records=3,bootstrap_servers=['192.168.124.201:9092'])
    consumer.subscribe(topics=('TEST','TEST2'))
    while True:
            message = consumer.poll(timeout_ms=5)   #从kafka获取消息
            if message:
                print (message)
                time.sleep(1)
def main():
    bootstrap_servers = ['192.168.124.201:9092']
    topic = "TEST"
    operateKafka = OperateKafka(bootstrap_servers,topic)
    #operateKafka.produce()
    #operateKafka.consume()
    #operateKafka.consume2()
    #operateKafka.consume3()


main()