Feature: Hello World

  Scenario: The website says hello world
      When I visit the website root url
      Then the text 'Hello World!' is visible

  Scenario: The website says hello mariano
      When I visit the website root url
      Then The text shows 'Hello Mariano'
    
