


After running NKscan for a period of time, working through the differences between python-nmap and libnmap, and benchmarking performance, it became clear that I needed to write a tool that would work through the scans both quickly and in more detail, and allow a user to make the choice.
The script calls through the os library to nmap and masscan, and then parses the output into either xml, txt or html, without attempting to parse through any libraries first, to save system resources and make the running of the script more efficient.  At this point the script cannot output masscan results directly to html (there are some technical reasons for this having to do with the absence of stylesheet differentiation in the masscan xml results).  I recommend using the Masscan Web UI developed by Offensive Security for the display of xml files (https://github.com/offensive-security/masscan-web-ui)
  

This update to the NKscan project is based on attempting to balance these demands.  This updated version runs one of two different functions, chosen by the user.  The first scan configuration is based on a simple os call to masscan, which will scan the network at really fast speeds and grab banners from services, but will not footprint the services in detail.  The second scan configuration is based in the python-nmap library, with the goal being the most detailed results possible, albeit at a much slower rate.

The speed of the scans, specifically, with the masscan option, will be dependent on the speed and bandwidth of the connection that the scans are running through.  From a domestic connection, running through a VPN the masscan scans are taking around 4-5 hours to run completely, while the nmap scans can easily take twice as long if not more.  If a user is able to access a gigabyte internet connection this time will be cut significantly, if running straight to the internet, without the VPN in between.  

This project is the result of months of research and scanning of the externally facing North Korean internet, which is around 1500 IP addresses.  The wider project was undertaken both to learn how to more effectively learn to use nmap on large networks, but also to explore the uses of technical tools in developing political analysis, even in conditions where information is often distorted and limited.

Through this project I have collected dozens of scan results, using various nmapoption configurations, and have come to what I have found to be the most bountiful and robust results.  These scans have a number of hurdles to overcome.  Firstly, information on North Korea is extremely limited, and the information about technicalinfrastructure is even more limited.  Secondly, at times of heightened tensions on theKorean peninsula certain types of scans tend to be blocked, systems are taken off line, and firewalls become tightened up, making the extraction of results difficult. This and other complications have made this project difficult to undertake, and many weeksof experimentation has gone into the development of the scan process outlined in this script.


When these obstacles are overcome, however, the results can provide an interesting insightinto the mentalities, conflictual posture and security approaches of a regime that thoseon the outside have little understanding of.  Often these scans are done around times of tension, and a lot of oddly numbered open ports are observed coming from limited IP ranges. When compared to scans that attempted to geolocate these IPs, which are located outside of Pyongyang and near a large military base, and when compared to scans in times of lower tension, where the same number of open onddly numbered ports do not appear, this can provide the basis to examine past North Korean digital operations, and correlate data.  This is one
of many points of data that came from this research


Some notes on the options selected:

Masscan:
-c : Allows the scan to run from a configuration file, which allows for much better option control.

Within this file the following options are set:

	rate: The rate of packet transmission
	ports: Sets the scan to scan all ports
	range: Sets the IP ranges to scan
	adapter-ip: Sets the IP that the scan will run its dedicated TCP/IP stack as (masscan creates 
				its own TCP/IP stack and is allocated an IP address).
	capture: Sets the scan to capture banners, certs, html and scan for heartbleed vulnerabilities


NMAP:
-n : Prevents nmap from attempting to resolve DNS for each IP.  Given the internal structure of 
what can aptly be described as an intranet in North Korea, there are few DNS entries to begin 
with, and this option makes the scan significantly more efficient.

-sT : TCP scans seem to work better than SYN or ACK scans.  This is likely due to a security
configuration that blocks all SYN and ACK scans, and only allows full TCP connections.  It is 
less stealthy, but it works more consistently than other options.

-A : Information can be difficult to gather, due to specific configurations, odd ports, out
of date software and so on, and using aggressive scanning allows for the maximum amount of
information to be gathered without resorting to using numerous NSE scripts (though awesome, NSE 
scripts take a long time to run, depending on the script and number being run)

-p 1-65535: I scan the entire port range for a simple reason, sketchy stuff tends to run on high
numbered ports outside of common ports.  Part of this project is to understand North Korean digital
operations in relation to the outside world, and to understand internal technical infrasture, and 
this work often involves anomaly detection and comparative analysis.  Scanning uncommon ports is 
useful in this sort of analysis.

-vvv : Often these scans will terminate without warning, and it is important to understand why this 
may be the case.  Though the output will not display when running the script, it will display errors
in the text file output file that is generated during the scan.  The use of robust verbosity during 
scans helped identify forms of blocking, delays in traffic, the blocking of IP addresses I was scanning
from and so on.

-T45: Throttling the scan to level 4 is purely for efficiency.  I have also found that the scan is less 
likely to be blocked if it runs quickly.


Dependencies:
masscan
https://github.com/robertdavidgraham/masscan

nmap



Configuration:
The masscan function runs off of a configuration file (nkscan.conf).  Masscan runs its own tcp/ip stack and, as such, is allocated an IP address.  In the configuration file the user can set the local IP that the scan will configure itself to run through.  Personally, I run scans of North Korea through a VPN, but I would also recommend setting a local IP that is not concurrent with the machines on your network that are live, just for some added security. 

If you are running Masscan Web UI I have found that the best results come from running through the instructions posted by Offensive Security, then making the following changes.

At the end of the setup:

mkdir results (this keeps the date stamped results organized if you ever want to reference them again)
php import.php results/results_file
service apache2 start

In Browser:
localhost/index.php



usage: A Simple Script To Gain Some Insight Into The Hermit Kingdom
       [-h] [--masscan_xml] [--masscan_txt] [--nmap_xml] [--nmap_txt]
       [--nmap_html]

optional arguments:
  -h, --help     show this help message and exit
  --masscan_xml  Run masscan and output into xml format
  --masscan_txt  Run masscan and output into txt format
  --nmap_xml     Run nmap and output into xml format
  --nmap_txt     Run nmap and output into txt format
  --nmap_html    Run nmap and output into html format


''''
