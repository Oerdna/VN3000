import can


class BlockDC:
    """this class implements interaction with the control unit.
    """

    """id - the frame identifier used for arbitration on the bus.
    """
    id_blockDC_command = 0x101E0010

    def __init__(self, bus: object):
        """Variables are responsible for storing the pressure value, I and U.

        Args:
            bus (object): [USB-CAN object]
        
        :range_current:
            current seted for Dc magnetron sputtering
            
        :block_dc_state:
            state of block DC
        
        :block_enable:
            enable/disable block

        :current_state:
            state process of sputtering material

        :mes_current:
            effective current flow throught magnetron
        
        :mes_voltage:
            effective voltage applayed to magnetron
        """

        self.range_current: int = 0

        self.block_dc_state: bool = False
        self.block_dc_enable: bool = False
        self.current_state: bool = False

        self.mes_current_dc: int = 0
        self.mes_voltage_dc: int = 0
        self.mes_seted_cur_dc: int = 0

        self.bus = bus
        self.msg_send_upr = can.Message(
            arbitration_id=self.id_blockDC_command,
            is_extended_id=True,
            dlc=4,
            data=bytearray(4),
        )

    def get_states(self):
        """call to get the actual states of the units.
        """
        self.msg_send_upr.data[0] = b"\x0f"[0]
        self.send_and_flush(self.msg_send_upr)

    def get_measurements(self):
        """called to get values from sensors.
        """
        self.msg_send_upr.data[0] = b"\xff"[0]
        self.send_and_flush(self.msg_send_upr)

    def state_block_dc(self, state: bool):
        """Enable/disable DC block
        """
        if state:
            self.msg_send_upr.data[0] = b"\x32"[0]
        else:
            self.msg_send_upr.data[0] = b"\x30"[0]
        self.send_and_flush(self.msg_send_upr)

    def current_dc(self, state: bool, value: int = 0):
        """Enable/disable sputtering
        """
        if state:
            self.msg_send_upr.data[0] = b"\x48"[0]
            self.msg_send_upr.data[2] = value
        else:
            self.msg_send_upr.data[0] = b"\x50"[0]
        self.send_and_flush(self.msg_send_upr)

    def send_and_flush(self, msg):
        """Send fun with callbcak Eror
        """
        try:
            self.bus.send(msg)
            msg.data[:4] = bytearray(4)
            # print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")

    def return_states_mes(self):
        return {
            "range_current": self.range_current,
            "block_dc_state": self.block_dc_state,
            "block_dc_enable": self.block_dc_enable,
            "current_state": self.current_state,
            "mes_current_dc": self.mes_current_dc,
            "mes_voltage_dc": self.mes_voltage_dc,
        }

    def return_mes(self):
        return {
            "block_dc_state": self.block_dc_state,
            "block_dc_enable": self.block_dc_enable,
            "current_state": self.current_state,
            "mes_current_dc": self.mes_current_dc,
            "mes_voltage_dc": self.mes_voltage_dc,
        }

    def return_states(self):
        return {
            "range_current": self.range_current,
            "block_dc_enable": self.block_dc_enable,
            "current_state": self.current_state,
        }
