# HelloWorld

1. Create a new virtual environment to work in
2. Git clone this repository
3. Pip install `Django`, and the BDD requirements `django-behave` and `splinter`
4. Create a django project with a single app named `hello`
5. edit your `settings.py` file to add `django_behave` and `hello` to `INSTALLED_APPS` and set `TEST_RUNNER` to `django_behave.runner.DjangoBehaveTestSuiteRunner`
6. Create a directory named `features` in the app you created
7. Create a directory named `steps` directory inside the `features` directory
8. Create a file named `environment.py` inside the `features` directory with the following contents:
            
        from splinter.browser import Browser

        def before_all(context):
            browser = context.config.browser
            if browser is None:
                browser = 'phantomjs'
            context.browser = Browser(browser)

        def after_all(context):
            context.browser.quit()
            context.browser = None

9. Create a new file named `helloworld.feature` file with features below:

      Feature: Hello World

        Scenario: The website says hello world
          When I visit the website root url
          Then the text 'Hello World!' is visible


10. Run the test with `python manage.py test hello`
11. Copy the suggested step implementations into `features/steps/helloworld.py`
12. Implement the steps with meaningful python code
13. Satisfy the test so it passes
