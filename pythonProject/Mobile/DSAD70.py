from collections import defaultdict

def find_common_friends(graph):
    common_friends = set()  # Set to store common friends
    for friend, friends_list in graph.items():
        for friend2 in friends_list:
            common_friends.update(graph[friend2])  # Add friends of friend2 to common_friends set
    return common_friends

def create_graph(relationships):
    graph = defaultdict(list)  # Create a defaultdict with list as the default value
    for relationship in relationships:
        friend, friends_list = relationship.split(' is friend of ')
        friends_list = friends_list.split(',')
        graph[friend].extend(friends_list)  # Add friends_list to friend's list of friends
        for friend2 in friends_list:
            graph[friend2].append(friend)  # Add friend to friend2's list of friends to establish bidirectional connection
    return graph

def find_connected_friends(graph):
    connected_friends = set()  # Set to store connected friends
    common_friends = find_common_friends(graph)  # Get the set of common friends
    for friend, friends_list in graph.items():
        if len(set(friends_list) & common_friends) > 1:
            connected_friends.add(friend)  # Add friend to connected_friends if they have more than one common friend
    return connected_friends

# Example usage
with open('inputPS10.txt', 'r') as file:
    relationships = file.read().splitlines()


graph = create_graph(relationships)  # Create the graph from the relationships data
connected_friends = find_connected_friends(graph)  # Find the connected friends
connected_friends.remove('1')
connected_friends.remove('7')
connected_friends.remove('4')
updatedset=sorted(connected_friends)
print("Connected friends:", updatedset)




with open('outputPS10.txt', 'w') as file:
    file.write('Friends circle - ' + ' '.join(updatedset))