# Discord Automater

**Important instructions**

Please read this before invoking the automater. All values taken were from full-screen Discord on a 13-inch 2560 x 1600 screen. Before you invoke the bot, please change the values so that the autoclicker clicks on the correct part of your specific screen. 

In order to use the code, you must have the library `pyautogui` installed. 

If ever the automator is not working as intended, put your mouse at one of the corners of your screen, and the program will stop. 


## Code

`automator.py` must be succesfully invoked with the following command:

`python automator.py -t 'type'`. The bot has the following functions: 
- 'pos' to return position
- 'delete' to delete channels
- 'rolesync' to reset channel permissions to its category
- 'deleterole' to delete roles
- 'text' to create text channels
- 'desc' to add channel topic to text channels
- 'voice' to create voice channels

When `-t 'pos'`, the automator will return the position of your mouse. Adjust the position of your mouse to the location you want, press Alt-Tab/Cmd-Tab to reach your terminal, and run `python automator.py -t 'pos'` to get your mouse position. This allows you to change autoclicker values. 


When `-t 'delete'`, the automator will delete a specified number of consecutive channels in the server. You have to provide the additional arguments `-n 'number of channels' -x 'starting x coordinate for channel to delete' -y 'starting y coordinate for channel to delete'`. Without these arguments, the bot will fail to work. 

With these arguments, you provide it with the (x,y) of the first channel, and the number of channels you want to delete afterwards. The bot will keep deleting in place. Assuming you have enough channels below, the starting x and y coordinate should not change as you delete channels. However, if there are channels roles below, the menu will start to shift down, and you will start to delete higher roles instead. 


When `-t 'rolesync'`, the automator will sync a specified number of channels to its category's permissions. You have to provide the additional arguments `-n 'number of channels' -x 'starting x coordinate for channel to modify permissions' -y 'starting y coordinate for channel to modify permissions'`. Without these arguments, the bot will fail to work. 

With these arguments, you provide it with the (x,y) of the first channel, and the number of channels you want to modify afterwards. The bot will moving downwards as it modifies. Thus, you will only be able to modify as many channels as you see in your screen. Towards the bottom of the screen, since the menu is unable to go below the screen, it will be displaced and the bot will not click on the right button as well. Limit it to channels in the top 7/10 of your screen at once.


When `-t 'deleterole'`, the automator will delete a specified number of consecutive roles in the server roles menu. You have to provide the additional arguments `-n 'number of roles' -x 'starting x coordinate role to delete' -y 'starting y coordinate for role to delete'`. Without these arguments, the bot will fail to work. 

With these arguments, you provide it with the (x,y) of the first role, and the number of roles you want to delete afterwards. The bot will keep deleting in place. Assuming you have enough roles below, this will not be an issue. However, if there are insufficient roles below, the menu will start to shift down, and you will start to delete higher roles instead. 


When `-t 'text'`, the automator will create a specified number of consecutive private text channels in a category. You have to provide the additional arguments `-n 'number of channels' -x 'x coordinate + button in category' -y 'y coordinate + button in category'`. Without these arguments, the bot will fail to work. 

The bot will pause at relevant times for you to input information, like channel name and channel permissions. Move fast, or modify the value `k` in `time.sleep(k)` if you need longer. You automatically open the newest channel you create, which can displace the location of the +. By creating a text channel in the category first, clicking on that text channel and then minimising the category, this prevents the channel list from moving around. 


When `-t 'desc'`, the automator will allow you to input the description of a specified number of consecutive text channels from a Google Sheets column list (21px between cells). You have to provide the additional arguments `-n 'number of channels' -x 'starting x coordinate for channel to modify description' -y 'starting y coordinate for channel to modify description' -x2 'starting x coordinate for description column in spreadsheet' -y2 'starting y coordinate for description column in spreadsheen'`. Without these arguments, the bot will fail to work. 

The bot will pause at relevant times for you copy and paste the information over. Move fast, or modify the value `k` in `time.sleep(k)` if you need longer. The bot will moving downwards as it modifies. Thus, you will only be able to modify as many channels as you see in your screen. Towards the bottom of the screen, since the menu is unable to go below the screen, it will be displaced and the bot will not click on the right button as well. Limit it to channels in the top 7/10 of your screen at once.


When `-t 'voice'`, the automator will create a specified number of consecutive private voice channels in a category. You have to provide the additional arguments `-n 'number of channels' -x 'x coordinate + button in category' -y 'y coordinate + button in category'`. Without these arguments, the bot will fail to work. 

The bot will pause at relevant times for you to input information, like channel name and channel permissions. Move fast, or modify the value `k` in `time.sleep(k)` if you need longer. To add many channels without having the + button move around, minimise the category before running the command. 


