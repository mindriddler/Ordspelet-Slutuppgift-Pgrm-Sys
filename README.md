# Ordspelet
## Author: Fredrik Magnusson [fredrik.magnusson2@yh.nackademin.se] ##

This is my version of the final assignment for the course "Programmering & Systemering" in the DevOps22 class at Nackademin.

I've created two versions of this game, one swedish and one english

To use the english version you will need to switch the branch from master to english


# **Setup** 
To use the game you will need python 3.10 installed on your computer

For how to install python 3.10, see instructions at the bottom


## **Game rules** ##
- The word must be 5 characters 
- Must be a swedish word
- Can not contain repeted characters, such as "tunna"
- Can not be a name, such as "Johan"
- Can not be in tempus or plural form

## **How to play the game:** ##
- Start the game by accepting the rules
- Choose 1 or 2 depending on if you want to be the guesser or the thinker
- Follow the instructions shown on the screen
- You can always quit the game at any time by writing "quit" when asked for a input
- Password to reset highscore is "qwerty123"

## **How to run** ##
- Navigate to the folder where you cloned the repository to in the terminal
- Start the game
```
python main.py 
```
-----



## **Windows** ##
You can either download python by clicking **_[here](https://www.python.org/downloads/)_**

you can use also use winget by typing the line below into powershell
```powershell
winget install python --accept-package-agreements
```
<sup>read more about winget [here](https://learn.microsoft.com/en-us/windows/package-manager/winget/)</sup>

## **Linux** ##
First check if python3.10 is already installed
```
python3 -v
```
if you get no return from that input, follow below
```
sudo apt update
sudo apt-get install python3
```
