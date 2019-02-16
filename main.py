from GameManagerView import GameManagerView
from TimingTest import TimingTest


def run_timing_tests():
    num_columns = 7
    num_rows = 6
    test = TimingTest(num_columns, num_rows)
    #run_evaluations_per_second_test(test)
    run_agent_evaluations_per_second_test(test)
    #run_games_per_second_test(test)

def run_evaluations_per_second_test(test):
    num_boards = 1000
    iterations = 100
    test.print_evaluations_per_second(num_boards, iterations)


def run_agent_evaluations_per_second_test(test):
    num_boards = 100
    test.print_agent_evaluations_per_second(num_boards)


def run_games_per_second_test(test):
    num_games = 10
    test.print_games_per_second(num_games)


if __name__ == '__main__':
    # run_timing_tests()
    gm = GameManagerView()
    gm.main_loop()


