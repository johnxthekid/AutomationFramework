# Automation Execution Framework

This is an Automation framework to test Web Browsers and Windows Applications. This framework allows users to run automation test without having extensive knowledge of a programming language. The framework is built using python and uses Selenium library for browser testing, Pywinauto for windows application testing. Robot Framework is also used to help with test case writing structure and report generation.

This framework also includes the feature run in parallel or in a remote server. 

## Getting Started

This a private repository on Bitbucket. Please contact the author to receive a demo

### Prerequisites

All required libraries are up to date in the projects requirement document.

```
pip install -r requirements.txt
```

### Setting up a virtual environment

In Python, each project may have separate libraries that they use. So, it is best to create separate virtual environment for each python project.

To create a virtual environment, navigate to the location where you want the folder to contain the virtual environment libraries to be located and run the commands below

```
python -m venv <virtual environment folder name>
```

Once created, the virtual environment needs to be activated. This can be done by navigating to the newly created folder and locating the 'Scripts' folder and run the commands below

```
activate.bat
```

#### Run Configuration

##### IDE Configuration

In order to run in the IDE, you must execute the Robot File which is the test suite.

```
Set Working Directory to the Project Root Directory
```
update the Parameters section as shown below. The run_arguments.robot contains all test configuration
All that needs to be pass is the folder containing the test files or the actual files themselves

Suite Run:
```
-m robot -A .\config\run_arguments.robot -s test.browser .
```

Test Run:
```
-m robot -A .\config\run_arguments.robot --test "test sample actions on broswer" .
```

passing variables
```
robot -A .\config\run_arguments.robot --variable BROWSER:chrome --suite test.browser .
```

Without passing the --suite argument, the __init__.robot file is not executed.

#### Command Line Configuration
To run on the command line, navigate to the project root directory and run the command below
```
python -m robot -A .\config\run_arguments.robot test\browser
```

##### Parallel Execution

As mentioned above, this framework also has the capabillities to run test in parallel. In order to do so, the test can be executed as specified below: 


Suite Run:
```
pabot --verbose --pabotlib --resourcefile .\config\value_set.dat --processes 1 -A .\config\run_arguments.robot test\browser
```

Test Run:
```
pabot --verbose --pabotlib --resourcefile .\config\value_set.dat --processes 1 -A .\config\run_arguments.robot test\browser\browser_test
```

passing variables
```
pabot --verbose --pabotlib --resourcefile .\config\value_set.dat --processes 1 -A 
.\config\run_arguments.robot --variable BROWSER:chrome test\browser
```

The 'processes' parameter is used to run test in parallel. This can be used to execute in multiple processes on the same computer or multiple remote computers. 

The file 'value_set.dat' contains the information for the differnet remote machines such as the IP address of those remote computers.  Duplicate the Sets to configure multiple computers. 


#### Remote Server configuration
To run on a remote server, the python script to start the remote server must be executed.

The remote server can be started below. Navigate to the location from the project directory. The remote server can be run on any local IP location and open ports.

NOTE: The RemoteServerAPI script must be executed on each remote computer

```
cd lib\utils
python RemoteServerAPI -a 127.0.0.1 -p 8272
```

## Authors

* **John Exantus** - *Full Framework*

## License

This project is property of John Exantus and may be reused without explicit permission.
