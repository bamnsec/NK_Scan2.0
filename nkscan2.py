import os
import argparse
import datetime

print """


         _             _             _             _             _                   _               _              _
        /\ \     _    /\_\          / /\         /\ \           / /\                /\ \     _     /\ \           / /
       /  \ \   /\_\ / / /  _      / /  \       /  \ \         / /  \              /  \ \   /\_\  /  \ \         / /  
      / /\ \ \_/ / // / /  /\_\   / / /\ \__   / /\ \ \       / / /\ \            / /\ \ \_/ / / / /\ \ \       / / /\ 
     / / /\ \___/ // / /__/ / /  / / /\ \___\ / / /\ \ \     / / /\ \ \          / / /\ \___/ /  \/_/\ \ \     / / /\ \ 
    / / /  \/____// /\_____/ /   \ \ \ \/___// / /  \ \_\   / / /  \ \ \        / / /  \/____/       / / /    /_/ /  \ \ 
   / / /    / / // /\_______/     \ \ \     / / /    \/_/  / / /___/ /\ \      / / /    / / /       / / /     \ \ \   \ \ 
  / / /    / / // / /\ \ \    _    \ \ \   / / /          / / /_____/ /\ \    / / /    / / /       / / /  _    \ \ \   \ \ 
 / / /    / / // / /  \ \ \  /_/\__/ / /  / / /________  / /_________/\ \ \  / / /    / / /       / / /_/\_\ _  \ \ \___\ \ 
/ / /    / / // / /    \ \ \ \ \/___/ /  / / /_________\/ / /_       __\ \_\/ / /    / / /       / /_____/ //\_\ \ \/____\ \ 
\/_/     \/_/ \/_/      \_\_\ \_____\/   \/____________/\_\___\     /____/_/\/_/     \/_/        \________/ \/_/  \_________\/


"""


parser = argparse.ArgumentParser("A Simple Script To Gain Some Insight Into The Hermit Kingdom")

parser.add_argument('--masscan_xml', help = 'Run masscan and output into xml format', action = 'store_true')
parser.add_argument('--masscan_txt', help = 'Run masscan and output into txt format', action = 'store_true')
parser.add_argument('--nmap_xml', help = 'Run nmap and output into xml format', action = 'store_true')
parser.add_argument('--nmap_txt', help = 'Run nmap and output into txt format', action = 'store_true')
parser.add_argument('--nmap_html', help = 'Run nmap and output into html format', action = 'store_true')

args = parser.parse_args()
masscan_xml = args.masscan_xml
masscan_txt = args.masscan_txt
nmap_xml = args.nmap_xml
nmap_txt = args.nmap_txt
nmap_html = args.nmap_html

filename = str(datetime.date.today())

def masscan_xml():
    mx = str(filename + "masscan" + ".xml")
    mx1 = str(filename + "masscan1" + ".xml")
    mx2 = str(filename + "masscan2" + ".xml")
    print "[*]Starting Scan"
    os.system('masscan -c NKscan.conf --interactive -oX %s' % mx)
    os.system('masscan -c NKscan1.conf --interactive -oX %s' % mx1)
    os.system('masscan -c NKscan2.conf --interactive -oX %s' % mx2)
    print "[*] Scan Completed"

def masscan_txt():
    mt = str(filename + "masscan" + ".txt")
    mt1 = str(filename + "masscan1" + ".txt")
    mt2 = str(filename + "masscan2" + ".txt")
    print "[*]Starting Scan"
    os.system('masscan -c NKscan.conf --interactive -oL %s' % mt)
    os.system('masscan -c NKscan1.conf --interactive -oL %s' % mt1)
    os.system('masscan -c NKscan2.conf --interactive -oL %s' % mt2)
    print "[*] Scan Completed"


def nmap_xml():
    nx = str(filename + "nmap" + ".xml")
    print "[*] Starting Scan"
    os.system('nmap -n -sT -A -p 1-65535 --script discovery -vvv -T5 -iL list.txt -oX %s' % nx)
    print "[*] Scan Completed"

def nmap_txt():
    nt = str(filename + "nmap" + ".txt")
    print "[*] Starting Scan"
    os.system('nmap -n -sT -A -p 1-65535 --script discovery -vvv -T5 -iL list.txt -oN %s' % nt)
    print "[*] Scan Completed"

