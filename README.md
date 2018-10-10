# sublist
quick and easy, no frills subdomain enumeration using crt.sh

# about
sublist quickly enumerates subdomains while querying crt.sh.  the tool is useful for penetration testers, threat hunters, bug bounty hunters, and anyone else looking to enumerate their external posture.  

this list can be used to feed into eyewitness or any other tool used in the OSINT process.

# screenshot
![screengrab](https://github.com/murpsec/sublist/blob/master/sublist_screen.png)

# installation and usage 
*sudo git clone https://github.com/murpsec/sublist.git* <br>
*cd sublist* <br>
*sudo python3 sublist.py* <br>

You have to ability to save the output as a txt file.  If you chose this option, it will be in the directory in which sublist was ran.

# python version
sublist supports python 3.x

# dependencies
beautifulsoup4 <br>
to install run - *sudo apt-get install python3-bs4*




