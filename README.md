This is an implementation of some testing scenarios using  **behave**  as a BDD python framework.

**Pre-requestes:**
- Python3
- Chrome (tested with Chromium 55.0.2883.87 Built on Ubuntu , running on Ubuntu 16.04)
- Firefox (tested with Mozilla Firefox 53.0.0)
- GeckoDriver (testd with geckodriver 0.16.0)

**Installation:**
```bash
apt-get install xvfp
git clone git@github.com:islamTaha12/behave-propertyfinder.git
cd behave-propertyfinder
pip3 install -r requirements.txt
```

**Execution modes:**

1- Run all features using chrome
```bash
behave
```

2- Run all features using a specific browser
```bash
behave -D BROWSER=firefox
```

3- Run all features with headless mode
```bash
behave -D HEADLESS_MODE=true
```

4- Run a specific feature
```bash
behave <feature_path>
```

**Change base url**

You can change the base urls in https://github.com/islamTaha12/behave-propertyfinder/blob/master/features/environment.py#L7 or you can send BASE_URL as a context parameter.

**Reports**

All the required data can be found in **behave-propertyfinder/reports** and you can generate xml results by using **--junit** behave options.

**First agent info:**

https://github.com/islamTaha12/behave-propertyfinder/blob/master/reports/1492904453/Marina%20Berdnikova

**Price List:**

https://github.com/islamTaha12/behave-propertyfinder/blob/master/reports/1492904453/priceList.csv

**ScreenShots:**

https://github.com/islamTaha12/behave-propertyfinder/blob/master/reports/1492904453/7f48ea1f.png
https://github.com/islamTaha12/behave-propertyfinder/blob/master/reports/1492904453/d1093ef1.png


**Results**
```bash
 Before All
 Reports Dir: reports/1492904130
Feature: Buy villa # features/BuyVilla.feature:1
Before scenario


  Scenario: Buy Villa in location THE PEARL with minimum 3BEDS and maximum 7BEDS              # features/BuyVilla.feature:3
    Given I open https://www.propertyfinder.qa web site                                       # features/steps/steps.py:7 13.724s
    When I search for VILLA to BUY in location THE PEARL with minimum 3BEDS and maximum 7BEDS # features/steps/steps.py:12 28.496s
    And Sort the villas from maximum price to lowest price                                    # features/steps/steps.py:20 5.485s
    And Fetch all the prices of the listing and save it in a csv                              # features/steps/steps.py:24 1.382s
    Then Make sure that the listing items are equal to the results                            # features/steps/steps.py:30 0.000s
  Scenario status: passed

Feature: Find specific agents # features/FindAgents.feature:1
Before scenario


  Scenario: Capture the first agent's info and take a screen shoots            # features/FindAgents.feature:3
    Given I open https://www.propertyfinder.ae web site                        # features/steps/steps.py:34 17.001s
    When I click on find agent tab                                             # features/steps/steps.py:39 10.819s
    And Select the first agent                                                 # features/steps/steps.py:43 12.147s
    And Capture information about him in a text file                           # features/steps/steps.py:47 1.504s
    And Capture a screen shot                                                  # features/steps/steps.py:53 0.210s
    And Change language to arabic                                              # features/steps/steps.py:57 5.462s
    Then make sure that language changed to arabic then capture a screen shoot # features/steps/steps.py:61 0.158s
  Scenario status: passed
Before scenario


  Scenario: Filter agents who can speak "HINDI, ENGLISH, ARABIC" and from India  # features/FindAgents.feature:12
    Given I open https://www.propertyfinder.ae web site                          # features/steps/steps.py:34 16.884s
    When I click on find agent tab                                               # features/steps/steps.py:39 9.961s
    And Filter agents who can speak "HINDI, ENGLISH, ARABIC"                     # features/steps/steps.py:67 7.402s
    And Note down the total count of agents before                               # features/steps/steps.py:72 0.040s
    And Filter agents from India                                                 # features/steps/steps.py:77 7.182s
    And Note down the total count of agents after                                # features/steps/steps.py:81 0.040s
    Then Assert that latest count is less than the previous count                # features/steps/steps.py:85 0.000s
  Scenario status: passed

2 features passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
19 steps passed, 0 failed, 0 skipped, 0 undefined
Took 2m17.895s

```
