# Carro offline test

>###  Installation 
Please use the buildin python in Pycharm to install the following libraries to avoid dependency conflicts: 
1. launch Pycharm and open the project, 
2. then use the terminal which is on the bottom of Pycharm
* #### Install selenium 
```
pip install selenium
```
* #### Install HTMLTestRunner
```
pip install HTMLTestRunner-Python3
```
* #### Install chromedriver
1. Download chromedriver from:  https://chromedriver.chromium.org/downloads  
2. Get system’s path
```
echo $PATH
```
3. Unzip chromedriver and copy to the system’s path
```
cp ~/Downloads/chromedriver /usr/local/bin/
```
>### Execution
To run the test cases, please use this command in Pycharm:
```
python RunTest.py
```
