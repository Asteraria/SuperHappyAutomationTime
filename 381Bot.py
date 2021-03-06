### teams Bot ###
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
### Utilities Libraries
import routers
import robot
import useless_skills as useless
import useful_skills as useful
from netconf_loopback import create_loopbacks 
from netmiko_int import int_brief
from ansible_playbook_runner import Runner

# Router Info 
device_address = routers.router['host']
device_username = routers.router['username']
device_password = routers.router['password']

# RESTCONF Setup
port = '443'
url_base = "https://{h}/restconf".format(h=device_address)
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Bot Details
bot_email = '381NetBot@webex.bot'
teams_token = 'MzE1MzRkNzEtNWM2NS00OWI3LWFjYzYtOGIyMDU3NDQwNDI3MzE5ZDNmZTYtNzQ0_P0A1_529b5ae9-ae34-46f8-9993-5c34c3d90856'
bot_url = "https://753c-144-13-254-51.ngrok.io" 
bot_app_name = 'Steve'

# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},],
)

# Create a function to respond to messages that lack any specific command
# The greeting will be friendly and suggest how folks can get started.
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Hello {}, I'm a friendly CSR1100v assistant .  ".format(
        sender.firstName
    )
    response.markdown += "\n\nSee what I can do by asking for **/help**."
    return response

def arp_list(incoming_msg):
    """Return the arp table from device
    """
    response = Response()
    arps = useful.get_arp(url_base, headers,device_username,device_password)

    if len(arps) == 0:
        response.markdown = "I don't have any entries in my ARP table."
    else:
        response.markdown = "Here is the ARP information I know. \n\n"
        for arp in arps:
            response.markdown += "* A device with IP {} and MAC {} are available on interface {}.\n".format(
               arp['address'], arp["hardware"], arp["interface"]
            )

    return response

def sys_info(incoming_msg):
    """Return the system info
    """
    response = Response()
    info = useful.get_sys_info(url_base, headers,device_username,device_password)

    if len(info) == 0:
        response.markdown = "I don't have any information of this device"
    else:
        response.markdown = "Here is the device system information I know. \n\n"
        response.markdown += "Device type: {}.\nSerial-number: {}.\nCPU Type:{}\n\nSoftware Version:{}\n" .format(
            info['device-inventory'][0]['hw-description'], info['device-inventory'][0]["serial-number"], 
            info['device-inventory'][4]["hw-description"],info['device-system-data']['software-version'])

    return response

def get_int_ips(incoming_msg):
    response = Response()
    intf_list = useful.get_configured_interfaces(url_base, headers,device_username,device_password)

    if len(intf_list) == 0:
        response.markdown = "I don't have any information of this device"
    else:
        response.markdown = "Here is the list of interfaces with IPs I know. \n\n"
    for intf in intf_list:
        response.markdown +="*Name:{}\n" .format(intf["name"])
        try:
            response.markdown +="IP Address:{}\{}\n".format(intf["ietf-ip:ipv4"]["address"][0]["ip"],
                                intf["ietf-ip:ipv4"]["address"][0]["netmask"])
        except KeyError:
            response.markdown +="IP Address: UNCONFIGURED\n"
    return response
def Backups(incoming_msg):
    Runner(['hosts'], 'backup_router_playbook.yaml').run()
    return "Backup Config successfully saved."
def loopmaker(incoming_msg):
    create_loopbacks
    return "Loopback interfaces created."
def showIPINTBR(incoming_msg):
    int_brief
    return "Check terminal."
#Function to execute robot framework 1
def takeScreenshot(incoming_msg):
    robot.run("initial_snapshot.robot")
    return "Screenshot taken successfully. For more information, check the robot_initial directory"

#Function to execute robot framework 2 
def compareScreenshot(incoming_msg):
    robot.run("compare_snapshot.robot")
    return "Comparison made. For more information, check the robot_compare directory."
# Set the bot greeting.

bot.set_greeting(greeting)

# Add Bot's Commmands
bot.add_command(
    "arp list", "See what ARP entries I have in my table.", arp_list)
bot.add_command(
    "system info", "Checkout the device system info.", sys_info)
bot.add_command(
    "show interfaces", "List all interfaces and their IP addresses", get_int_ips)
bot.add_command("attachmentActions", "*", useless.handle_cards)
bot.add_command("showcard", "show an adaptive card", useless.show_card)
bot.add_command("dosomething", "help for do something", useless.do_something)
bot.add_command("time", "Look up the current time", useless.current_time)
bot.add_command("Backup","Create backup of current config",Backups)
bot.add_command("Take snapshot", "Take a snapshot of current configuration using genie robot", takeScreenshot)
bot.add_command("Compare snapshot", "Compare current snapshot of configuration with good snapshot", compareScreenshot )
bot.add_command("create loopbacks", "create loopback interfaces.", loopmaker)
bot.add_command("show int brief", "run show ip interface brief command", showIPINTBR)
# Every bot includes a default "/echo" command.  You can remove it, or any
bot.remove_command("/echo")

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
