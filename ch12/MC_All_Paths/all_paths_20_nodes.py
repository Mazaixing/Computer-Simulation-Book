def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
   # if start not in graph:
     #   return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
    

graph = {
    "1": ("2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "19"),
    "2": ("1", "3", "4", "6", "7", "8", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"),
    "3": ("1", "2", "5", "7", "8", "9", "11", "12", "13", "14", "15", "16", "17", "19", "20"),
    "4": ("1", "2", "5", "6", "7", "8", "10", "11", "12", "14", "15", "17", "18", "19", "20"),
    "5": ("1", "3", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"),
    "6": ("1", "2", "4", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"),
    "7": ("1", "2", "3", "4", "6", "8", "9", "10", "11", "12", "13", "16", "17", "18", "19", "20"),
    "8": ("1", "2", "3", "4", "5", "6", "7", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19", "20"),
    "9": ("1", "3", "5", "6", "7", "8", "10", "11", "12", "13", "14", "15", "16", "17", "19", "20"),
    "10": ("1", "2", "4", "5", "6", "7", "8", "9", "11", "12", "13", "16", "17", "18", "19", "20"),
    "11": ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "13", "15", "16", "17", "18", "20"),
    "12": ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "14", "15", "16", "18", "19", "20"),
    "13": ("1", "2", "3", "5", "6", "7", "8", "9", "10", "11", "14", "15", "16", "17", "18", "19"),
    "14": ("1", "2", "3", "4", "5", "6", "8", "9", "12", "13", "15", "16", "17", "18", "19"),
    "15": ("1", "2", "3", "4", "5", "6", "8", "9", "11", "12", "13", "14", "16", "17", "18", "19"),
    "16": ("1", "2", "3", "5", "6", "7", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19"),
    "17": ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "13", "14", "15", "16", "18", "19", "20"),
    "18": ("2", "3", "5", "6", "7", "8", "10", "11", "12", "13", "14", "15", "16", "17", "19", "20"),
    "19": ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12", "13", "14", "15", "16", "17", "18", "20"),
    "20": ("1", "5", "6", "7", "8", "9", "10", "11", "12", "17", "18", "19"),
}

paths = find_all_paths(graph, "1", "20")

print("Number of Paths = ", len(paths))
