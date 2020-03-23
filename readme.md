To make the file work first you need to go to your google sheets and then create a sheet and remember its name.
Now go to console.cloud.google.com and create an app there.
Once the app is created then go to the library in the left and search for google drive api and then go in it.
Enable it and then on the top right(after enabling) you can see create credentials and fill the details according to you.
Most of them have to be default.Once you will fill the details a json file for your credentials will be downloaded.
Now go back to library and then search for google-sheet api and enable it as well
Now head to you editor.
Install gspread and oauth2client.
Then add that file(jsno) in it and open it.
You will see an email address there.
Copy that email address and then share your sheet with the mentioned email.
Now create a python file, one similar to the one i have created,in the same directory and code as given in it.
Change the details as asked and then run the file you will see the appropriate outputs.