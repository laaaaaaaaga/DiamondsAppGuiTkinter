---
author:		Marcin Grelak
title:		Diamonds pricing app readme
date:		21.01.2024
lang:		en
---
## Diamonds pricing app
This app is a part of a bigger project. To use it simply download the 'DiamondsApp.exe' file from 'dist' folder and enjoy your pricing app.

## How to use it?
All data entries must be filled with floating-point numbers, and all categories of radio button must have  an option choosen.
There are some default options, but you can change them according to your diamond values.
After providing all necessary data press 'Price' button and wait for the result to poup. Application requires internet connection.

## How to deploy my own executable file?
Clone the repository to your desired directory on any machine that has git installed by opening terminal in this location and typing
```shell
git clone https://github.com/laaaaaaaaga/DiamondsAppGuiTkinter.git
```
<br>

Install pyinstaller by typing into terminal.
```shell
pip install pyinstaller
``` 
<br>
In terminal run command

```shell
pyinstaller main.py --onefile --name DesiredAppName
```
<br>
After a short while your executable file called "DesiredAppName.exe" should be created in folder "dist". This exectuable file will be created for system that you are currently using. For example if you follow this tutorial on windows the created file extension will be ".exe". To create ".dmg" or other executable files you will need to repeat the proccess on the machine with the desired system.