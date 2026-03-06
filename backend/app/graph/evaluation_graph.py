from langgraph.graph import StateGraph, END

from app.graph.state import HealthBotState
from app.graph.nodes.answer_evaluation_node import AnswerEvaluationNode


class EvaluationGraph:
    """
    LangGraph workflow responsible for evaluating the patient's answer.

    This graph is executed after the user submits their quiz answer.
    It evaluates the answer and returns a grade with an explanation.
    """

    def __init__(self) -> None:
        """
        Initialize and compile the evaluation workflow.
        """

        workflow_builder = StateGraph(HealthBotState)

        workflow_builder.add_node("evaluate", AnswerEvaluationNode())

        workflow_builder.set_entry_point("evaluate")

        workflow_builder.add_edge("evaluate", END)

        self.graph = workflow_builder.compile()

    def run_workflow(self, state: HealthBotState):
        """
        Execute the evaluation workflow.

        Args:
            state (HealthBotState): Current workflow state containing
            the quiz question, summary and user's answer.

        Returns:
            HealthBotState: Updated state including grade and explanation.
        """

        return self.graph.invoke(state)