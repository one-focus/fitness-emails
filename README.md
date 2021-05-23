## Email project
### Installation
```
brew install python
brew install chromedriver
pip install git+https://github.com/behave/behave
pip install -r requirements.txt
```
### Run 
```
behave
```
+ Use tags
```
behave --tags=regression,search
```
+ Generate allure report
```
behave -f allure_behave.formatter:AllureFormatter -o allure-results --tags=regression,search  
allure generate --clean "allure-results" -o "allure-report"
allure serve allure-results
```
+ Run parallel (by features)
```
python behave-parallel.py --tags=regression,search
```
