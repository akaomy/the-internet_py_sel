Feature: Positive test cases for login page

Background: User navigates to login page
	Given I navigate to "login_page" page

Scenario: User is able to login with valid credentials and then logout
   Given I enter valid "tomsmith" username
   And I enter valid "SuperSecretPassword!" password
   And I click on "login" button
   Then I should see "You logged into a secure area!" success login message
   Then I click on "logout" button
   And should see "You logged out of the secure area!" success logout message
   Then I close "browser"
