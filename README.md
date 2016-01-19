# HelloWorld

- Create a django project with a single app
- Pip install the BDD requirements django-behave and splinter
- Create a features directory in the app you created, and a steps directory inside the features directory
- Create a helloworld.feature file with features below
- Run the test with python manage.py test yourappname
- Copy the suggested step implementations into features/steps/helloworld.py
- Implement the steps with meaningful python code
- Satisfy the test so it passes

# Features

```
Scenario: Hello World

  Feature: The website says hello world
    When I visit the website root url
    Then the text 'Hello World!' is visible
```
