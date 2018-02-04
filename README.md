This script can be used as a base to similar bruteforce HTTP applications. It's necessary to have 'tac' and 'crunch' installed: "sudo apt-get install tac crunch", on Linux, or "brew install tac crunch", for MacOS.

Usage from terminal: python bruteforcepin.py

Once executed, crunch will create a text file with 10^(number of digits of the PIN you want to break) and tac will create another file with the inverse data. The script will, then, start the brute force attack based on the two lists created by tac and crunch: the first starts from top (usually 0000, if it's a 4 digits PIN, for example) and the other, from bottom to top (9999). Despite consuming more of the processor's capacity, it's still not expressive. I was able to break PIN 7914 in 21 minutes and 21 seconds, as an example. Since you don't know if the PIN is above or below 5000, the script will take, at least, half of time it would normally need to break.

The website must also accept GET requests to input the PIN. You need to modify the variable "url" on the script with the correct address.

This is for educational purposes only. I wrote this code due to a Capture the Flag (CtF) challenge. Use it only in accordance with the law; I'm not responsible for its use. In any case, most websites have protections against too many failed attempts, so be advised.
