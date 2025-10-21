import networkx as nx


class SessionGraphConstructer:

    def __init__(self, kind="simple"):
        self.kind = kind

    def construct(self, session):
        if self.kind == "simple":
            graph = self.simple_session(session)
            return graph

    def simple_session(self, session):
        G = nx.DiGraph()
        n = len(session)
        for i in range(n-1):
            G.add_edge(session[i], session[i+1])
        
        return G

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
    
    