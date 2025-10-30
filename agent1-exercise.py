#create a personalized compilement agent using langgraph
'''
input: {"name" : "Bob"}

output : "Bob, you're doing ana amazing job learning langgraph"


'''


from typing import Dict, TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    message : str


def compliment_node(state: AgentState) -> AgentState:
    state['message'] = state["message"] + "you are doing a great job learning langgraph"
    return state

graph = StateGraph(AgentState)
graph.add_node("complimenter", compliment_node)
graph.set_entry_point("complimenter")
graph.set_finish_point("complimenter")

app = graph.compile()

from IPython.display import Image, display

png_bytes = app.get_graph().draw_mermaid_png()
print(type(png_bytes), len(png_bytes))

display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({"message" : "bob"})
result["message"]