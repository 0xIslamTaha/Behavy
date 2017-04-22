Feature: Find specific agents

  Scenario:  Capture the first agent's info and take a screen shoots
    Given I open https://www.propertyfinder.ae web site
    When I click on find agent tab
    And Select the first agent
    And Capture information about him in a text file
    And Capture a screen shot
    And Change language to arabic
    Then make sure that language changed to arabic then capture a screen shoot

  Scenario:  Filter agents who can speak "HINDI, ENGLISH, ARABIC" and from India
    Given I open https://www.propertyfinder.ae web site
    When I click on find agent tab
    And Filter agents who can speak "HINDI, ENGLISH, ARABIC"
    And Note down the total count of agents before
    And Filter agents from India
    And Note down the total count of agents after
    Then Assert that latest count is less than the previous count
