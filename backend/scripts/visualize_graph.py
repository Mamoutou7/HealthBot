from backend.app.graph.healthbot_graph import HealthBotGraph


if __name__ == "__main__":

    graph = HealthBotGraph()

    graph.visualize()

    print("Graph visualization generated: healthbot_graph.png")