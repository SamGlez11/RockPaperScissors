# Rock Paper Scissors - Network Play Setup

## Playing with Friends on Different Computers

### For the Host Player (Person hosting the game):

1. **Start the Server:**
   ```bash
   python Server.py
   ```

2. **Find your IP address:**
   ```bash
   python get_ip.py
   ```
   Your IP will be shown (e.g., 172.25.27.124)

3. **Share your IP** with the other player

4. **Start your client:**
   ```bash
   python ClientHost.py
   ```

### For the Remote Player (Person joining the game):

1. **Get the host's IP address** from the host player

2. **Start your client with the host's IP:**
   ```bash
   python ClientRemote.py <HOST_IP>
   ```
   
   Example:
   ```bash
   python ClientRemote.py 172.25.27.124
   ```

## Important Notes:

- **Firewall**: Make sure port 5555 is open on the host's firewall
- **Network**: Both players must be on the same network (WiFi/LAN) or have port forwarding set up
- **IP Address**: The host's IP address might change if they restart their router

## Troubleshooting:

1. **Connection refused**: Check if the server is running and firewall allows port 5555
2. **Wrong IP**: Make sure you're using the correct IP address from get_ip.py
3. **Network issues**: Ensure both computers are on the same network

## Files:
- `Server.py` - The game server (run this first)
- `ClientHost.py` - Client for the host player
- `ClientRemote.py` - Client for remote players
- `get_ip.py` - Gets your IP address to share
- `Network.py` - Original local network config (for localhost play)
- `NetworkConfig.py` - Network configurations for host/remote play
