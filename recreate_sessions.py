import networkx as nx
import random


class SessionGraphConstructer:

    def __init__(self, kind="simple"):
        self.kind = kind

    def construct(self, session):
        # converts a session into directed graph
        if self.kind == "simple":
            graph = self.simple_session(session)
            return graph

    def simple_session(self, session):
        # simple session DiGraph, where an item is only connected to next item
        G = nx.DiGraph()
        n = len(session)
        for i in range(n-1):
            G.add_edge(session[i], session[i+1])
        
        return G
    
class Combiner:

    def __init__(self):
        pass

    def combine(self, sessions, n_groups=1, kind="random"):
        
        if kind == "random":
            graphs = self.random_split(sessions, n_groups)

        return graphs

    def random_split(self, sessions, n_groups):
        
        random.shuffle(sessions)
        groups = [sessions[i::n_groups] for i in range(n_groups)]

        graphs = []
        for group in groups:
            graph = nx.compose_all(group)
            graphs.append(graph)

        return graphs
        

def get_session_graphs(sessions):

    session_graphs = []
    constructer = SessionGraphConstructer("simple")

    for session in sessions:
        session_graph = constructer.construct(session)
        session_graphs.append(session_graph)

    return session_graphs

def combine_session_graphs(session_graphs):

    final_graph = nx.compose_all(session_graphs)
    return final_graph
    
    