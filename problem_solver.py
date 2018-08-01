# -*- coding: utf-8 -*-
"""@author: M_Ark"""

from abc import ABC, abstractmethod
from time import time


class ProblemSolver(ABC):
    """Abstract class to generalize problem solvers' interfaces.

    Main purpose of class's child is to proccess online interpreter's
    (or user's) input and return correct answer according to problem
    statement. This abstract class is for cutting programmer's work
    during making the specific problem solver (and for training ofc=)).
    There is only two things to make left: how to split data to cases
    and how to solve particular case.

    Supports test mode (test mode needs check_method function to be
    imported). To enable test mode give ProblemSolver's child test data
    as an argument at initialization.

    Attributes:
        test_data (str): Initialization argument. Data to test object.
        test_mode (bool): Turns True if object got test_data.
        test_answers (str): Initialization argument. Answer to test.
        data_lines (list): Consists of strs, problem's raw data.
        cases (list): Consists of tuples, data processed for solving.
        answers (str): Answer to whole problem, combined of answers
            to all cases.
    """
    def __init__(self, test_data='', test_answer=''):
        """Init, gets data, preparing for test if required.

        Considers ProblemSolver as real-world object, so init beside
        attribute creation takes input (problem data).

        Raises:
            TypeError: During init abstract method get_cases is
                executed. Error raises if get_cases returns unexpected
                data type (expects list).
        """
        if test_data:
            self.test_mode = True
            self.test_data = test_data
            self.test_answers = test_answer.split()
            print("\nTest mode on.", end=' ')
            if test_answer:
                print("Answers are given.\n")
            else:
                print("No answers given.\n")
        else:
            self.test_mode = False

        self.data_lines = self.get_data()
        self.cases = self.get_cases()
        self.answers = ''

        if self.test_mode:
            if not isinstance(self.cases, list):
                raise TypeError("TEST: Data Processor does not return list.")
            if len(self.cases) != len(self.test_answers):
                print("TEST: Number of given cases and answers are differ.\n")
                self.test_answers = None

    def get_data(self):
        """Takes input - data to work with. Unite it to list.

        Getter tries to return the result of it's previous work first.
        If it's the first call gets new data as a problem conditions.
        The way of getting data depends on self.test_mode variable.
        If it is True gets data from test data, typed in editor.
        Otherwise takes input from online interpreter (user's input).

        Returns:
            List of strings, each represents line of the input.
        """
        try:
            return self.data_lines
        except AttributeError:
            if self.test_mode:
                data_lines = self.test_data.split('\n')
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

    def get_cases(self):
        """Returns list of cases or calls method to create it.

        Small method to separate case-getter (this function) and
        abstract method process_data. It gives programmer opportunity
        forget about object's structure and focus on data processor.

        Returns:
            List of tuples, each represents case needed to solve.
        """
        try:
            return self.cases
        except AttributeError:
            return self.process_data()

    def get_answers(self):
        """Returns answer. If no answer stored, calls solve_problem."""
        if not self.answers:
            self.answers = self.solve_problem()
        return self.answers

    def solve_problem(self):
        """Solves by passing cases to abstract method solve_case.

        Method is separated from case_solver. It is the second purpouse
        of creating abstract ProblemSolver. Depending on the test_mode
        uses check_method decorator on the solve_case.

        Returns:
            String of answers to all cases (total problem answer).
        """
        answers = []
        for i in range(len(self.get_cases())):
            if not self.test_mode:
                answer = self.solve_case(self.get_cases()[i])
            else:
                try:
                    answer = check_method(
                        self.solve_case,
                        (self.get_cases()[i], ),
                        self.test_answers[i])
                except IndexError:
                    answer = check_method(
                        self.solve_case,
                        (self.get_cases()[i], ))
            answers.append(answer)
        return ' '.join(answers)

    @abstractmethod
    def process_data(self):
        """Splits data to cases, depending on the specific problem.

        Method supposed to be realised individually for each problem.

        Returns:
            List of tuples, each represents single problem case.
        """
        pass

    @abstractmethod
    def solve_case(self, case):
        """Solves particular case according to problem statement.

        Method supposed to be realised individually for each problem.

        Returns:
            String, answer to problem.
        """
        pass


def check_method(method, inp, outp=None):
    """Decorator compares return of method to the pre-known answer.

    This function needed for testing ProblemSolver's child, but can be
    used by any other object. Prints method name, it's arguments,
    output, results of checking for correctness and execution time.

    Arguments:
        method (callable): Function or method to run test on.
        inp (tuple): Arguments for callable being checked.
        outp (any): pre-known callable's output.

    Returns:
        Result of callable's execution.

    Raises:
        AssertionError: If argument method is not callable or
            argument inp is not a tuple.
    """
    assert callable(method), "TEST: No method given to checker."
    assert isinstance(inp, tuple), "TEST: Method's args must be a tuple."
    print("TEST: Checking method {}.".format(method.__name__))
    print("TEST: Arguments are: {}".format(inp))
    start_time = time()

    result = method(*inp)

    solving_time = round(time() - start_time, 2)
    print("TEST: Output:\nTEST: {}".format(result))
    if outp:
        if result == outp:
            print("TEST: Correct! ")
        else:
            print("TEST: Wrong! Correct output:\nTEST: {}".format(outp))
    print("TEST: Time: {}.\n".format(solving_time))

    return result
