Hey there anyone who finds this page!

Welcome to the page, please look at the Tutorial-Readme file for any quirks and oddities needed to make the program run!
pardon our dust its still a work in progress!

Regards

Team Super Happy Automation Time


Tutorial
Chat bot Configuration:
	Using the previously designed chat bot in class the only additions that were added are listed below and updating the token and ngrok address to allow the bot access to our webex chat.
Individual skills will have to be imported from separate files or configured within the bot. We put the vast majority of our skills in separate files in the same directory for the sake of readability.

![image](https://user-images.githubusercontent.com/60437398/145248545-28bf2d17-ff2d-485f-a20e-3fc61d649f46.png)

Ansible Skill Tutorial:	
Key Item to Install for ansible chat bot skill to function:
Ansible_playbook_runner via pip 3
The Ansible Skill required some outside sourcing to find a way to run, in this case a user made library was imported to run the yaml commands that make up Ansible

![image](https://user-images.githubusercontent.com/60437398/145248586-d71b8d29-ed97-48ce-8958-d4691b1061ca.png)

Once that was imported a simple definition was added so that a chat bot command could be added to the list, as the playbook needs an inventory both the book and inventory had to be specified within the command to function.  In a more flexible bot adding in a user input to change the inventory and play book would be the next step in evolving the bot.

![image](https://user-images.githubusercontent.com/60437398/145248617-c2270ad0-fc17-4cbd-b610-29557bebf8db.png)

The calls for this is a simple “backup” or “create backup of current config” while the bot does not display the output it does save them in a designated backups folder.

Genie Robot Skill Tutorial:
For the genie skills to function, we needed to import the genie robot library:

![image](https://user-images.githubusercontent.com/60437398/145248639-63671e34-db71-45a6-87a3-dec98195cab3.png)

We defined the robot skills in separate. robot files:

![image](https://user-images.githubusercontent.com/60437398/145248661-1673fbd8-10f5-4cac-8ad8-9536c2a2298b.png)

![image](https://user-images.githubusercontent.com/60437398/145248676-9c5d8642-0c09-4db6-ae8d-3157a8983db0.png)

These are simple robot frameworks, taken almost directly from in-class labs. The only alterations specify that saved snapshots be saved within the backups directory.
Within the actual chatbot code, we needed to define functions that the chatbot could call:

![image](https://user-images.githubusercontent.com/60437398/145248725-21ed0e87-74b3-4e76-8d70-5e204da95133.png)

The robot.run() command allows the python code to execute a genie robot framework. Lastly, within the chatbot code, I had to define the user input that would cause the bot to execute the functions which would execute the genie robot frameworks: 

![image](https://user-images.githubusercontent.com/60437398/145248742-6bddc518-231c-4d32-833a-cfd0440662ac.png)

Netconf/Netmiko Skills:
As stated before, the Netconf and Netmiko skills were imported from separate files. 

![image](https://user-images.githubusercontent.com/60437398/145248759-64859516-6f1a-4856-8bc8-c14809a1e7da.png)

The Netconf file was defined in the separate netconf_loopback file. 

![image](https://user-images.githubusercontent.com/60437398/145248835-9f30705f-7853-491a-9825-cfc6cea503ab.png)

The Netmiko file was defined in the separate netmiko file.

![image](https://user-images.githubusercontent.com/60437398/145248862-6439981b-6b1f-4eec-825d-10ff9ee9a1d3.png)

The functions defined in the separate files are then called within the bot.

![image](https://user-images.githubusercontent.com/60437398/145248894-79423eaa-680c-41ed-9afb-aef846ee95d1.png)


The Netconf skill creates a loopback on each of the two routers. The Netmiko skill runs the show interface brief on both of the routers. 
