Feature: The user can upload, delete and get metadata
  @fixture.drive
Scenario: the user uploads a file
Given logged in dropbox
When user uploads
Then check for existence

Scenario: the user gets metadata
Given logged in dropbox
When the user gets metadata
Then check metadata

Scenario: the user deletes a file
Given logged in dropbox
When user deletes
Then check for absence