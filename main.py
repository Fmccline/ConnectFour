from GameManagerView import GameManagerView
from TimingTest import TimingTest


def run_evaluations_per_second_test(test):
    num_boards = 100
    iterations = 50
    test.print_evaluations_per_second(num_boards, iterations)


def run_board_creations_per_second_test(test):
    num_boards = 7 ** 6
    test.print_board_creations_per_second(num_boards)


def run_agent_evaluations_per_second_test(test):
    num_boards = 50
    test.print_seconds_per_agent_move(num_boards)


def run_games_per_second_test(test):
    num_games = 10
    test.print_games_per_second(num_games)


def run_timing_tests(timing_tests):
    num_columns = 7
    num_rows = 6
    test = TimingTest(num_columns, num_rows)
    for timing_test, should_run in timing_tests.items():
        if should_run:
            timing_test(test)


if __name__ == '__main__':
    timing_tests = {
        run_evaluations_per_second_test: False,
        run_board_creations_per_second_test: False,
        run_agent_evaluations_per_second_test: False,
        run_games_per_second_test: True
    }

    RUN_TESTS = False
    if RUN_TESTS:
        run_timing_tests(timing_tests)
    else:
        gm = GameManagerView()
        gm.main_loop()
