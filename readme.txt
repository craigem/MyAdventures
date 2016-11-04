Raspberry Pi Starter Kit
Martin O'Hanlon

From the book: "Adventures in Minecraft"
 written by David Whale and Martin O'Hanlon, Wiley, 2014
 http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
-------------------------------

Description
------------------------------- 
This starter kit contains a folder called "MyAdventures" which contains all the Python libraries required to complete all the chapters in "Adventure in Minecraft".

It is highly recommended that you use the Starter Kit as is and follow the instructions in Adventure 1 - "Hello Minecraft World" to setup your computer.  

The structure of the StarterKit zip file is as follows:
MyAdventures : folders to save the minecraft programs too
 - mcpi : python api library distributed with Minecraft: Pi Edition
 - anyio : python library which contains the library to control the 7 segment display
-------------------------------

StarterKit Creation Guide
-------------------------------
If required the information below can be used as a guide to create your own StarterKit from scratch.  It is written as guide, not as a precise series of instructions.  There is no guarantee that they are accurate and are provided as is.

Create folder
----------------------
Create a folder "MyAdventures"

Setup MyAdventures folder
----------------------
Download mcpi(*) from github https://github.com/martinohanlon/mcpi
   - git clone https://github.com/martinohanlon/mcpi
   * - the mcpi folder contains the python library supplied by mojang with Minecraft: Pi Edition and the minecraftstuff library (github.com/martinohanlon/minecraft-stuff) by Martin O'Hanlon 

Copy the mcpi folder to MyAdventures

Download anyio from github https://github.com/whaleygeek/anyio
 - git clone https://github.com/whaleygeek/anyio

Create a folder "anyio" in MyAdventures

Copy the anyio/seg7.py file to MyAdventures/anyio
Copy the anyio/__init__.py file to MyAdventures/anyio

