# gymbot
This was a bot I created to book gym time slots during the pandemic. 
Now that my location mandates a 10 person limit to the gym at a time, it's been much harder to 
schedule a gym session. The gym opens slots every day at midnight for the day that is 2 days away. I went on once to see how 
fast they get booked and saw that it took less than 10 minutes for all the slots to be fully booked, so I decided to make a bot since
I don't want to stay up until midnight every night to book a gym session especially when I need to wake up early.

This bot is made mostly through selenium and made specifically for the Fit4Less booking system. It may be helpful as a template for creating similar bots but the 
navigation will need to be adjusted appropriately.


## Installation

### Step 1
Download this zip and make sure you have a [chromedriver](https://chromedriver.chromium.org/) that corresponds to your current google chrome version. 
### Step 2
Then install the `requirements.txt` with `pip` as follows:

`pip install -r requirements.txt`

### Step 3
Adjust the `.bat` file to have the appropriate path

```
call C:\path\to\Anaconda3\Scripts\activate.bat C:\path\to\Anaconda3
cd C:\path\to\gymbot
C:\path\to\python.exe "C:\path\to\project\gymbot.py" 
pause
```


### Step 4 
Open up Task Scheduler on Windows or an equivalent scheduler for your OS.
1. Click Create Basic Task at the right window.
![Task Scheduler](https://github.com/michaelarman/gymbot/blob/main/images/tasksched.PNG)
2. Choose your trigger time and how often to trigger.
3. Start a program - browse to the `.bat` file
![Action](https://github.com/michaelarman/gymbot/blob/main/images/action.PNG)
4. Insert your program script where you saved your bat file earlier.
5. Click Finish.


