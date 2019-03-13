from ChartCreator import ChartCreator
from GameManagerView import GameManagerView
from TimingTest import TimingTest


def run_evaluations_per_second_test(test):
    num_boards = 500
    iterations = 100
    test.print_evaluations_per_second(num_boards, iterations)


def run_board_creations_per_second_test(test):
    num_boards = 7 ** 7
    test.print_board_creations_per_second(num_boards)


def run_agent_evaluations_per_second_test(test):
    num_boards = 50
    test.print_seconds_per_agent_move(num_boards)


def run_games_per_second_test(test):
    num_games = 5
    test.print_games_per_second(num_games)


def run_timing_tests(timing_tests):
    num_columns = 7
    num_rows = 6
    test = TimingTest(num_columns, num_rows)
    for timing_test, should_run in timing_tests.items():
        if should_run:
            timing_test(test)


def make_charts():
    file_name = 'charts.csv'
    num_games = 10
    chart_creator = ChartCreator()
    chart_creator.make_charts(num_games, file_name)


if __name__ == '__main__':
    timing_tests = {
        run_evaluations_per_second_test: True,
        run_board_creations_per_second_test: True,
        run_agent_evaluations_per_second_test: False,
        run_games_per_second_test: False
    }
    RUN_TEST = False
    PLAY_GAME = True
    MAKE_CHARTS = False

    if RUN_TEST:
        run_timing_tests(timing_tests)
    if PLAY_GAME:
        gm = GameManagerView()
        gm.main_loop()
    if MAKE_CHARTS:
        make_charts()
