Feature: Verify that User is able to delete book details

  @regression
  Scenario: TC04_Verify_DeleteBook_Functionality
    When We execute the Delete Book Resource for Library API
    Then Verify Response Code is 200
    Then Verify JSON Schema of the Response returned
    Then Verify the message property

  @regression
  Scenario: TC05_Verify_DeleteBook_For_Already_Deleted_Book
    When We execute the Delete Book Resource for Library API
    Then Verify Response Code is 404
    Then Verify JSON Schema of the Response returned
    Then Verify the error message in message property