from ncclient import manager
import xml.dom.minidom

m1 = manager.connect(
    host="192.168.56.102",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>My NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.1.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""

print('#'*80)
netconf_reply = m1.edit_config(target="running", config=netconf_loopback)

m2 = manager.connect(
    host="192.168.56.107",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>My NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.2.2.2</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""

netconf_reply = m2.edit_config(target="running", config=netconf_loopback)
print (xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())