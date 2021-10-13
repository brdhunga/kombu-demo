import kombu
import os 
from kombu import serialization
import json 


for directory in ["data_in"]:
    if not os.path.exists(directory):
        os.mkdir(directory)


kombu_conn = kombu.Connection(
    'filesystem://', transport_options={
        'data_folder_in': 'data_in', 'data_folder_out': 'data_in'
    }
)


serialization.register(
    'my_json', json.dumps, json.loads,
    content_type='application/json',
    content_encoding='utf-8',
)

test_queue = kombu.Queue('test', routing_key='test')
