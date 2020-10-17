##### Table for R2

| Specification                                                | Test case ID | Purpose                                                      |
| ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ |
| If the user has logged in, redirect back to the user profile page / | R2.1         | Check if the page will be redirected to the user profile page when the user has logged in |
| If the user has not logged in, show the user registration page | R2.2         | Check if the registration page will be shown if the user has not logged in |
| the registration page shows a registration form requesting: email, user name, password, password2 | R2.3         | Check if the registration page shows a registration form requesting related parameters |
| The registration form can be submitted as a POST request to the current URL (/register) | R2.4         | Check if the registration form can be submitted as a POST request to the current URL |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.5         | Check if the registration parameters are inputted as required formats |
| Password and password2 have to be exactly the same           | R2.6.1       | Check if the registration actions succeed when the password and password2 are identical |
| Password and password2 have to be exactly the same           | R2.6.2       | Check if the registration actions fail when the password and password2 are not identical |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character | R2.7.1       | Check if the registration actions succeed with proper user name |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character | R2.7.2       | Check if the registration actions fail with improper user name |
| User name has to be longer than 2 characters and less than 20 characters | R2.8.1       | Check if the registration actions succeed with proper user name |
| User name has to be longer than 2 characters and less than 20 characters | R2.8.2       | Check if the registration actions fail with improper user name |
| For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute) | R2.9         | Check if the page will be redirected to login page and show respective message when formatting errors occur |
| If the email already exists, show message 'this email has been ALREADY used' | R2.10        | Check if the page shows respective when the registration email has already been used |
| If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page | R2.11        | Check if the new user will be created, balance will be set, and page be redirected to /login page if no errors occur regarding the inputs |

##### Table for R5

| Specification                                                | Test case ID | Purpose                                                      |
| ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ |
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character | R5.1.1       | Check if the updating actions succeed with proper ticket name inputted |
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character | R5.1.2       | Check if the updating actions fail with improper ticket name inputted |
| The name of the ticket is no longer than 60 characters       | R5.2.1       | Check if the updating actions succeed with ticket name in proper length |
| The name of the ticket is no longer than 60 characters       | R5.2.2       | Check if the updating actions fail with ticket name not in proper length |
| The quantity of the tickets has to be more than 0, and less than or equal to 100 | R5.3.1       | Check if the updating actions succeed with ticket quantity in proper range |
| The quantity of the tickets has to be more than 0, and less than or equal to 100 | R5.3.2       | Check if the updating actions fail with ticket quantity not in proper range |
| Price has to be of range [10, 100]                           | R5.4.1       | Check if the updating actions succeed with the price in proper range |
| Price has to be of range [10, 100]                           | R5.4.2       | Check if the updating actions fail with the price not in proper range |
| Date must be given in the format YYYYMMDD                    | R5.5.1       | Check if the updating actions succeed with date inputted in proper format |
| Date must be given in the format YYYYMMDD                    | R5.5.2       | Check if the updating actions fail with date inputted not in proper format |
| The ticket of the given name must exist                      | R5.6.1       | Check if the updating actions succeed with a given name that exists |
| The ticket of the given name must exist                      | R5.6.2       | Check if the updating actions fail with a given name that does not exist |
| For any errors, redirect back to / and show an error message | R5.7         | Check if the page will be redirected to / and error message will be shown when any error occurs |

##### Test Plan:

1. Method to organize the documentation of test cases:

- We created a folder named "TestCases" in our repository, and each team member will create a subfolder that contains two markdown files: the test cases written in nature language, and test tables that summarize the test cases.

2. How the chosen testing frameworks to test the frontend, and when and how the test cases will be running directly on GitHub

- The testing framework tells the developer what to test for and how the software should behave.
- The test case will run each time a unit test is required. The first time that test cases need to run is the end of prototyping stage.

3. How to organize different test case code files? 

- We created a folder name "TestCaseCodes" in the repository, and we will create subfolders for different requirements to organize different test case code files and avoid further confusion by setting up our naming convention for the folders.