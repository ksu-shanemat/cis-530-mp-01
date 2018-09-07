import sys
import aig

import queue as q
from aig import SearchNode


def construct_solution(final_search_node):
    """
    Constructs string containing solution in proper format from final search node

    :param final_search_node: Result of search
    :return: String containing solution
    """

    result = ""
    path_length = len(final_search_node.path)

    for path_index in range(path_length):

        result += "{0}".format(final_search_node.path[path_index])

        if not path_index == path_length - 1:
            result += " -[{0}]-> ".format(final_search_node.costs[path_index])

    result += "\n"
    result += "Total path cost: {0}".format(final_search_node.total_cost)

    return result


def execute_a_search(graph, heuristic_index):
    """
    Executes A search on given graph

    :param graph: Graph to run A search in
    :param heuristic_index: Index of selected heuristic function
    :return: Node containing solution of search
    """

    if heuristic_index < 0 or graph.heuristics_count <= heuristic_index:
        raise Exception("Invalid number of selected heuristic!")

    node = SearchNode(graph.start_nodes[0], 0, None)
    heuristic = graph.heuristics[heuristic_index]

    queue = q.PriorityQueue()
    queue.put((heuristic[graph.start_nodes[0]], node))

    while not queue.empty():
        f, node = queue.get()
        if node.node_index in graph.goal_nodes:
            break

        for (next_node, cost) in graph.nodes[node.node_index].items():
            generated_node = SearchNode(next_node, cost, node)
            queue.put((heuristic[next_node] + generated_node.total_cost, generated_node))

    return construct_solution(node)


def run_program():
    """
    Main function of the program
    """

    if not aig.are_parameters_valid():
        raise Exception("You must provide the name of input file as first argument!")

    graph = aig.parse_input(sys.argv[1])

    for heuristic_index in range(graph.heuristics_count):
        print(execute_a_search(graph, heuristic_index), "\n")


run_program()
