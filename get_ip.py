import socket

def get_local_ip():
    """Get the local IP address of this machine"""
    try:
        # Connect to a remote address (doesn't actually send data)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

if __name__ == "__main__":
    ip = get_local_ip()
    print(f"Your local IP address is: {ip}")
    print(f"Share this IP with other players so they can connect to your game!")
    print(f"Other players should use this IP in their Network.py file")