def nmap_html():
    nh = str(filename + "nmap" + ".xml")
    nc = str(filename + "nmap" + ".html")
    print "[*] Starting Scan"
    os.system('nmap -n -sT -A -p 1-65535 --script discovery -vvv -T5 -iL list.txt -oX %s --stylesheet /usr/share/nmap/nmap.xsl' % nh)
    print "[*] Scan Completed"
    print "[+] Converting to HTML"
    os.system('xsltproc %s -o %s' % (nh, nc))


if args.masscan_xml:
    masscan_xml()

if args.masscan_txt:
    masscan_txt()

if args.nmap_xml:
    nmap_xml()

if args.nmap_txt:
    nmap_txt()

if args.nmap_html:
    nmap_html()

print('----------------------------------------------------')
print ""
print ""
print "The Scan Has Completed"
print ""
print "The Great Leader Honors and Praises You"
print """
                                   `.'''''.                                
                              .@@@@@@@@@@@@@;                              
                             :@@@;@@;    @@@@'                             
                            @@@.@ .`,+` '.@@@@                             
                           @@:  @@@@@@@@; .;@@+                            
                          ;@@'#@#     :+@@`@@@;                            
                          @@# @`          @@@@+                            
                          #@@@:           @@@@@                            
                           #@@             ,@@@                            
                   #@       @@              .@@                            
                  @@@      ,@   `   '@;;     @@                            
                 @@#@@     :@         `     ;@@@                           
                 @ :@@     :@  :@@  @.`..`  ;;@@                           
                @@ @#@     +@ ..'; + ,     ;@ @@                           
               #@ ;'@@     #@      #`     @+  @@                           
              `@ .':@      #@   `. ' @    ` , @@                           
              @+ +;,@:     #@   @',#@ #  +   :@                            
             ;@ @#`'@@@    #@  ,.     :    `@@                             
             @; ;  `@@@;   +@, `'''+.@;    `@@                             
            ;@  .# @ `@`   '@@   ';+.     . @@                             
            @# :@' , ;@     @@    . `   @ @ @@                             
           .@,  @    @:     @@'   @@#,  .` `@@                             
           :@   @   ++      ,@@+.      @   @@@                             
           ;@   @   @.       @@@@'   :@  `@.:@+,                           
           @'      @.         ;@#; +'   :@   @@@@@@@+                      
           @+ ,`',@@:           @@`@@@ @'    @,,,#@@@@@@                   
          #@.  `'@@       :+'#@@; @  '#     @      .'@@@@@,                
         ;@@   `@@   `:+@@@@@@@@   :#      ,+          +@@@@               
         @ #;  ,@@``@@@@@@'..`+,  :@@;    `@             ,@@               
        @    ';@@@ ;@        @`   @;@@   '@               #@`              
       ,'  , @@ @; @+       +@`  '@:@@@:'`               :@@@`             
       @   `.:  @# @        @@@@;#   @@@                 @ @@@             
      +#  .'#  .@@@@.        +@@@                       '  #@@@            
      @   `;@ `'@@@:                                    ;@'  @@            
     .@     ,` `;@`                       #@@'        `@@  , @@#           
     +@    ` `: '                ,:      @`  '@       :# ,'   @@,          
     #@    '@  .                 # '.    @,   @       @`@`    '@@          
     @@   #@   +    `@@;         ;#      ;+@@##       @,       @@@         
     @@  @@     ;  :@@@@@@@@`            :@@@@@@@@@@ .@;        @@@        
     @@ .'      +  @,  :'@@@@           :#++';###+@@``@@         @@;       
     @#   :+ +  +  @       @@           @'        `@. @@         `@@       
     @@ @.  @ . # '@@`     @:           @@         @  ;@,         @@,      
     @@@   @#,  #  @@@@@@@@;            @@@@@@@@@@@'  @@@         .@@      
     @@@ :@' `  @   +####'               +'''''++::   @@@          @@:     
    ``@@@@@#@,,:@               #'                     @@      ##:.:@@     
       +@@@@@@@'               ' ,'                    @+:          @@;    
            .@@@@                                                   :@+    
              '@@@                                                   @@    
                @#                                                   @     
                `                                                          
                                                                           
                                                                           
"""
