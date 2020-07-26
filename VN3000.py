import can
import json
import sys 

filename = 'vn3000.json'

class VN3000:
    """Class for installation"""

    def __init__(self):

        """
        id - the frame identifier used for arbitration on the bus.
        """
        self.id_pumps = 0x101E0070
        self.id_valve = 0x181E0E50
        self.id_to_pc = 0x101E0065
        self.id_to_pc_pressure = 0x181E0E60

        """
        The data parameter of a CAN message is exposed as a bytearray with length between 0 and 8.
        """
        self.data_vacuum_pump_on = [0x11, 0x00, 0x01, 0x00, 0xDC, 0xF6, 0x12, 0x00]
        self.data_vacuum_pump_off = [0x11, 0x00, 0x02, 0x00, 0xDC, 0xF6, 0x12, 0x00]
        self.data_vacuum_turbine_on = [0x11, 0x00, 0x03, 0x00, 0xDC, 0xF6, 0x12, 0x00]
        self.data_vacuum_turbine_off = [0x11, 0x00, 0x04, 0x00, 0xDC, 0xF6, 0x12, 0x00]
        self.data_valve_1_open = [0x01, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.data_valve_1_close = [0x01, 0x00, 0x1F, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.data_valve_2_open = [0x01, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.data_valve_2_close = [0x01, 0x00, 0x2F, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.data_valve_3_open = [0x01, 0x00, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.data_valve_3_close = [0x01, 0x00, 0x3F, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.state_pumps = [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.state_valve = [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00] 
        
        """
        Load settings for VN3000
        """
        with open (filename) as f:
            templates = json.load(f)

        self.dcBlock = templates['presetting'].get('dcBlock')
        self.rfBlock = templates['presetting'].get('rfBlock')
        self.highVoltageBlock = templates['presetting'].get('highVoltageBlock')

        """
        Try to open CAN BUS systec
        """
        try:
            bus = can.interface.Bus(bustype='systec', channel='0', bitrate=1000000)
        except can.CanError:
            print("Hardware or CAN interface initialization failed.")
            input()
            sys.exit()

    def star_work(self):
        """Getting started, the foundation of the program"""
        print("ВН-3000")


        if input():
            pass

        if command == 'vacuum pump on':
            msg = can.Message(is_extended_id=True, arbitration_id=self.id_pumps, data=self.data_vacuum_pump_on)
            bus.send(msg)
            self.state_pumps[2] = self.data_vacuum_pump_on[2]
