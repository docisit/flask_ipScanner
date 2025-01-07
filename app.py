from flask import Flask, render_template, request, jsonify
import platform
import subprocess
import re
import ipaddress
import socket

app = Flask(__name__)

@app.route('/')
def index():
    # Get the operating system information
    os_info = platform.system() + " " + platform.release()
    
    # Render the index page with OS info
    return render_template('index.html', os_info=os_info)

@app.route('/scan', methods=['POST'])
def scan():
    # Get the IP range input from the user
    ip_input = request.form['ip_range']
    ports = request.form['ports'].split(',')

    # Validate CIDR format
    try:
        network = ipaddress.ip_network(ip_input, strict=False)
    except ValueError:
        return jsonify({'error': 'Invalid CIDR address format.'}), 400

    # Get connected devices
    devices = get_connected_devices()

    # Scan ports for each device
    scan_results = scan_ports(devices, ports)

    return jsonify({'devices': scan_results})

def get_connected_devices():
    devices = []
    try:
        output = subprocess.check_output(['arp', '-a']).decode()
        pattern = re.compile(r'\((.*?)\)\s+([0-9a-fA-F:]+)')
        for line in output.splitlines():
            match = pattern.search(line)
            if match:
                ip = match.group(1)
                mac = match.group(2)
                devices.append({'ip': ip, 'mac': mac})
    except Exception as e:
        print(f"Error retrieving devices: {e}")

    return devices

def scan_ports(devices, ports):
    results = []
    for device in devices:
        ip = device['ip']
        device_ports = {}
        for port in ports:
            port = port.strip()  # Remove any extra whitespace
            if port.isdigit():  # Check if the port is a number
                port = int(port)
                device_ports[port] = is_port_open(ip, port)
        results.append({'ip': ip, 'mac': device['mac'], 'ports': device_ports})
    return results

def is_port_open(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0  # Return True if port is open

if __name__ == '__main__':
    app.run(debug=True)