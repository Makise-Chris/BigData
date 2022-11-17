from kafka import KafkaProducer
import SpotifyGetData
import pickle
import time

spotipyGetData=SpotifyGetData.MySpotify()
producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic_artist = 'artists'
artists=spotipyGetData.artist_genre()
i=0
for artist in artists:
    i=i+1
    print(i)
    print(artist)
    print('-----------------------------')
    producer.send(topic_artist,pickle.dumps(artist))
    time.sleep(0.5)