# LAMEHUG

Recreation of APT-28 AI empowered malware.

Based on {research done by CATO}[https://www.catonetworks.com/blog/cato-ctrl-threat-research-analyzing-lamehug/]

## Disclaimer

THIS CODE IS FOR RESEARCH AND EDUCATIONAL PURPOSES ONLY AND TO AID THREAT ANALYSIS. Don't do bad things. Also don't use this to do bad things, it's so stupid.

## What it be

APT-28 did a funny where they launched a malware campaign with no malware. Their phishing attack got a user to launch a pyinstaller exe hiding as a PDF or as...an AI prompt to make titties? The python in question made a call out to a quen-coder model on huggingface and asked it some questions - questions like ```“Make a list of commands to create folder C:\Programdata\info and to gather computer information, hardware information, process and services information, networks information, AD domain information, to execute in one line and add each result to text file c:\Programdata\info\info.txt. Return only commands, without markdown.”```, which were then fed to a subprocess spawning a shell for later harvesting and exfil (also done with AI generated commands). Wild times.

## What it do

Right now not a whole lot - currently just a skeleton proof of concept for my own interests.

## Running it

pip install the requirements.txt.

Bundle with pyinstaller. Currently set up uses dotenv files to load in API keys and is pretty tightly coupled to chatGPT. pyinstaller supports loading in external files with your binary but there are better ways to bundle API keys with applications so you should use those.
