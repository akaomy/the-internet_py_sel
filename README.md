## Demo for web test automation framework  
for https://the-internet.herokuapp.com/ website  

Tool kit:
- Selenium
- Python
- Behave
- Expects
- Allure


## RUNNING
to run separate scenarious marked by specific tag which you specify in .feature file using '@':

`<behave --tags=tag_name>` 



## REPORTING
to see the graphical output of test execution run following steps: 
1. create folder where you want to save your reports
2. create behave.ini - here you specify folder where you want to save your report data
3. in behave.ini specify: `<junit_directory=reports>`
4. install allure: `<pip install allure-behave>`
5. run `<behave>` - you'll get some .xml files
6. run `<allure>` serve your_folder (it should contain xml test data reports)
