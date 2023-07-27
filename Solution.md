# btwanswerd
Tech test for Between

Basically I have added a function to the API (todo_to_csv) and completed the function "run".

In the "run" function I get from the url provided two things:
first the response of the page, in case of status 200 I get the response of the page in JSON format and I run through the elements one by one passing them to the todo_to_csv function.

In the todo_to_csv function I create the file name from the ID, make sure that "storage" exists and then use the csv library to save the file in its place.
