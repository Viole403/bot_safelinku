#Create By Monnalisa-ID
#Bot Safelinku Version BETA
#DECODE = LEMAH!
#Susah Susah Buat Malah di diceode anjg emang!
import time,sys,random,os
from os import system, name 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from multiprocessing.pool import ThreadPool
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
res = Style.RESET_ALL
abu2 = Style.DIM+Fore.WHITE
biru = Style.RESET_ALL+Style.BRIGHT+Fore.BLUE
ungu2 = Style.NORMAL+Fore.MAGENTA
ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
hijau2 = Style.NORMAL+Fore.GREEN
yellow2 = Style.NORMAL+Fore.YELLOW
yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
red2 = Style.NORMAL+Fore.RED
red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
cyan = Style.BRIGHT+Fore.CYAN
cyan2 = Style.NORMAL+Fore.CYAN
des = Style.BRIGHT+Fore.GREEN+"『🔥』"
kur1 = Style.BRIGHT+Fore.RED+"["
kur2 = Style.BRIGHT+Fore.RED+"]"
print(f"""{biru}
╔╗ ┌─┐┌┬┐ ╔═╗┌─┐┌─┐┌─┐┬  ┬┌┐┌┬┌─┬ ┬
╠╩╗│ │ │  ╚═╗├─┤├┤ ├┤ │  ││││├┴┐│ │
╚═╝└─┘ ┴  ╚═╝┴ ┴└  └─┘┴─┘┴┘└┘┴ ┴└─┘With Selenium\n{hijau}Bot Version : BETA\n""")
time.sleep(3)
print('_' * 60)
print (f"""{cyan2}WELCOME TO BOT SAFELINKU\n{red}Created By Monnalisa ID\n{hijau}Contact Me on : https://github.com/Monnalisa-ID\n{red}This Still Version Beta|ComingSoon Version Final""")
time.sleep(5)  

print("\n")
print('=' *60)

time.sleep(1)

kw=input(f"{cyan}Enter Link Your (Safelinku)\n{hijau}example :https://semawur.com/xxxxxx : ")
time.sleep(1)
os.system('cls')

time.sleep(3)
print ("Your Link Has been input....",)  
ua = open('ua.txt', 'r')

data=ua.read()

pl = []
prolist = requests.get("https://sunny9577.github.io/proxy-scraper/proxies.txt").text
prolist1 = requests.get("https://sunny9577.github.io/proxy-scraper/proxies.csv").text
prolist2 = requests.get("https://sunny9577.github.io/proxy-scraper/proxies.json").text
dl = []
for i in prolist.splitlines():
    pl.append(i)

for i in prolist1.splitlines():
    pl.append(i)

for i in prolist2.splitlines():
    pl.append(i)
my_url = "kw"

def tri(i):
   try:
    if requests.get(my_url,proxies={"https":"https://"+i},timeout=0.4).status_code == 200:
       print (i)
       tro(i)
   except:
    pass



def fres(i):
    i.refresh()
    i.minimize_window()


def tro(i):
            chrome_options = Options()
            chrome_options.add_argument("--proxy-server="+i)    
            driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_options)
            driver.get("https://github.com/Monnalisa-ID")
            driver.get(my_url)
            dl.append(driver)

def ua(i):
    user_agent = 'data'

driver = webdriver.Chrome()
opts = Options()
opts.add_argument("user-agent=" + user_agent)
driver = webdriver.Chrome(chrome_options=opts)
driver.get(my_url)

tp = ThreadPool(5000)
tp.map(tri,pl)

tp = ThreadPool(300)
tp.map(fres,dl,ua)


print ("Job Done")


