import pyshark

# Create an empty packet
packet = pyshark.packet.packet.Packet()

# Ethernet Layer - you would need actual MAC addresses here
packet.eth = pyshark.packet.layer.Layer("eth", src="00:11:22:33:44:55", dst="66:77:88:99:aa:bb")

# IP Layer - change these to your desired IPs
packet.ip = pyshark.packet.layer.Layer("ip", src="192.168.1.1", dst="192.168.1.2")

# TCP Layer - here you're setting basic parameters, but you'd need to adjust based on your original packet
packet.tcp = pyshark.packet.layer.Layer("tcp", srcport=102, dstport=49154, ack=1, seq=1, flags="AP")

# Here, you'd need to manually construct or use a library for S7COMM-PLUS data
# This is a simplification; actual implementation would require more detail:
packet.s7comm_plus = pyshark.packet.layer.Layer("s7comm_plus", 
    protocol_id=0x72, protocol_version=3, data_length=98, 
    # etc... you would need to add all the fields here or use a more specialized library
)

# This part is hypothetical because S7COMM-PLUS isn't natively supported by pyshark:
# You might need to pack your custom payload into the packet:
custom_payload = b'\x72\x03...'  # Your S7COMM-PLUS data here
packet.set_payload(custom_payload)

# Send the packet - you'd need an interface to send from:
# This would typically be done using raw sockets, which are not directly supported by pyshark.
# You might need to switch to scapy or another library for actual sending:

# print(packet)  # To see what the packet looks like

# Note: Sending packets requires admin privileges and can be dangerous if misused.