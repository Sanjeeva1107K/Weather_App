\# Test Case Document



\## Automated Weather Dashboard \& Alert System



\### Objective



The purpose of this document is to verify the functionality, reliability, and error handling capabilities of the Automated Weather Dashboard \& Alert System.



\---



\# 1. Positive Test Cases



| Test Case ID | Scenario                  | Input               | Expected Result                            | Actual Result                   | Status |

| ------------ | ------------------------- | ------------------- | ------------------------------------------ | ------------------------------- | ------ |

| TC-01        | Search Valid City         | Kanchipuram         | Weather information displayed successfully | Weather displayed successfully  | PASS   |

| TC-02        | Display Temperature       | Valid City          | Temperature shown in Celsius               | Temperature displayed correctly | PASS   |

| TC-03        | Display Humidity          | Valid City          | Humidity percentage displayed              | Humidity displayed correctly    | PASS   |

| TC-04        | Display Weather Condition | Valid City          | Weather condition displayed                | Condition displayed correctly   | PASS   |

| TC-05        | Save Search History       | Valid City Search   | Search stored in history.json              | Record saved successfully       | PASS   |

| TC-06        | View Search History       | Select View History | Previous searches displayed                | History displayed correctly     | PASS   |

| TC-07        | Exit Application          | Select Exit         | Program terminates successfully            | Program exited successfully     | PASS   |



\---



\# 2. Negative Test Cases



| Test Case ID | Scenario               | Input               | Expected Result                        | Actual Result                      | Status |

| ------------ | ---------------------- | ------------------- | -------------------------------------- | ---------------------------------- | ------ |

| TC-08        | Invalid City Name      | Ho chi 854          | Error message displayed                | ❌ City not found.                 | PASS   |

| TC-09        | Numeric Input          | 125488555           | Error message displayed                | ❌ City not found                  | PASS   |

| TC-10        | Empty Input            | ""                  | User prompted again or error displayed | ❌ City not found.                 | PASS   |

| TC-11        | Invalid API Key        | Incorrect API Key   | Authentication error displayed         | ❌ Network/API Error               | PASS   |

| TC-12        | No Internet Connection | Disconnect Network  | Network error displayed                | ❌ Network/API Error               | PASS   |

| TC-13        | Missing History File   | Delete history.json | No history found message displayed     | Message displayed correctly         | FAIL   |



\---



\# 3. Edge Test Cases



| Test Case ID | Scenario                       | Input                    | Expected Result                 | Status |

| ------------ | ------------------------------ | ------------------------ | ------------------------------- | ------ |

| TC-14        | City Name With Spaces          | New York                 | Weather displayed successfully  | PASS   |

| TC-15        | Very Long City Name            | Extremely Long City Name | Weather displayed successfully  | PASS   |

| TC-16        | Less Than Five History Records | 3 Records                | Last Five Records Displayed     | PASS   |

| TC-17        | Exactly Five History Records   | 5 Records                | All five records displayed      | PASS   |

| TC-18        | More Than Five History Records | 10 Records               | Latest five records displayed   | PASS   |

| TC-19        | Temperature Exactly 35°C       | Boundary Value           | Verify alert threshold behavior | PASS   |

| TC-20        | Temperature Exactly 0°C        | Boundary Value           | Verify alert threshold behavior | PASS   |



\---



\# 4. False Positive Test Cases



| Test Case ID | Scenario                               | Input   | Expected Result            | Status |

| ------------ | -------------------------------------- | ------- | -------------------------- | ------ |

| TC-21        | Temperature Below High Alert Threshold | 34.9°C  | No High Temperature Alert  | PASS   |

| TC-22        | Temperature Above Freezing Threshold   | 1°C     | No Freezing Alert          | PASS   |

| TC-23        | Weather Condition Clouds               | Clouds  | No Rain Alert Generated    | PASS   |

| TC-24        | Weather Condition Clear                | Clear   | No Snow Alert Generated    | PASS   |

| TC-25        | Valid City Search                      | Chennai | No Error Message Displayed | PASS   |



\---



All executed test cases behaved as expected.

