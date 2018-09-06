import sys
import aig


def read_path():
    """
    Prints request for input and reads it. Note that this will also raise an exception
    in case input contains other characters than numbers and whitespace

    :return: List of user specified nodes
    """

    nodes = []
    fragments = input("Please specify the path for computation:\n").split()

    for node in fragments:
        if not node.isdigit():
            raise Exception("Invalid format of specified nodes!")
        else:
            nodes.append(int(node))

    return nodes


def check_node_bounds(node, graph):
    """
    Check whether given node is in graph bounds

    :param node: Index of node to be checked
    :param graph: Actually active graph
    """

    if node < 0 or graph.nodes_count < node:
        raise Exception("Trying to access node outside the graph bounds!")


def compute_path_cost(path, graph):
    """
    Computes costs along given path in specified graph

    :param path: List of nodes indicating path
    :param graph: Graph to be used for computation
    :return: String containing current costs along specified path
    """

    previous_node = None

    result = ""
    cumulative_cost = 0

    for node in path:

        check_node_bounds(node, graph)

        if previous_node is None:
            result += "0 "
        elif node in graph.nodes[previous_node]:
            cost = graph.nodes[previous_node][node]
            cumulative_cost += cost

            result += "{0} ".format(cumulative_cost)
        else:
            raise Exception("Specified path does NOT exist in given graph!")

        previous_node = node

    return result


def run_program():
    """
    Main function of the program
    """

    if not aig.are_parameters_valid():
        raise Exception("You must provide the name of input file as first argument!")

    graph = aig.parse_input(sys.argv[1])
    path = read_path()

    print(compute_path_cost(path, graph))


run_program()
