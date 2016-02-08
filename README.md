# HelloWorld

- Create a new virtual environment to work in
- Git clone this repository
- Pip install `Django`, and the BDD requirements `django-behave` and `splinter`
- Create a django project with a single app named `hello`
- edit you settings file to add `django_behave` and `hello` to INSTALLED_APPS and set TEST_RUNNER to django_behave.runner.DjangoBehaveTestSuiteRunner
- Create a features directory in the app you created, and a steps directory inside the features directory
- Create a features/environment.py file with the following contents
    
'''

      from splinter.browser import Browser
      
      def before_all(context):
          context.browser = Browser(context.config.browser)
      
      def after_all(context):
          context.browser.quit()
          context.browser = None
'''

- Create a helloworld.feature file with features below
- Run the test with `python manage.py test hello`
- Copy the suggested step implementations into features/steps/helloworld.py
- Implement the steps with meaningful python code
- Satisfy the test so it passes

# Features

```
Feature: Hello World

  Scenario: The website says hello world
    When I visit the website root url
    Then the text 'Hello World!' is visible
```
