# Automation Execution Framework

This is an Automation framework to test Web Browsers and Windows Applications. This framework allows users to run automation test without having extensive knowledge of a programming language. The framework is built using python and uses Selenium library for browser testing, Pywinauto for windows application testing. Robot Framework is also used to help with test case writing structure and report generation.

## Getting Started

This a private repository on Bitbucket. Please contact the author to receive a demo

### Prerequisites

All required libraries are up to date in the projects requirement document.

```
pip install -r requirements.txt
```

## Running the tests

To run the test cases in the project, you can either configure a run configuration in the IDE or Command prompt.

#### IDE Configuration

In order to run in the IDE, you must execute the Robot File which is the test suite.

```
Set Working Directory to the Project Root Directory
```
update the Parameters section as shown below. The run_arguments.robot contains all test configuration
All that needs to be pass is the folder containing the test files or the actual files themselves

Suite Run:
```
-m robot -A .\config\run_arguments.robot test\browser
```

Test Run:
```
-m robot -A .\config\run_arguments.robot test\browser\browser_test
```

passing variables
```
robot -A .\config\run_arguments.robot --variable BROWSER:chrome test\browser
```

#### Command Line Configuration
To run on the command line, navigate to the project root directory and run the command below
```
python -m robot -A .\config\run_arguments.robot test\browser
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

## Authors

* **John Exantus** - *Full Framework*

## License

This project is property of John Exantus and may be reused without explicit permission.
