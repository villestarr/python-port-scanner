import socket

# Get target info from user
target = input("Enter IP address to scan: ")
ports = input("Enter comma-separated ports to scan (e.g. 22,80,443): ")

# Split port string into a list of ints
ports = [int(p.strip()) for p in ports.split(",")]

print(f"\nStarting scan on {target}...\n")

# Scan each port
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # wait 1 second max for response
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is closed")
    sock.close()
