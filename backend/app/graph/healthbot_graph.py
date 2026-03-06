from langgraph.graph import START, END, StateGraph

from app.graph.state import HealthBotState
from app.graph.nodes.tavily_search_node import TavilySearchNode
from app.graph.nodes.topic_node import TopicNode
from app.graph.nodes.summarizer_node import SummarizerNode
from app.graph.nodes.present_summary_node import PresentSummaryNode
from app.graph.nodes.ready_for_quiz_node import ReadyForQuizNode
from app.graph.nodes.quiz_generation_node import QuizGenerationNode
from app.graph.nodes.answer_evaluation_node import AnswerEvaluationNode
from app.graph.nodes.new_topic_node import NewTopicNode
from app.graph.nodes.session_control_node import SessionControlNode

class HealthBotGraph:
    """
    Workflow responsible for generating explanations and quiz questions.

    The workflow includes:
    - Asking the patient for a health topic
    - Searching medical information
    - Generating a patient-friendly summary
    - Generating a quiz question
    - Evaluating the patient's response
    """

    def __init__(self):
        workflow_builder = StateGraph(HealthBotState)

        # Nodes
        workflow_builder.add_node("topic", TopicNode())
        workflow_builder.add_node("tavily_search", TavilySearchNode())
        workflow_builder.add_node("summary", SummarizerNode())
        workflow_builder.add_node("present_summary", PresentSummaryNode())
        workflow_builder.add_node("ready_for_quiz", ReadyForQuizNode())
        workflow_builder.add_node("quiz", QuizGenerationNode())
        workflow_builder.add_node("evaluate", AnswerEvaluationNode())
        workflow_builder.add_node("new_topic", NewTopicNode())
        workflow_builder.add_node("reset", SessionControlNode())

        # Entry point
        workflow_builder.add_edge(START, "topic")

        # Main workflow
        workflow_builder.add_edge("topic", "tavily_search")
        workflow_builder.add_edge("tavily_search", "summary")

        workflow_builder.add_edge("summary", "present_summary")
        workflow_builder.add_edge("present_summary", "ready_for_quiz")
        workflow_builder.add_edge("ready_for_quiz", "quiz")
        workflow_builder.add_edge("quiz", "evaluate")
        workflow_builder.add_edge("evaluate", "new_topic")

        # Conditional decision
        workflow_builder.add_conditional_edges(
            "new_topic",
            should_continue,
            {
                "reset": "reset",
                "end": END,
            },
        )

        workflow_builder.add_edge("reset", "topic")

        self.graph = workflow_builder.compile()

    def run_workflow(self, state: HealthBotState):
        """
        Execute the HealthBot workflow.

        Args:
            state (HealthBotState): Initial workflow state.

        Returns:
            HealthBotState: Final state after workflow execution.
        """
        return self.graph.invoke(state)

    def visualize(self):
        """
        Generate a PNG visualization of the LangGraph workflow.
        """

        graph_png = self.graph.get_graph().draw_mermaid_png()

        with open("healthbot_graph.png", "wb") as f:
            f.write(graph_png)



def should_continue(state: HealthBotState) -> str:
    """
    Determine whether the session should continue with a new topic
    or end the workflow.

    Args:
        state (HealthBotState): Current workflow state.

    Returns:
        str: The next node key ("reset" or "end").
    """

    if state["session_active"]:
        return "reset"

    return "end"



if __name__ == "__main__":

    graph = HealthBotGraph()

    initial_state = {
        "topic": "What is paracetamol?",
        "patient_answer": "It reduces pain and fever"
    }

    result = graph.run_workflow(initial_state)

    print(result)