import pyfiglet
import string
import secrets 
import webbrowser
import feedparser
import requests
import json
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes


def password_generator(size):
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for i in range(size))
    return password

def cybernews():
    print("Cybersecurity News and Blogs")
    print("0. NIST")
    print("1. The Hacker News")
    print("2. ThreatPost")
    print("3. NakedSecurity")
    print("4. SecurityWeek")
    print("5. Google Security Blogs")

    websites = ("https://www.nist.gov/blogs/cybersecurity-insights/rss.xml", "https://feeds.feedburner.com/TheHackersNews", "https://threatpost.com/feed", "https://nakedsecurity.sophos.com/feed", "https://feeds.feedburner.com/Securityweek", "https://feeds.feedburner.com/GoogleOnlineSecurityBlog")

    website = int(input("Enter website number[0-5]:"))
    News = feedparser.parse(websites[website])
    articlelist = []
    articlelink = []
    for i in range(5):
        article = News.entries[i]
        title = article.title
        link = article.link
        articlelist.append(title)
        articlelink.append(link)

    article_num = 1
    for article in articlelist:
        print('{}. {}'.format(str(article_num), article))
        article_num = article_num + 1

    article_link_click = False
    while not article_link_click:
        click = int(input("Choose the link to the article you want to read: "))
        webbrowser.open(articlelink[click - 1])
        article_link_click = True

def cvesearch():
    id = input("Enter CVE ID(along with -): ")
    url = "https://cve.circl.lu/api/cve/{}".format(id)
    content = requests.get(url)
    fcontent = content.text
    json_format = json.loads(fcontent)
    print("{} {}".format("CVE ID: ", json_format["id"]))
    print("{} {}\n".format("Description: ", json_format["summary"]))

def cryptobot():
    def no_such_action():
        print("No such option available. Please select an option from 1-6")
        print(" ")
        pass

    def cryptobot_menu():
        print(" ")
        print("1. ECB mode")
        print("2. CBC mode")
        print("3. CTR mode")
        print("4. CFB mode")
        print("5. OFB mode")
        print("6. Exit")
        print(" ")
    
    def aes_cbc():
        key = get_random_bytes(24) # 192 Bit Key
        iniv = get_random_bytes(16) # 128 bit Initialization Vector
        print ("key: ",key)

        pt = input("Enter the plaintext: ")
        pt = bytes(pt,"UTF-8") #Encodes the plain text to a UTF-8 string

        encrypt_obj = AES.new(key,AES.MODE_CBC,iv=iniv)

        ct = encrypt_obj.encrypt(pad(pt,AES.block_size))

        print ("Cipher Text:",ct)

    def aes_cfb():
        key = get_random_bytes(24)  
        iniv = get_random_bytes(16)

        print ("key:",key)

        pt =input("Enter the plaintext: ")
        pt =bytes(pt,"UTF-8")

        encrypt_obj = AES.new(key,AES.MODE_CFB,iv=iniv)

        ct = encrypt_obj.encrypt(pad(pt,AES.block_size))

        print ("Cipher Text:",ct)

    def aes_ctr():
        key = get_random_bytes(24)
        
        iniv = get_random_bytes(8)
        nc = get_random_bytes(8)  #64 bit nonce 

        print ("key:",key)

        pt =input("Enter the plaintext: ")
        pt =bytes(pt,"UTF-8")

        encrypt_obj = AES.new(key,AES.MODE_CTR,nonce=nc,initial_value=iniv)

        ct = encrypt_obj.encrypt(pad(pt,AES.block_size))

        print ("Cipher Text:",ct)

    def aes_ofb():
        key = get_random_bytes(24)
        iniv = get_random_bytes(16)

        print ("key:",key)

        pt =input("Enter the plaintext: ")
        pt =bytes(pt,"UTF-8")

        encrypt_obj = AES.new(key,AES.MODE_OFB,iv=iniv)

        ct = encrypt_obj.encrypt(pad(pt,AES.block_size))

        print ("Cipher Text:",ct)

    def aes_ecb():
        key = get_random_bytes(16)
        print ("key:",key)

        pt = input("Enter the plaintext: ")
        pt = bytes(pt,"UTF-8")

        encrypt_obj = AES.new(key,AES.MODE_ECB)

        ct = encrypt_obj.encrypt(pad(pt,AES.block_size))

        print ("Cipher Text:",ct)

    actions = {"1": aes_ecb, "2": aes_cbc, "3": aes_ctr, "4": aes_cfb, "5": aes_ofb}
    while True:
        print(" ")
        print("Hi! I am CryptoBot")
        print("Following are the modes of AES encryption I can encrypt your message in")
        cryptobot_menu()
        selection = input("Your selection: ")
        if "6" == selection:
            return
        toDo = actions.get(selection, no_such_action)
        toDo()
        k = input("Do you wish to continue?(y or n) ")
        if k == 'n':
            return

while True:
    art = pyfiglet.figlet_format("CyberUtils", font = "doom")
    print("-------------------------------------------------------")
    print(art)
    print("-------------------------------------------------------")
    print(" ")
    print("[1]Password Generator")
    print("[2]Cybersecurity News")
    print("[3]CVE Search")
    print("[4]CryptoBot")
    print("[5]Exit")
    print(" ")
    choice = int(input("Enter Your Selection[1-5]:"))
    print(" ")

    if choice == 1:
        size = int(input("Enter the size length of the password to be generated:"))
        print("Password:", password_generator(size))
        break

    elif choice == 2:
        cybernews()
        break

    elif choice == 3:
        cvesearch()
        break
        
    elif choice == 4:
        cryptobot()

    elif choice == 5:
        break

    else:
        print("Wrong Input, Please select an option between 1-5")


print("Thank you for using CyberUtils")
