Feature: Login thought authentification pop up
	
	Scenario: Log in to the page with valid credentials
		Given I navigate to the basic auth page
		And I should see "Congratulations! You must have the proper credentials." the success message 
		Then I close the browser
