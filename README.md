# social-engineering-attack-wifi
Social Engineering Attack Using Phishing in a Local Area Wi-Fi by Creating an Access Point and DNS Manipulation

# **WIFI Social Engineering Attack**
This project was part of a sensitization programme to inform students in my university on the dangers of connecting to unknown wifi networks. The project involved cloning The university's wifi captive portal and serving it on my Kali Linux laptop. A fake access point was setup and DNS requests were spoofed the cloned website IP address on the network.

**Cloning The Project**

*Requirements*

 - You will need a linux OS with hostapd and dnsmasq installed
 - The website was made with Flask so ou will need to have python installed
 
 *Running the Project*
 
 - Open a terminal window in the the directory the project was cloned and run the following command
 `$ python hostap.py`
 - Open another terminal window in the the directory the project was cloned and run this command
 `$ python dnsmasq.py`
 
 - Finally, run the website on another terminal
 `$ python portal_server.py`
 
 *Login details of victims will be recorded in the sniffed_details.txt
   file*
