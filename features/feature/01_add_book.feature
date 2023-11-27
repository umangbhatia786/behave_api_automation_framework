Feature: Verify that User is able to Add a new book

  @regression
  Scenario: TC01_Verify_Add_Book_API_Functionality
    When We execute the Add Book Resource for Library API
    Then Verify Response Code is 200
    Then Verify JSON Schema of the Response returned
    Then Verify that success message is returned in Response JSON
    Then Verify that ID generated is concatenation of ISBN and Aisle