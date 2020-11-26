import can


class BlockRF:
    """this class implements interaction with the control unit.
    """

    """id - the frame identifier used for arbitration on the bus.
    """
    id_blockRF_command = 0x101E0030

    def __init__(self, bus: object):
        """Variables are responsible for storing the pressure value, I and U.

        Args:
            bus (object): [USB-CAN object]
        
        :range_power:
            power seted for Rf magnetron sputtering
            
        :block_rf_state:
            state of block Rf
        
        :block_rf_enable:
            enable/disable block

        :block_rf_sputtering:
            enable/disable pre -sputtering
        
        :block_rf_set_power:
            enable/disable sputtering 

        :mes_rf_KBV:
            Measurement of KBV

        :mes_rf_Imagn:
            Measurement of current's magnetron

        :mes_rf_Umagn:
            Measurement of voltage's magnetron

        :mes_rf_Power:
            Measurement of power

        :mes_rf_Idriver:
            Measurement of current's driver

        :mes_rf_Ianod:
            Measurement of currnet's anod

        """

        self.range_power: int = 0

        self.block_rf_state: bool = False
        self.block_rf_enable: bool = False
        self.block_rf_ready: bool = False
        self.block_rf_sputtering: bool = False
        self.block_rf_set_power: bool = False
        self.rf_active_C1up: bool = False
        self.rf_active_C2up: bool = False
        self.rf_active_C1down: bool = False
        self.rf_active_C2down: bool = False
        self.error: bool = False

        self.mes_rf_KBV: int = 0
        self.mes_rf_Imagn: int = 0
        self.mes_rf_Umagn: int = 0
        self.mes_rf_Power: int = 0
        self.mes_rf_Idriver: int = 0
        self.mes_rf_Ianod: int = 0

        self.bus = bus
        self.msg_send_upr = can.Message(
            arbitration_id=self.id_blockRF_command,
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

    def state_block_rf(self, state: bool):
        """Enable/disable RF block
        """
        if state:
            self.msg_send_upr.data[0] = b"\x45"[0]
        else:
            self.msg_send_upr.data[0] = b"\x44"[0]
        self.send_and_flush(self.msg_send_upr)

    def check_rf(self, state):
        """Enable/disable cheking of RF sputtering
        """
        if state:
            self.msg_send_upr.data[0] = b"\x45"[0]
        else:
            self.msg_send_upr.data[0] = b"\x44"[0]
        self.send_and_flush(self.msg_send_upr)

    def power_rf(self, state: bool, value: int = 0):
        """Enable/disable sputtering
        """
        if state:
            self.msg_send_upr.data[0] = b"\x66"[0]
            self.msg_send_upr.data[2:4] = value.to_bytes(2, "little")
        else:
            self.msg_send_upr.data[0] = b"\x67"[0]
        self.send_and_flush(self.msg_send_upr)

    def cap_state(self, name: str, direct: str, state: bool):
        """
        Enable/disable capacity С1/2 increase/reduction
        """
        if name == "C1":
            if direct == "up":
                if state:
                    self.msg_send_upr.data[0] = b"\x50"[0]
                else:
                    self.msg_send_upr.data[0] = b"\x51"[0]
            elif direct == "down":
                if state:
                    self.msg_send_upr.data[0] = b"\x52"[0]
                else:
                    self.msg_send_upr.data[0] = b"\x53"[0]
        elif name == "C2":
            if direct == "up":
                if state:
                    self.msg_send_upr.data[0] = b"\x54"[0]
                else:
                    self.msg_send_upr.data[0] = b"\x55"[0]
            elif direct == "down":
                if state:
                    self.msg_send_upr.data[0] = b"\x56"[0]
                else:
                    self.msg_send_upr.data[0] = b"\x57"[0]
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
            "range_power": self.range_power,
            "error": self.error,
            "block_rf_ready": self.block_rf_ready,
            "block_rf_state": self.block_rf_state,
            "block_rf_enable": self.block_rf_enable,
            "block_rf_sputtering": self.block_rf_sputtering,
            "block_rf_set_power": self.block_rf_set_power,
            "mes_rf_KBV": self.mes_rf_KBV,
            "mes_rf_Imagn": self.mes_rf_Imagn,
            "mes_rf_Umagn": self.mes_rf_Umagn,
            "mes_rf_Power": self.mes_rf_Power,
            "mes_rf_Idriver": self.mes_rf_Idriver,
            "mes_rf_Ianod": self.mes_rf_Ianod,
        }

    def return_mes(self):
        return {
            "mes_rf_KBV": self.mes_rf_KBV,
            "mes_rf_Imagn": self.mes_rf_Imagn,
            "mes_rf_Umagn": self.mes_rf_Umagn,
            "mes_rf_Power": self.mes_rf_Power,
            "mes_rf_Idriver": self.mes_rf_Idriver,
            "mes_rf_Ianod": self.mes_rf_Ianod,
            "block_rf_state": self.block_rf_state,
            "block_rf_enable": self.block_rf_enable,
            "block_rf_sputtering": self.block_rf_sputtering,
            "block_rf_set_power": self.block_rf_set_power,
            "error": self.error,
            "block_rf_ready": self.block_rf_ready,
        }

    def return_states(self):
        return {
            "range_power": self.range_power,
            "block_rf_enable": self.block_rf_enable,
            "block_rf_sputtering": self.block_rf_sputtering,
            "block_rf_set_power": self.block_rf_set_power,
        }
