import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from robot.libraries.BuiltIn import BuiltIn
from robot.errors import UserKeywordExecutionFailed

from lib.utils.RemoteServerAPI import remote_status


class RemoteServerListener:
    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self

    def _start_suite(self, data, result):
        print(f"Root Suite Name: {data.name}")
        try:
            BuiltIn().run_keyword('Get Arguments')
        except UserKeywordExecutionFailed:
            print("Keyword 'Get Arguments' failed.")
            BuiltIn().fatal_error(f"Keyword 'Get Arguments' failed. Stopping execution for Suite: {data.name}")

        run_location = BuiltIn().get_variable_value('${RunLocation}')
        server_uri = BuiltIn().get_variable_value('${Server_URI}')
        print(f"Server URI: {server_uri}")
        while True:
            if run_location == "remote" and server_uri != "Local Libraries" and not remote_status(server_uri):
                print("Remote Server not running. trying to refresh it")
                BuiltIn().run_keyword('Disable Value Set')
                try:
                    BuiltIn().run_keyword('Get Arguments')
                except UserKeywordExecutionFailed as err:
                    print(f"Failed to retrieve another value set. {err.message}")
                    BuiltIn().fatal_error(f"Failed to retrieve another value set. {err.message} \n"  
                                            f"Stopping execution for Suite: {data.name}")
                    break

                run_location = BuiltIn().get_variable_value('${RunLocation}')
                print(f"New Server URI: {server_uri}")
            else:
                break

        print(f"Root Suite Remote Server Status: {remote_status(run_location)}")
