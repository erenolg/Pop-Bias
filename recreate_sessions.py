import networkx as nx
import random


class SessionDAGConstructor:

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
        G.session = session
        return G
    
class Walker:

    def __init__(self, G: nx.DiGraph):
        self.G = G

    def sample_walk(self, walk_length, source_node):
        
        walk = [source_node]
        for _ in range(walk_length-1):
            candidates = list(self.G.successors(walk[-1]))

            if len(candidates) == 0:
                break
            else:
                next_node = random.choice(candidates)
                walk.append(next_node)
        
        return walk

class CoPurchaseGraph(nx.DiGraph):

    def __init__(self, graph, sessions):
        super().__init__(graph)
        self.sessions = sessions

    def walk(self, kind="random"):
        
        if kind == "random":
            walks = self.random_walk()
        
        return walks
            
    def random_walk(self, walk_length=None):

        walker = Walker(self)
        walks = []

        for session in self.sessions:

            source = session[0]
            L = walk_length or len(session)
            walk = walker.sample_walk(L, source)
            walks.append(walk)
        
        return walks

    
class Combiner:

    def __init__(self):
        pass

    def combine(self, session_dags, n_groups=1, kind="random"):
        
        if kind == "random":
            graphs = self.random_split(session_dags, n_groups)

        return graphs

    def random_split(self, session_dags, n_groups):
        
        random.shuffle(session_dags)
        chunk_size = len(session_dags) // n_groups
        groups = [session_dags[i*chunk_size:(i+1)*chunk_size] for i in range(n_groups)]

        graphs = []
        for group in groups:
            sessions = [dag.session for dag in group]
            graph = nx.compose_all(group)
            graph = CoPurchaseGraph(graph, sessions)
            graphs.append(graph)

        return graphs
        

def get_session_dags(sessions, kind="simple"):

    session_dags = []
    constructer = SessionDAGConstructor(kind)

    for session in sessions:
        session_dag = constructer.construct(session)
        session_dags.append(session_dag)

    return session_dags

    