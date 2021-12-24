Feature: The user can add and delete pay grades
  @fixture.drive
Scenario: The user can add and delete pay grade with name Smith in canadian dollars with minimum ammount 1500 and maximum ammount 3000
Given the user is on the login page
When the user logs in
And the user opens Pay Grades tab
And the user adds new record
Then check for existence
When the user opens Pay Grades tab
And the user deletes this record
Then check for absence