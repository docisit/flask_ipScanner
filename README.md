# IP Scanner

A simple IP scanner built with Flask that detects connected devices on a network and checks specified ports to see if they are open. The application also displays the operating system of the client.

## Features

- Detects the operating system of the client.
- Lists connected devices with their IP and MAC addresses.
- Scans specified ports on each device to check if they are open.
- Validates CIDR input format.

## Requirements

- Python 3.x
- Flask
- flask-cors (if needed)

## Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ip-scanner.git
   cd ip-scanner

   ##Highly recomend you run this app in a Virtual Enviroment (venv)

   Linux
   python -m venv venv

   Activate venv Windows
   venv\Scripts\activate

   Activate venv Linus
   venv/bin/activate

   once you activate, then
pip install -r requirements.txt

make sure flask and scapy are installed in your venv, as well.

Once you have your enviorment running, create a templates directory, and place the index.html into the templates directory.
then to run the app
python app.py

you can then use it at 
http://127.0.0.1:5000

My first Flask App, and I am still working on it.  
   

   
