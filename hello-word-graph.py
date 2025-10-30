#hello world graph

'''
what even is langraph?
It is a graph-based framework for building and executing complex workflows.

we will be building this graph:
start->node->end

'''



#understand and define the agentState structure

# create a simple node functions fto process and update state

#set up a basic langGraph structure

#compile and invoke a langGraph graph

#understand how data flows throuogh a single-node in langGraph




from typing import Dict, TypedDict
from langgraph.graph import StateGraph # framework that helps you design 
                                       #and manage the flow of tasks in your application using a graph.






class AgentState(TypedDict): # essentially a shared data struct keeping track of the info as app runs
    message : str #first input called message of type string


def greeting_node(state: AgentState) -> AgentState:
    #doc strings are what tell the ai agents what that function actually does 
    """ simple node that adds a greeting message to the state"""
    state['message'] = "hey" + state["message" + ", how is your day going?"]

    return state





graph = StateGraph(AgentState)

#graph is empty so lets add a node

graph.add_node("greeter", greetin_node)

#now we created the node ie the middle of the snadwich
#now we create a start and end point


graph.set_entry_point("greeter")# reference the ndoe tocreate and edge


graph.set_finish_point("greeter")

app = graph.compile()



from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))





