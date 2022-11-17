from kafka import KafkaConsumer

topic_artist = 'artists'

consumer = KafkaConsumer(topic_artist, bootstrap_servers=["localhost:9092"])

for msg in consumer:
    print(msg)