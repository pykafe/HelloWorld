Feature: Hello World

  Scenario: The website says hello world
      When I visit the website root url
      Then the text 'Hello World!' is visible
