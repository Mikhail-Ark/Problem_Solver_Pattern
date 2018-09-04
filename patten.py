# -*- coding: utf-8 -*-
"""

@author: M_Ark
"""

from problem_solver import ProblemSolver


class Problem_No_Solver(ProblemSolver):
    def process_data(self):
        """Makes cases out of data.

        Returns:
            List of
        """
        outp = []
        for line in self.data_lines:
            pass
        return outp

    def solve_case(self, case):
        """.

        Returns:
            String of
        """
        return str()


if __name__ == '__main__':

    test_data = """"""
    test_answer = """"""
    solver = Problem_No_Solver(test_data, test_answer)
    print(solver.get_cases())
#    print(solver.get_answers())
