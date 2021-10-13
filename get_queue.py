import kombu

from connection import kombu_conn, test_queue


kombu_conn.connect()
client = kombu_conn.get_manager()

import pdb; pdb.set_trace()

# with kombu_conn as conn:
#     with conn.default_channel as channel:
#         print(test_queue.get('name'))


