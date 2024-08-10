import socket
import threading

def scan_port(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        s.settimeout(1)
        
        # Try to connect to the host and port
        result = s.connect_ex((host, port))
        
        # Check if the connection was successful
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        # Close the socket
        s.close()
    except socket.error:
        print("Socket error occurred")

def port_scan(host, ports):
    # Loop through the ports and create threads to scan them
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(host, port))
        thread.start()

def main():
    # Host to scan
    host = input("Enter the target host IP address or hostname: ")
    
    # Range of ports to scan
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    # Generate a list of ports to scan
    ports = range(start_port, end_port + 1)
    
    # Perform the port scan
    port_scan(host, ports)

if __name__ == "__main__":
    main()
