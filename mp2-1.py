import sys
import aig


def run_program():
    """
    Main function of the program
    """

    if not aig.are_parameters_valid():
        raise Exception("You must provide the name of input file as first argument!")

    graph = aig.parse_input(sys.argv[1])

    print("  Adjacency list:\n")
    print(graph.get_printable_adjacency_list())

    print("  Adjacency matrix:\n")
    print(graph.get_printable_adjacency_matrix())


run_program()
