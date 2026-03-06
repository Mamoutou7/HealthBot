from app.graph.healthbot_graph import HealthBotGraph
from langgraph.graph import END


def run_chat():

    graph = HealthBotGraph()

    state = {}

    print("\nHealthBot - AI Patient Education\n")

    config = {"configurable": {"thread_id": "healthbot-cli"}}

    events = graph.graph.stream(state, config)

    for event in events:

        for node, output in event.items():

            if node == END:
                print("\nSession finished.")
                return

            if isinstance(output, dict):

                if "topic" in output and output["topic"]:
                    print(f"\nTopic: {output['topic']}")

                if "summary" in output:
                    print("\nSummary:\n")
                    print(output["summary"])

                if "quiz_question" in output:
                    print("\nQuiz:\n")
                    print(output["quiz_question"])

                if "explanation" in output:
                    print("\nEvaluation:\n")
                    print(output["explanation"])


def main():

    while True:

        topic = input("\nWhat health topic would you like to learn about?\n> ")

        graph = HealthBotGraph()

        state = {"topic": topic}

        result = graph.run(state)

        print("\nSummary:\n", result["summary"])
        print("\nQuiz:\n", result["quiz_question"])

        answer = input("\nYour answer:\n> ")

        result["user_answer"] = answer

        result = graph.run(result)

        print("\nEvaluation:\n", result["explanation"])

        cont = input("\nLearn another topic? (yes/no)\n> ")

        if cont.lower() != "yes":
            break


if __name__ == "__main__":
    main()