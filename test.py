import csv

def loadData(filename):
    csv_data = []
    with open(f'./large/{filename}.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            csv_data.append(row)
    return csv_data

def makeGraph():
    movies_csv = loadData("movies")
    people_csv = loadData("people")
    stars_csv = loadData("stars")
    
    moviesDict = {}
    for row in movies_csv:
        id,name = row[0],row[1]
        moviesDict[id] = name

    peopleDict = {}
    for row in people_csv:
        id,name = row[0],row[1]
        peopleDict[id] = name

    dict = {}
    for row in stars_csv:
        star,movie = row[0],row[1]
        if movie not in dict.keys():
            dict[movie] = []
        dict[movie].append(star)
    
    graph = {}
    for item in dict.values():
        for star in item:
            for star2 in item:
                if star != star2:
                    if star not in graph.keys():
                        graph[star] = []
                    graph[star].append(star2)
    print(graph)
    return graph

def shortestPath(num1, num2, graph):
    queue = []
    queue.append([num1,0])
    vis = {}
    ans = -1
    vis[num1] = 1
    while queue:
        node = queue.pop()
        actor,steps = node[0],node[1]
        print(actor)
        for item in graph[actor]:
            if item not in vis.keys():
                vis[item] = 1
                queue.append([item,steps+1])
                if item == num2:
                    return steps+1
    return ans

def main():
    graph = makeGraph()
    actor1 = (input("enter the id of first actor")).strip()
    actor2 = (input("enter the id of second actor")).strip()
    print(actor1,actor2)
    print(shortestPath(actor1,actor2,graph))

if __name__ == '__main__':
    main()