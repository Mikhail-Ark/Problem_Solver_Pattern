# -*- coding: utf-8 -*-
"""
    @author: M_Ark

    
    
"""

from abc import ABC, abstractmethod


class Problem_Solver(ABC):
    """
        Abstract class to generalize problem solvers' interface.
    """
    def __init__(self, test_mode=False):
        """
            Take data from input or TEST_CASE in test_mode.
                Input: test_mode = bool
                Output: init: get data.lines
        """
        self.data_lines = self.get_data(test_mode)

    def solve_problem(self):
        """
            Use data lines to solve problem. Call process_data first,
            than solves problem case by case, transfers answers
            to strings and returns their join.
                Output: str
        """
        data = self.process_data(self.data_lines)
        case_answers = []
        for case in data:
            case_answer = self.solve_case(case)
            if isinstance(case_answer, list):
                case_answer = ' '.join(map(str, case_answer))
            case_answers.append(str(case_answer))
        answer_to_problem = ' '.join(case_answers)
        return answer_to_problem

    def get_data(self, test_mode):
        """
            Takes input according to problem statement, or uses test data.
            Output: list of strings.
        """
        if test_mode:
            data_lines = TEST_CASE.split('\n')
        else:
            data_lines = []
            while True:
                try:
                    data_lines.append(input())
                except EOFError:
                    break
        return data_lines

    @abstractmethod
    def process_data(self, data_lines):
        """
            Take list of the raw data and return only significant stuff.
            Return list of data split to cases.
                Input: data_lines: list of str.
                Output: list: depends on particular problem.
        """
        pass

    @abstractmethod
    def solve_case(self, case):
        """
            Abstract method which solves problem for particular case.
                Input: case: tuple.
                Output: depends on particular problem.
        """
        pass


class Problem_No_Solver(Problem_Solver):
    def process_data(self, data_lines):
        """
            
                Input: data_lines: list of str.
                Output:
        """
        raise Exception("TODO: need to implement data-processor")

    def solve_case(self, case):
        """
            
                Input: case: 
                Output: 
        """
        raise Exception("# TODO: need to implement case-solver")


if __name__ == '__main__':

    TEST_CASE = """"""
    solver = Problem_No_Solver(test_mode=True)
    print(*solver.process_data(solver.data_lines))
#    print(solver.solve_problem())
