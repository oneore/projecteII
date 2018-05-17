import numpy as np
songs = ['new_rules.txt','shape_of_you.txt','idgaf.txt','havana.txt'] #nuestra lista de canciones

def distance(pt_1, pt_2):
    print(pt_1)
    print(pt_2)
    pt_1 = np.array((float(pt_1[0]), float(pt_1[1])))
    pt_2 = np.array((float(pt_2[0]), float(pt_2[1])))
    return np.linalg.norm(pt_1-pt_2)

def closest_node(node, nodes):
    pt = []
    dist = 9999999
    for n in nodes:
        n=eval(n)
        if distance(node, n) <= dist:
            dist = distance(node, n)
            pt = n
    return pt, dist
