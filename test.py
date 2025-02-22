import pyshark

capture = pyshark.FileCapture("captures\\s7comm_plus.pcap")

for packet in capture:
    if(packet.highest_layer == "S7COMM-PLUS"):
        print(packet)
        break