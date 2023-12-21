from kafka import KafkaConsumer
from concurrent.futures import ThreadPoolExecutor

def consume_from_kafka(topic):
    kafka_broker = "localhost:9092"
    consumer = KafkaConsumer(topic, bootstrap_servers=kafka_broker)

    for message in consumer:
        print(f"Received message from topic {topic}: {message.value.decode('utf-8')}")

    consumer.close()

if __name__ == "__main__":
    kafka_topics = ["turbine1", "turbine2", "turbine3", "turbine4", "turbine5"]

    with ThreadPoolExecutor(max_workers=len(kafka_topics)) as executor:
        executor.map(consume_from_kafka, kafka_topics)