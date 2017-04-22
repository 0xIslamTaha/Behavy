Feature: Buy villa

  Scenario:  Buy Villa in location THE PEARL with minimum 3BEDS and maximum 7BEDS
    Given I open https://www.propertyfinder.qa web site
    When I search for VILLA to BUY in location THE PEARL with minimum 3BEDS and maximum 7BEDS
    And Sort the villas from maximum price to lowest price
    And Fetch all the prices of the listing and save it in a csv
    Then Make sure that the listing items are equal to the results
