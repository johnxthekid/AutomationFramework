import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from robotremoteserver import RobotRemoteServer

from lib.frontend.apphelpers.SampleNotepadHelper import SampleNotepadHelper
from lib.browsers.pageobjectmodels.DemoMainPage import DemoMainPage


class RemoteServer(SampleNotepadHelper, DemoMainPage):
    # def __init__(self):
    pass


if __name__ == '__main__':
    # server = Robotremoteserver(RemoteServer(), host='127.0.0.1', port='8270', server=False)
    server = RobotRemoteServer(RemoteServer(), host='192.168.0.144', port=8570)