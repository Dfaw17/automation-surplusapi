# How to run project!

- make sure python has been installed and configured
- make sure pycharm has been installed and configured
- clone repository in pycharm
- create new python environtment in project
- install library 
> pip install -r requirements.txt
- run project 
> python -m pytest -v --html-report=./report/report.html -p no:cacheprovider --disable-pytest-warnings -W ignore::DeprecationWarning