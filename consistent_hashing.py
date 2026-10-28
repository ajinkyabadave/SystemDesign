
import random


def hash_function(key):
    # hash the key to a number between 0 and 2**5 - 1
    return (hash(key) % (2**5)) -1
servers = [
    "server1",
    "server2",
    "server3",
]

hash_space = [None] * 2**5
data_array  = [1, 32, 3, 4, 51, 6, 70, 811]
data_server_map = {}

def add_server(server: str):
    servers.append(server)
    server_index = map_server_to_hash_space(server)

    # find the next server
    i = (server_index + 1) % len(hash_space)
    while hash_space[i] is None:
        i = (i + 1) % len(hash_space)

    next_server = hash_space[i]

    # find all the data that is mapped to the next server and reassign them to the new server
    for i in data_server_map:
        if data_server_map[i] == next_server and hash_function(i) <= server_index:
            data_server_map[i] = server


def remove_server(server: str):
    servers.remove(server)
    # remove the server from the hash space
    hash_space[hash_function(server)] = None

def map_server_to_hash_space(server: str) -> int:
    # get all indices that are None
    free_indices = [i for i, x in enumerate(hash_space) if x is None]

    #choose one of the free indices randomly
    random_index = random.choice(free_indices)
    hash_space[random_index] = server
    return random_index

def assign_data_to_servers():
    for i in data_array:
        server_index = hash_function(i)
        #find the next non None index
        while hash_space[server_index] is None:
            server_index += 1

        data_server_map[i] = hash_space[server_index]
        

def add_data(data: int):
    data_array.append(data)
    server_index = hash_function(data)
    #find the next non None index
    while hash_space[server_index] is None:
        server_index += 1

    data_server_map[data] = hash_space[server_index]

def init():
   for server in servers:
       map_server_to_hash_space(server)

   assign_data_to_servers()


init()
print(hash_space)
print(data_server_map)

add_server("server4")
print(hash_space)
print(data_server_map)