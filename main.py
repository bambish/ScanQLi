import function
import requests
import time
import config
from termcolor import colored

# url = "http://challenge01.root-me.org/web-serveur/ch18/"
# url = "http://challenge01.root-me.org/web-serveur/ch9/"
# url = "http://challenge01.root-me.org/web-serveur/ch19/"
# url = "http://challenge01.root-me.org/web-serveur/ch49/"
# url = "http://challenge01.root-me.org/web-serveur/ch34/"
# url = "http://challenge01.root-me.org/realiste/ch9/" # Web TV
# url = "http://challenge01.root-me.org/web-serveur/ch10/"
# url = "http://challenge01.root-me.org/web-serveur/ch31/" # File reading
# url = "http://styleshit.altervista.org/lvl1.php?id=1"
# url = "http://challenge01.root-me.org/web-serveur/ch40/" # Time base
# url = "http://challenge01.root-me.org/realiste/ch8/" # MALab SQL Blind *

# url = "http://challenge01.root-me.org/web-serveur/ch42/" # GBK *
# url = "http://challenge01.root-me.org/web-serveur/ch30/" # filter
# url = "http://challenge01.root-me.org/web-serveur/ch33/" # Insert *
# url = "http://challenge01.root-me.org/realiste/ch4/index.php"
# url = "http://challenge01.root-me.org/realiste/ch14/?p=news"
# url = "http://challenge01.root-me.org/realiste/ch1/" # False positive

# Cookies
# function.cookies = {"PHPSESSID":"4bn7uro8qq62ol4o667bejbqo3" , "Session":"Mzo6YWMwZGRmOWU2NWQ1N2I2YTU2YjI0NTMzODZjZDVkYjU="}

# Banned URLs
# config.BannedURLs.append("http://challenge01.root-me.org/realiste/ch8/index.php?id=5")
# config.BannedURLs.append("http://challenge01.root-me.org/realiste/ch8/?id=5")

# Quick scan
# config.scantype = "quick"

# init config
config.init()

# Start
starttime = time.time()

baseurl = function.GetCurrentDir(url)
print("Base URL = " + baseurl + "\n")
pageset = function.GetAllPages(baseurl)
print(str(len(pageset)) + " URLs found")
print("----------------------------")

result = function.CheckPageListAllVulns(pageset)
print("----------------------------")
if len(result) <= 1:
    print(colored(str(len(result)) + " vulnerability ", attrs=["bold"])  + "found in " + str(round(time.time() - starttime, 2)) + " seconds!")
    # colored("[GET] ", "green", attrs=["bold"])
else:
    print(colored(str(len(result)) + " vulnerabilities ", attrs=["bold"])  + "found in " + str(round(time.time() - starttime, 2)) + " seconds!")