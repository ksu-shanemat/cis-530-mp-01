*************************************** README file for CIS-530-MP2 ****************************************

 This file contains compile and runtime documentation for solution files for the first
machine problem for KSU class CIS-530 (Introduction to) Artificial Intelligence. Please
read those carefully since without further understanding of documentation given Python
scripts might not work properly.

 Content:
    * aig.py - library containing necessary objects and function for proper parsing
                of .aig files
    * mp2-i.py - scripts with solution for corresponding assignment parts (1-3)
    * mp2-x3.py - script containing B&B search algorithm extended by option to select
                    one of given heuristics (extra credit problem no. 3)

 Compilation:
    * all solution files were written using Python v3.6 (in JetBrains IDE PyCharm 2018.1)
        and therefore compatible version of Python is needed to run them
    * solution scripts use following python libraries (accessible via pip):
        * re - used for RegEx matching
        * copy - used for easy creation of deep copies instead of shallow ones
        * q - used for implementation of priority queue
    * those libraries are NOT included in the archive and you should make sure you have
        them installed before attempting to execute any scripts

 Execution:
    All given scripts should work according to specification provided. In case input does
    NOT match the specification, exception is raised (trying to provided description of
    what went wrong).

    * mp2-1.py
        * command line: 1 argument - path to .aig file
    * mp2-2.py
        * command line: 1 argument - path to .aig file
        * standard input: 1 line ended by newline - list of indexes of nodes on path
    * mp2-3.py
        * command line: 1 argument - path to .aig file
    * mp2-x3.py
        * command line: 1 argument - path to .aig file
        * standard input: 1 number followed by newline - index of heuristic to use

 Compatibility:
    The author (shanemat@KSU) did his best to make those scripts compatible with ANY of
    .aig format versions (all 3 of them). However, due to bit fuzzy specification you
    might run into runtime parsing problems in versions 1 and 2. The version 3 should
    however get parsed properly under any circumstances.

    If you run into compatibility problems, please contact the author (shanemat@ksu.edu)
    with your problem description preferably with problematic input file attached along
    with description of why does your file match the specification. Thank you

 Solution for problem no. 6 - Analysis:
    - Show that it is possible for a heuristic to be admissible but not consistent, but
    not the other way around.

    First it is good to specify, what does "admissible" and "consistent" mean.

    "Admissible" means, that heuristic function never overestimates the remaining cost
    of path from current node to the goal node.

    "Consistent" means, that the function "f(n)" ( = g(n) + h(n) ) is non-decreasing
    along any path.

    Let's first prove that heuristic can be admissible but not consistent. Admissibility
    only requires the heuristic function to be less or equal to actual path cost from node
    to goal node. However, we can construct heuristic, which will be always admissible by
    making all its values lower than cost of the least expensive path in given graph.

    To construct heuristic, which is admissible but not consistent, we simply set the values
    of heuristic function to actual cost of remaining path, except for one node in the middle,
    which we can give any lesser value than the actual.

    In this case the heuristic is still admissible, since all nodes have lesser or equal value
    to cost of remaining path but the value of our heuristic function would decrease from node
    before the lowered one to the lowered one, making the heuristic function non-consistent.

    Example could be following graph (with h(n) in brackets above nodes, nodes being named as
    letters and numbers in the middle of arrows being path costs):

    (3)      (1)      (0)
     A -[1]-> B -[2]-> C

     Where the values of f(n) would be:
        * A ~ 3 + 0 = 3
        * B ~ 1 + 1 = 2 (decrease!)
        * C ~ 0 + 3 = 3

    Now, let's focus on proving that any consistent heuristic function must also be admissible,
    by contradiction. Let's assume that our heuristic is consistent but is NOT admissible. Therefore
    for any node "n" and its succeeding node "n'" it holds that:

        f(n) <= f(n')
        g(n) + h(n) <= g(n') + h(n')
        g(n) + h(n) <= g(n) + c(n, a, n') + h(n')
        h(n) <= c(n, a, n') + h(n')

    and also there is at least one node "n" that for goal node "x":

        h(n) > remaining_cost(n, x)

    Let's rewrite the consistency condition for n' ~ goal node "x" and n ~ m the node right before "x":

        h(m) <= c(m, a, x) + h(x)

    From the definition of heuristic we know, that h(n) must be 0 for every goal node. We then get:

        h(m) <= c(m, a, x) + 0

    And we also know, that "c(m, a, x)" is the cost of remaining path from "m" to "x". Therefore we either
    get contradiction with original assumption of "h(n) > remaining_cost(n, x)" or we must admit, that on
    this part of the path the heuristic is also admissible.

    Now we use induction. Because we know, that part of path from "m" to "x" is admissible, we can simplify
    the problem by calling the "m" the new goal node and performing the step again. By doing this we either
    find contradiction or we reach the initial node without breaking the admissibility at least once.

    This means that once the heuristic is consistent, it also has to be admissible.
                                                                                                    Q.E.D.

************************************************************************************************************