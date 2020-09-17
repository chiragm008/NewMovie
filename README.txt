---------------------INSTRUCTIONS TO RUN THE TESTS-----------------------

STEPS:
1. Open command prompt or Terminal of the IDE/Editor at the location: "  \HybridALL\feature"
2. Execute the following command: pytest -v --html=report.html
    It will execute all the scripts starting with name "test_" and all the test case method inside it starting with "test_".
    It will also generate a report with the name "report.html" and will be saved in the same location.

Command to run the API tests        > pytest -v --html=report.html test_API.py
Command to run the UI tests         > pytest -v --html=report.html test_UI.py
Command to run all the tests        > pytest -v --html=report.html

UI Tests:
1. Check if the dashboard is loading properly
2. Check if the Country button is working fine from dashboard
3. Check search text box by entering Partial Country name
4. Check search button is clicable
5. Check if specific Country is clicable
6. Verify the Country page loads fine

7. Check if the Cities button is working fine from dashboard
8. Check if specific City is clicable
9. Verify the City page loads fine

10. Check if the Movies button is working fine from dashboard
11. Check search text box by entering Partial Movie name
12. Check search button is clicable
13. Check if specific Movie is clicable
14. Verify the Movie page loads fine

15. Check if the Shows button is working fine from dashboard
16. Check search text box by entering Partial Show name
17. Check search button is clicable
18. Check if specific Show is clicable
19. Verify the Show page loads fine

20. Check if the Continent button is working fine from dashboard
21. Check search text box by entering Partial Continent name
22. Check search button is clicable
23. Check if specific Continent is clicable
24. Verify the Continent page loads fine


API Tests:
1. Test Countries with ID: Test the "Counties" end point by fetching the details of a specific country using the Countries_ID and verify the value using assert.
2. Test Search: Test the "Movie Search" end point by fetching the search results of a specific search text.
3. Test Cities with ID: Test the "Cities" end point by fetching the details of a specific city using the Cities_ID and verify the value using assert.
4. Test Movies with ID: Test the "Movies" end point by fetching the details of a specific Movie using the Movies_ID and verify the value using assert.
5. Test Shows with ID: Test the "Shows" end point by fetching the details of a specific Shows using the Shows_ID and verify the value using assert.
