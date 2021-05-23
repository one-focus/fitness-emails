# Created by Alex Kardash at 14/11/2020
@regression
Feature: Main page
  Validate main page

  Scenario: Validate left menu
    Given I open login page
    When I log in
    When I open spam page
    When I remove from spam
    When I open inbox page
    When I read security emails
    When I read all emails
#    When I remove from inbox
