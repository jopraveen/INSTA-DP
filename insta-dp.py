# importing modules
from os import system
from termcolor import colored
import instaloader

# colors
cn = 'cyan'

# banner
system('clear')
system('figlet -f ./Arrows "INSTA" | lolcat -a -d 2')
system('echo "    >==> Profile Downloader By Jopraveen" | lolcat -a -d 15')

# Main code
ig = instaloader.Instaloader()
username = input(colored("\nEnter the username: ",cn))
print("\n",ig.download_profile(username,profile_pic_only = True))
system('echo "Saved in current working Directory" | lolcat -a -d 40')
print()
system('echo "I hope you liked it Follow  [ J O P R A V E E N ] in GITHUB For More COOL stuffs :D " | lolcat -a -d 120 ')
