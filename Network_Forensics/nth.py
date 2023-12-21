from scapy.all import sniff

# Define a packet callback function to process captured packets
def packet_callback(packet):
    if packet.haslayer('IP'):  # Filter only IP packets
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        proto = packet['IP'].proto
        print(f"Source IP: {src_ip} -> Destination IP: {dst_ip}, Protocol: {proto}")

# Start sniffing packets on the network interface (replace 'eth0' with your interface)
# You might need root/admin privileges to run this
sniff(iface='eth0', prn=packet_callback, count=10)  # Sniff 10 packets
