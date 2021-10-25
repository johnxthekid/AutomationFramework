import sys

from robot.run import RobotFramework as rf


class RobotRunArguments:

    @staticmethod
    def get_run_argument(run_argument):
        options, args = rf().parse_arguments(sys.argv[:])

        for value in args:
            user_param = value.split(':')
            if len(user_param) > 1 and run_argument == user_param[0]:
                return user_param[1]
