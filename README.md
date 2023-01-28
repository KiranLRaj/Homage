# Homage

# KiranL_HomageCodeChallenge
	
	The above repository is specifically to sole code challenge given by Homage team.

# Tools and framework used
	
	Selenium with python language and Pytest framework is used.

# Installation
	Python 3.10 or above must be installed on your computer.
	Add the path of scripts folder in your python directory to the system ENV Path parameter.(eg: C:\Users\***\AppData\Local\Programs\Python\Python311\Scripts)
	Run below command to install required packages:
		pip install selenium
		pip install pytest
	Download and install Pycharm IDE

# ENV Setup
	Download the repository from the link provided and open it in Pycharm (https://github.com/KiranLRaj/KiranL_HomageCodeChallenge)
	Goto "file->settings->project" and setup the python interpreter(select python exe file, eg: C:\Users\***\AppData\Local\Programs\Python\Python311\python.exe)
	After setting up the interpretor, check if the above installed packages are loaded

# Chrome driver setup(Selenium)
	Download appropriate selenium chrome driver(according to your chrome version) and save it in this path : "C:\Selenium\chromedriver.exe".
	Change the path in "conftest" python file if you have saved it in some other directory.(driver=webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe",options=options))

# Execution
	Open "Homage_codeChallenge" file under test_scripts folder and run the file.(Run option will be enabled only after setting up the interpreter) 

# Validation
	Please check the console after execution, for appropriate comments after each step.
	Please validate the screenshot captured at the last step(screenshot will be saved in test_scripts folder).
