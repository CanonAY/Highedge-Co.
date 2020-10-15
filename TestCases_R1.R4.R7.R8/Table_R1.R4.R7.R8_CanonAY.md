#### Table for R1:

|                                                                      Specification                                                                     | Test case ID |                                                                                   Purpose                                                                                   |
|:------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                                                    If the user hasn't logged in, show the login page                                                   | R1.1         | Check if the user open /login in un-logged in status, user will be directed to login page                                                                                   |
|                                            the login page has a message that by default says 'please login'                                            | R1.2         | Check if the login page contains a message "please login"                                                                                                                   |
|                                              If the user has logged in, redirect to the user profile page                                              | R1.3         | Check if the user open /login in logged in status, user  will be re-directed to profile page                                                                                |
|                                  The login page provides a login form which requests two fields:  email and passwords                                  | R1.4         | Check if the login page contains two fields for the user  to enter email and password                                                                                       |
|                                      The login form can be submitted as a POST request to the current URL (/login)                                     | R1.5         | Check if the form contains user's login information has  been sent to and received by /login                                                                                |
|                                                         Email and password both cannot be empty                                                        | R1.6.1       | Check that when the user enters non-empty, matching email  and password, the login action succeed                                                                           |
|                                                         Email and password both cannot be empty                                                        | R1.6.2       | Check that when either of email and password field is empty,  an error message will pop up, and the login action failed                                                     |
|                                                    Email has to follow addr-spec defined in RFC 5322                                                   | R1.7.1       | Check that when user enter valid email with matching password,  the login action succeed                                                                                    |
|                                                    Email has to follow addr-spec defined in RFC 5322                                                   | R1.7.2       | Check that when user enter email that not follows RFC5322  specification, an error message will pop up, the login action failed.                                            |
| Password has to meet the required complexity: minimum length 6,  at least one upper case, at least one lower case, and at least one  special character | R1.8.1       | Check that when user enter validly complex password with  matching email, the login action succeed                                                                          |
| Password has to meet the required complexity: minimum length 6,  at least one upper case, at least one lower case, and at least one  special character | R1.8.2       | Check that when user enter invalid simple password, an  error message will pop up, the login action failed                                                                  |
|                      For any formatting errors, render the login page and show the message  'email/password format is incorrect.'                      | R1.9         | Check that when any formatting error occurs, the page will be  rendered, and an error message will pop up                                                                   |
|                                                      If email/password are correct, redirect to /                                                      | R1.10        | Check that when user enters matching email and password with no  formatting error occurs, the login in action succeed, and the user  will be redirected to the profile page |
|                                 Otherwise, redirect to /login and show message  'email/password combination incorrect'                                 | R1.11        | Check that login action failed when users enters email and password that  do not match, and user will be redirected to /login page                                          |


#### Table for R4:

|                                                       Specification                                                       | Test case ID |                                                              Purpose                                                             |
|:-------------------------------------------------------------------------------------------------------------------------:|:------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| The name of the ticket has to be alphanumeric-only, and space  allowed only if it is not the first or the last character. | R4.1.1       | Check when the user enters well-formatted ticket name and all other  information correctly, the selling action succeed           |
| The name of the ticket has to be alphanumeric-only, and space  allowed only if it is not the first or the last character. | R4.1.2       | Check when the user enters invalid ticket name, an error message pops  up, the selling action failed                             |
|                                   The name of the ticket is no longer than 60 characters                                  | R4.2.1       | Check when the user enters ticket name with length less than 60 and  all other information correctly, the selling action succeed |
|                                   The name of the ticket is no longer than 60 characters                                  | R4.2.2       | Check when the user enters ticket name with length greater than 60,  an error message pops up, the selling action failed         |
|                     The quantity of the tickets has to be more than 0, and less than  or equal to 100.                    | R4.3.1       | Check when the user enters quantity in range 1-100 and all other  information correctly, the selling action succeed              |
|                     The quantity of the tickets has to be more than 0, and less than  or equal to 100.                    | R4.3.2       | Check when the user enters quantity <1 or >=100, an error message  pops up, the selling action failed                            |
|                                             Price has to be of range [10, 100]                                            | R4.4.1       | Check when the user enters price in range [10,100] and all other  information correctly, the selling action succeed              |
|                                             Price has to be of range [10, 100]                                            | R4.4.2       | Check when the user enters price out of the range [10,100], an  error message pops up, the error message failed                  |
|                                         Date must be given in the format YYYYMMDD                                         | R4.5.1       | Check when the user enters well-formatted date and all other  information correctly, the selling action succeed                  |
|                                         Date must be given in the format YYYYMMDD                                         | R4.5.2       | Check when the user enters invalid data, an error message pops  up, the selling action failed                                    |
|                                For any errors, redirect back to / and show an error message                               | R4.6         | Check that if any error occurred, an error message pops up, the  selling action failed                                           |
|                          The added new ticket information will be posted on the user profile page                         | R4.7         | Check that after a new ticket is added, it will show up on the profile page                                                      |


#### Table for R7:

|                                                             Specification                                                                   | Test case ID |                                                                                   Purpose                                                                                   |
|:-------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.| R7./         | Check that after the user logged-out, user will be redirected to login page, and any attempt to access pages other than login, register and logout will fail.               |



#### Table for R8:

|                                  Specification                                     | Test case ID |                                                                                   Purpose                                                                                                                |
|:----------------------------------------------------------------------------------:|:------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| For any other requests except the ones above, the system should return a 404 error.| R8./         | Check that when user tries to open any pages except ones specified, the action will fail, no matter whether the user is logged-in or not. The user will then be directed to a page that shows error 404. |




#### Test Plan:
1. Method to organize the documation of test cases:  
  - We created a folder in our repository named "TestCases", then in this folder, each team member will create a subfolder that contains two markdown files: one that contains the test cases written in nature language, the other one contains the table with three columns: specification, test case ID, and purpose. Each file will be marked well in its name that what it contains, and created by whom, thus there will be no confusion. 
2. Understanding of testing framework:  
  - The testing framework works by setting up constaints, tell the developers what to test for and how the software should behave under certain circumstances. They helps developers to create the test cases, which works as the goal of the product development.
  - The test cases should run at each time a unit test is required, that a small section of code is completed. The first time that test cases need to run directly is the end of prototyping stage, where the prototype need to be tested to make sure it meets the requirement. 
3. Method to organize the test case code file:
  - We will create a folder in our repository named "TestCaseCodes", then in this folder, we will create a subfolder for each requirement, not sepcification because there are too many specifications, and too many subfolders can easily lead to confusion. To avoid potential confusion between files, each code file will be named based on the specification it's for, so confusion will be unlikely to occur. 


#### Requirement Problems Documentation:
 - For R1.8, the password complexity check should happen only in register page instead, because at current constraint, the user won't be able to login with invalid password because the register page already checks for password complexity, therefore check password complexity again at login page is unnessary. 
 - For R4.2, there should be an additional constraint that the length of ticket name should be no less than one, otherwise the user would be allow to enter empty ticket name. 

