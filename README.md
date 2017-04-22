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

You can change the base urls here or you can send BASE_URL as a context parameter.

**Reports**

All the required data can be found in **behave-propertyfinder/reports** and you can generate xml results by using **--junit** behave options.

**Results**
```bash
Before All
Reports Dir: reports/1492895904
Feature: Buy villa # features/BuyVilla.feature:1
Before scenario


 Scenario: Buy Villa in location THE PEARL with minimum 3BEDS and maximum 7BEDS              # features/BuyVilla.feature:3
   Given I open https://www.propertyfinder.qa web site                                       # features/steps/steps.py:7 13.424s
   When I search for VILLA to BUY in location THE PEARL with minimum 3BEDS and maximum 7BEDS # features/steps/steps.py:12 27.978s
   And Sort the villas from maximum price to lowest price                                    # features/steps/steps.py:19 10.150s
   And Fetch all the prices of the listing and save it in a csv                              # features/steps/steps.py:23 1.275s
 Scenario status: passed

Feature: Find Agents # features/FindAgents.feature:1
Before scenario


 Scenario: Capture the first agent's info and take a screen shoots  # features/FindAgents.feature:3
   Given I open https://www.propertyfinder.ae web site              # features/steps/steps.py:28 18.907s
   When I click on find agent tab                                   # features/steps/steps.py:33 10.494s
   And Select the first agent                                       # features/steps/steps.py:37 12.425s
   And Capture information about him in a text file                 # features/steps/steps.py:41 1.570s
   And Capture a screen shot                                        # features/steps/steps.py:47 0.199s
   And Change language to arabic                                    # features/steps/steps.py:51 6.529s
   And Capture a screen shot                                        # features/steps/steps.py:47 0.157s
 Scenario status: passed
Before scenario


 Scenario: Filter agents who can speak "HINDI, ENGLISH, ARABIC" and from India  # features/FindAgents.feature:13
   Given I open https://www.propertyfinder.ae web site                          # features/steps/steps.py:28 16.837s
   When I click on find agent tab                                               # features/steps/steps.py:33 11.226s
   And Filter agents who can speak "HINDI, ENGLISH, ARABIC"                     # features/steps/steps.py:55 7.896s
   And Note down the total count of agents before                               # features/steps/steps.py:60 0.067s
   And Filter agents from India                                                 # features/steps/steps.py:65 7.232s
   And Note down the total count of agents after                                # features/steps/steps.py:69 0.039s
   Then Assert that latest count is less than the previous count                # features/steps/steps.py:73 0.000s
 Scenario status: passed

2 features passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
18 steps passed, 0 failed, 0 skipped, 0 undefined
Took 2m26.406s

```
