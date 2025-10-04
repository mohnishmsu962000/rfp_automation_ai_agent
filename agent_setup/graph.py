from langgraph.graph import StateGraph, START, END
from models.schemas import State
from agent_setup.nodes.generator import generator_node
from agent_setup.nodes.researcher import researcher_node
from agent_setup.nodes.extractor import extractor_node
from agent_setup.nodes.supervisor import supervisor_node


graph = StateGraph(State)

graph.add_node('supervisor', supervisor_node)
graph.add_node('extractor', extractor_node)
graph.add_node('researcher', researcher_node)
graph.add_node('generator', generator_node)

def supervisor_logic(state):
    if state['questions'] and state['questions'][0]['answer']:
        return 'finish'
    elif state['questions'] and state['questions'][0]['chunks']:
        return 'generator'
    elif state['questions']:
        return 'researcher'
    else:
        return 'extractor'
        

graph.add_conditional_edges(
    'supervisor',
    supervisor_logic,
    {
        'extractor': 'extractor',
        'researcher': 'researcher',
        'generator': 'generator',
        'finish': END
    }
)

graph.add_edge(START, 'supervisor')
graph.add_edge('extractor', 'supervisor')
graph.add_edge('researcher', 'supervisor')
graph.add_edge('generator', 'supervisor')



workflow = graph.compile()