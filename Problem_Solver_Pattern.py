# -*- coding: utf-8 -*-
"""
    @author: M_Ark

    
"""

from abc import ABC, abstractmethod
from time import time


class Problem_Solver(ABC):
    """
        Abstract class to generalize problem solvers' interface.
    """
    def __init__(self):
        """
            Takes data from input or TEST_CASE in TEST_MODE.
                 Output: init: get data.lines
        """
        self.data_lines = self.get_data()

    def solve_problem(self):
        """
            Uses data lines to solve problem. Calls process_data first,
            than solves problem case by case, transfers answers
            to strings and returns their join.
            In TEST_MODE shows steps and correctness.
                Output: str.
        """
        global TEST_MODE, TEST_CASE, TEST_ANSWER
        if TEST_MODE:
            start_time = time()
            test_passed = True
        cases = self.process_data(self.data_lines)
        if not cases:
            raise Exception("Data-processor error")
        cases_answers = []
        if len(cases) > 1:
            TEST_ANSWERS = TEST_ANSWER.split()
        for case_id in range(len(cases)):
            if TEST_MODE:
                print("\nCase {}, conditions: {}".format(
                        case_id+1, cases[case_id]
                        ))
                case_start_time = time()
            case_answer = self.solve_case(cases[case_id])
            if not isinstance(case_answer, str):
                try:
                    case_answer = ' '.join(map(str, case_answer))
                except TypeError:
                    case_answer = str(case_answer)
            if TEST_MODE:
                case_fin_time = time()
                print("{}".format(case_answer))
                print("{} seconds.".format(
                        round(case_fin_time - case_start_time, 2)))
                if len(cases) > 1:
                    try:
                        correct_answer = TEST_ANSWERS[case_id]
                    except IndexError:
                        correct_answer = 'Unknown'
                else:
                    correct_answer = TEST_ANSWER
                if case_answer == correct_answer:
                    print("Correct!")
                elif correct_answer == 'Unknown':
                    pass
                else:
                    test_passed = False
                    print("Wrong! Correct answer:\n{}".format(correct_answer))
            cases_answers.append(case_answer)
        answer_to_problem = ' '.join(cases_answers)
        if TEST_MODE:
            fin_time = time()
            if test_passed:
                print("\nTest passed! It took {} seconds.\n".format(
                        round(fin_time - start_time, 2)))
            else:
                print("\nTest failed! It took {} seconds.\n".format(
                        round(fin_time - start_time, 2)))
                print("Correct final answer:\n{}".format(TEST_ANSWER))
            print("My final answer:")
        return answer_to_problem

    def get_data(self):
        """
            Takes input according to problem statement, or uses test data.
            Manual input demands EOF call by ctrl-z or !EOF.
            Output: list of strings.
        """
        global TEST_MODE, TEST_CASE
        if TEST_MODE:
            data_lines = [x.strip() for x in TEST_CASE.split('\n')]
        else:
            data_lines = []
            while True:
                try:
                    inp = input()
                    if inp == "!EOF":
                        raise EOFError
                    data_lines.append(inp)
                except EOFError:
                    break
        return data_lines

    @abstractmethod
    def process_data(self, data_lines):
        """
            Takes list of the raw data and returns only significant stuff.
            Returns list of data split to cases.
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
                Output: list: 
        """
        outp = []
        for line in data_lines:
            
        return outp

    def solve_case(self, case):
        """
            
                Input: case: 
                Output: 
        """
        pass

if __name__ == '__main__':

    TEST_MODE = True
    TEST_CASE = """"""
    TEST_ANSWER = """"""
    solver = Problem_No_Solver()
    print(solver.process_data(solver.data_lines))
#    print(solver.solve_problem())
