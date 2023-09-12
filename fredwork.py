#!/usr/bin/env python3

import os

# Function to clear the terminal screen
def clear_screen():
    os.system('clear')

# Function to display ASCII text
def display_ascii_text():
    print("""
 ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄     ▄▀▀█▄▄▄▄  ▄▀▀▀█▀▀▄ 
█ █   ▐ █ █    ▌ ▐ ▄▀ ▀▄ █   █   █ █    █     ▐  ▄▀   ▐ █    █  ▐ 
   ▀▄   ▐ █        █▄▄▄█ ▐  █▀▀█▀  ▐    █       █▄▄▄▄▄  ▐   █     
▀▄   █    █       ▄▀   █  ▄▀    █      █        █    ▌     █      
 █▀▀▀    ▄▀▄▄▄▄▀ █   ▄▀  █     █     ▄▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄    ▄▀       
 ▐      █     ▐  ▐   ▐   ▐     ▐     █         █    ▐   █         
        ▐                            ▐         ▐        ▐         
""")


def ask():
    print("""
[1] links        [12] comming soon [23] comming soon [34] comming soon
[2] comming soon [13] comming soon [24] comming soon [35] comming soon
[3] comming soon [14] comming soon [25] comming soon [36] comming soon
[4] comming soon [15] comming soon [26] comming soon [37] comming soon
[5] comming soon [16] comming soon [27] comming soon [38] comming soon
[6] comming soon [17] comming soon [28] comming soon [39] comming soon
[7] comming soon [18] comming soon [29] comming soon [40] comming soon
[8] comming soon [19] comming soon [30] comming soon [41] comming soon
[9] comming soon [20] comming soon [31] comming soon [42] comming soon
[10] comming soon [21] comming soon [32] comming soon [43] comming soon
[11] comming soon [22] comming soon [33] comming soon [h]  help
""")
    answer = input("select:")


# Main function
def main():
    clear_screen()
    display_ascii_text()
    ask()

    

if __name__ == "__main__":
    main()
