from app.graph.healthbot_graph import HealthBotGraph
import asyncio



async def main():
    """
    Run HealthBot in interactive CLI mode.
    """

    graph = HealthBotGraph()

    print("\nHealthBot - AI Patient Education\n")

    while True:

        # Ask topic
        topic = input("\nWhat health topic would you like to learn about?\n> ")

        state = {
            "topic": topic,
            "continue_active": True
        }

        # Run workflow
        result = graph.run_workflow(state)

        print(result)

        summary = result["summary"]
        quiz = result["quiz_question"]

        if summary:
            print("\nSummary:\n")
            print(summary)

        if quiz:
            print("\nQuiz:\n")
            print(quiz)

        # Ask user answer
        answer = input("\nYour answer:\n> ")

        result["patient_answer"] = answer

        # Evaluate answer
        result = graph.run_workflow(result)

        explanation = result["explanation"]

        if explanation:
            print("\nEvaluation:\n")
            print(explanation)

        # Continue session?
        cont = input("\nLearn another topic? (yes/no)\n> ")

        if cont.lower() not in ["yes", "y"]:
            print("\nSession ended. Goodbye!\n")
            break

        print("\n----------------------------------------")


if __name__ == "__main__":
    main()