import sys
import os
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from robot.libraries.BuiltIn import BuiltIn

from lib.utils.RemoteServerAPI import remote_status


class RemoteServerListener:
    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self

    def _start_suite(self, data, result):
        print(f"Root Suite Name: {data.name}")
        BuiltIn().run_keyword('Get Arguments')
        server_uri = BuiltIn().get_variable_value('${RunLocation}')
        print(f"Run Location: {server_uri}")
        while True:
            if server_uri != "" and not remote_status(server_uri):
                print("Remote Server not running. trying to refresh it")
                BuiltIn().run_keyword('Disable Value Set')
                BuiltIn().run_keyword('Get Arguments')
                server_uri = BuiltIn().get_variable_value('${RunLocation}')
                print(f"New Run Location: {server_uri}")    
                # break
            else:
                break

        print(f"Root Suite Remote Server Status: {remote_status(server_uri)}")
