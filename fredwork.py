#!/usr/bin/env python3

import os
import requests
import random
import string


DARK_RED = "\033[31;2m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Function to clear the terminal screen
def clear_screen():
    os.system('clear')

# Function to display ASCII text
def display_ascii_text():
    print(f"""{DARK_RED}
 ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄     ▄▀▀█▄▄▄▄  ▄▀▀▀█▀▀▄ 
█ █   ▐ █ █    ▌ ▐ ▄▀ ▀▄ █   █   █ █    █     ▐  ▄▀   ▐ █    █  ▐ 
   ▀▄   ▐ █        █▄▄▄█ ▐  █▀▀█▀  ▐    █       █▄▄▄▄▄  ▐   █     
▀▄   █    █       ▄▀   █  ▄▀    █      █        █    ▌     █      
 █▀▀▀    ▄▀▄▄▄▄▀ █   ▄▀  █     █     ▄▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄    ▄▀       
 ▐      █     ▐  ▐   ▐   ▐     ▐     █         █    ▐   █         
        ▐                            ▐         ▐        ▐   
{RESET}""")


def ask():
    print(f"""{DARK_RED}
[1] links         [12] comming soon [23] comming soon [34] comming soon
[2] sm maker      [13] comming soon [24] comming soon [35] comming soon
[3] sm transelator[14] comming soon [25] comming soon [36] comming soon
[4] advanced links[15] comming soon [26] comming soon [37] comming soon
[5] comming soon  [16] comming soon [27] comming soon [38] comming soon
[6] comming soon  [17] comming soon [28] comming soon [39] comming soon
[7] comming soon  [18] comming soon [29] comming soon [40] comming soon
[8] comming soon  [19] comming soon [30] comming soon [41] comming soon
[9] comming soon  [20] comming soon [31] comming soon [42] comming soon
[10] comming soon [21] comming soon [32] comming soon [43] comming soon
[11] comming soon [22] comming soon [33] comming soon [h]  help
{RESET}""")
    answer = input("select:")
    if (answer == "1"):
        links()
    if (answer == "2"):
        encrypt_message()
    if (answer == "3"):
        decrypt_message()
    if (answer == "4"):
        advanced_links()



def check_username(username):
    # Define the social media platforms and their URLs
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "YouTube": f"https://www.youtube.com/user/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "GitHub": f"https://github.com/{username}",
    }

    results = {}
    
    for platform, url in platforms.items():
        response = requests.head(url)
        exists = response.status_code == 200
        results[platform] = exists

    return results

# Function to display advanced links
def advanced_links():
    username = input("Enter username: ")
    print(f"{GREEN}CHECKING USERNAMES...{RESET}")
    results = check_username(username)

    for platform, exists in results.items():
        color = GREEN if exists else RED
        status = "Exists" if exists else "Does not exist"
        print(f"{color}{platform}: {status}{RESET}")
    input("click enter to continue...")
    main()



# Function to encrypt a message
def encrypt_message():
    custom_message = input("Enter a custom message: ")
    key = input("Enter a key to translate the text: ")

    encrypted_message = ""
    for char in custom_message:
        if char in key_dict:
            encrypted_message += key_dict[char]
        else:
            encrypted_message += char

    print("Encrypted Message:")
    print(encrypted_message)

# Function to decrypt a message
def decrypt_message():
    custom_message = input("Enter an encrypted message: ")
    key = input("Enter the key to decrypt the text: ")

    # Validate the key
    if key != original_key:
        print("Invalid key. Decryption failed.")
        return

    decrypted_message = ""
    for char in custom_message:
        for k, v in key_dict.items():
            if v == char:
                decrypted_message += k
                break
        else:
            decrypted_message += char

    print("Decrypted Message:")
    print(decrypted_message)

# Original key used for encryption
original_key = "scarlet"



# Dictionary for encryption and decryption key
key_dict = {
    'a': 'Jfo3',
    'b': 'O0:3s',
    'c': 'poQ2;s',
    'd': '@ssddw',
    'e': 'per0S',
    'f': 'KJdf',
    'g': '=889t',
    'h': 'Lpsd',
    'i': '=hfsd:;',
    'j': 'dfg=wd22',
    'k': 'PP',
    'l': 'K',
    'm': ':::',
    'n': '90d8',
    'o': 'poifFF@',
    'p': '1@€6',
    'q': '1asd7',
    'r': '1asdwd8',
    's': '145t9',
    't': '2h60',
    'u': '2hr1',
    'v': '2hfgh2',
    'w': '2sdf3',
    'x': '223f4',
    'y': '2ljkl5',
    'z': '2uilk6',
    'A': 'hj1',
    'B': '2dbr',
    'C': '3dfbr',
    'D': '4dfb',
    'E': '5rb',
    'F': '6ad222',
    'G': '7234',
    'H': '8f3f',
    'I': '9',
    'J': '123f0',
    'K': '1sdf1',
    'L': '1dfg2',
    'M': '1efsdf3',
    'N': '1grg4',
    'O': '1asdaf5',
    'P': '165t5y',
    'Q': '172y99',
    'R': '1qd8',
    'S': '13fh5hfghs9',
    'T': '23f2f0',
    'U': '223ff21',
    'V': '2qf3qwf2',
    'W': '2qf3q23',
    'X': '2lkjhgf4',
    'Y': '2asdwdas5',
    'Z': '2340f98g6',
    '1': '123r23ruhi7',
    '2': '132rwg8',
    '3': '1rht9',
    '4': '2aqwds0',
    '5': '2ad441',
    '6': '21342',
    '7': '2rthfghWW3',
    '8': '2WFFR4',
    '9': '25SDW',
    '0': '26CFWDWFff',
    ' ': '2FWfsdf6',
}
def links():
    clear_screen()
    username = input("username: ")


    # Twitter link
    twitter_link = f"https://twitter.com/{username}"
    print(f"Twitter: {twitter_link}")

    # TikTok link
    tiktok_link = f"https://www.tiktok.com/@{username}"
    print(f"Tiktok: {tiktok_link}")

    # Instagram link
    instagram_link = f"https://www.instagram.com/{username}"
    print(f"Instagram: {instagram_link}")

    # Facebook link
    facebook_link = f"https://www.facebook.com/{username}"
    print(f"Facebook: {facebook_link}")

    # LinkedIn link
    linkedin_link = f"https://www.linkedin.com/in/{username}"
    print(f"LinkedIn: {linkedin_link}")

    # Pinterest link
    pinterest_link = f"https://www.pinterest.com/{username}"
    print(f"Pinterest: {pinterest_link}")

    # Snapchat link
    snapchat_link = f"https://www.snapchat.com/add/{username}"
    print(f"Snapchat: {snapchat_link}")

    # YouTube link
    youtube_link = f"https://www.youtube.com/user/{username}"
    print(f"YouTube: {youtube_link}")

    # Reddit link
    reddit_link = f"https://www.reddit.com/user/{username}"
    print(f"Reddit: {reddit_link}")

    # GitHub link
    github_link = f"https://github.com/{username}"
    print(f"GitHub: {github_link}")



# Main function
def main():
    clear_screen()
    display_ascii_text()
    ask()

    

if __name__ == "__main__":
    main()
