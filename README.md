# Blindhit
A Simple Time based(GET only) SQLI detector using a python script.
This script checks the parameters one by one whether vuln or not. It uses a urls file with valid params and a time based sqli payload file.
It checks for each parameter with each payload from the file and gives the vulnerable result. Donot use same parameter values while running the tool. Change the parameter value if same

# Clonning and Usage:
~ git clone https://github.com/dotslashed/blindhit.git \
~ cd blindhit \
~ python3 bsqlin.py [urls file] [payloads file] \
\
\
![alt text](https://github.com/dotslashed/blindhit/raw/main/Captureg.PNG)
