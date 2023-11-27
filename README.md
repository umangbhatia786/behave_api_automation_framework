# Behave API Framework for API Automation Testing

Clone this project into your local using below command:

```
git clone https://github.com/umangbhatia786/behave_api_automation_framework.git
```

Install below Python packages if not already installed on local or PyCharm virtual environment using below commands:

```
pip install behave
pip install requests
pip install allure-behave
pip install faker
pip install jsonschema
```

Install allure on your Mac using below brew command:

```
brew install allure
```
Then you can run the scripts by using below command inside the project directory:

```
behave --tags=@regression
```

You can generate and view Allure Reports using the below commands:

```
allure generate test_reports/allure.reports -o ./allure-report --clean
allure open ./allure-report
```