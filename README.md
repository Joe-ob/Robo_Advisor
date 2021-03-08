# Robo_Advisor

Start by cloning the repo on the Github website. Click the green "Code" button and choose a method to download the file. Ideally, you have the github desktop downloaded and can use that. Save it somewhere you will remember such as your Desktop. Once you have the file, open it in your terminal by going into the terminal and entering "cd ~/Desktop/Robo_Advisor".

Then create a local environment by entering "conda create -n stocks-env python=3.8"

Once you create the environment, you can activate it at any time by entering "conda activate stocks-env"

Next, go into Visual Studio Code (in your github desktop, go to the top bar and hit 'Repository' then 'Open in Visual Studio Code'). Create a file called ".env" by left clicking on the Editor on the left side of the window.
When you create that file, inside you will enter ( ALPHAVANTAGE_API_KEY="abc123" ) with your personal api key inside the parenthesis.

Then, go back to your terminal and enter "pip install -r requirements.txt" to load the proper programs. You only need to do this once.

Now you are ready to use the program. Enter "python app/robo-advisor" into the terminal to begin.