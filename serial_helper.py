import meshtastic
import meshtastic.serial_interface


class SerialHelper:
    def __init__(self):
        self.interface = meshtastic.serial_interface.SerialInterface()
        self.node_list = []

    def retrieve_node_info_from_serial(self):
        # interface = meshtastic.serial_interface.SerialInterface()
        for node in self.interface.nodes.values():
            new_tuple = (node['user']['longName'], node['user']['macaddr'], node['num'])
            self.node_list.append(new_tuple)
        return self.node_list

    def retrieve_number_of_device_connected(self):
        count = 0
        for node in self.interface.node.values():
            count += 1
        return count

    def send_string(self, s):
        returned_packet = self.interface.sendText(s)
        print("Here is the packet returned")
        print(returned_packet)

    def close_connection(self):
        self.interface.close()
