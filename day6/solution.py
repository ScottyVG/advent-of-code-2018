from collections import Counter
'''
Using only the Manhattan distance, 
    determine the area around each coordinate by counting the number of integer X,Y locations 
    that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. 
'''
points = {chr(i+65): p
          for i, p in enumerate([(int(p[0]), int(p[1]))
                                 for line in open('input.txt').readlines()
                                 for p in [line.split(', ')]])}
max_dim = max(max(p[0] for p in points.values()), max(p[1] for p in points.values()))
manhattan_distance = lambda x0, y0, x1, y1, char: (abs(x0 - x1) + abs(y0 - y1), char)
safe_zone = 0
graph = {}
infinites = set()

for y in range(max_dim+1):
    for x in range(max_dim+1):
        m_dists = sorted([manhattan_distance(x, y, p[0], p[1], key) for key, p in points.items()])
        if sum(d[0] for d in m_dists) < 10000:
            safe_zone += 1
        graph[x,y] = '.' if m_dists[0][0] == m_dists[1][0] else m_dists[0][1]
        if x == 0 or y == 0 or x == max_dim or y == max_dim:
            infinites.add(graph[x,y])

for y in range(max_dim+1):
    for x in range(max_dim+1):
        print(graph[x,y], end='')
    print()

print(Counter(x for x in graph.values() if x not in infinites))

'''
What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?
'''

print(safe_zone)
