import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import argparse

from robotremoteserver import RobotRemoteServer

from lib.utils.AllKeywordsLibrary import AllKeywordsLibrary
# from lib.frontend.apphelpers.SampleNotepadHelper import SampleNotepadHelper
# from lib.browsers.pageobjectmodels.DemoMainPage import DemoMainPage


# class RemoteServer(DemoMainPage, SampleNotepadHelper):

#     def __init__(self):
#         SampleNotepadHelper.__init__(self)
#         DemoMainPage.__init__(self)

def main(arguments):
    parser = argparse.ArgumentParser(description='Remote server for the automation library')
    parser.add_argument("-a", '--address', default="127.0.0.1", help='Local IP address to launch the remote server. default: 127.0.0.1')
    parser.add_argument("-p", '--port', default="8271", help='Local Port number for the socket connection. default: 8271')
    args = parser.parse_args(arguments)
    RobotRemoteServer(AllKeywordsLibrary("Remote"), host=args.address, port=args.port)


if __name__ == '__main__':
    main(sys.argv[1:])