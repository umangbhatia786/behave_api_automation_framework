Feature: Verify that User is able to get book details

  @regression
  Scenario: TC02_Verify_GetBook_API_Functionality_ByID
    When We execute the Get Book Resource for Library API providing ID as query parameter
    Then Verify Response Code is 200
    Then Verify JSON Schema of the Response returned
    Then Verify Book Name is same as provided
    Then Verify ISBN is same as provided
    Then Verify Aisle is same as provided
    Then Verify Author Name is same as provided

  @regression
  Scenario: TC03_Verify_GetBook_API_Functionality_ByAuthor
    When We execute the Get Book Resource for Library API providing Author Name as query parameter
    Then Verify Response Code is 200
    Then Verify JSON Schema of the Response returned
    Then Verify Book Name is same as provided
    Then Verify ISBN is same as provided
    Then Verify Aisle is same as provided
