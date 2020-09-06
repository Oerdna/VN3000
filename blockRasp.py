import can


class BlockRasp:
    """this class implements interaction with the distribution unit.
    """

    """id - the frame identifier used for arbitration on the bus.
    """
    id_blockRasp_command = 0x101E0070

    def __init__(self, bus: object):
        """States of the working units of the block.

        :state_NL:
            foreline pump.

        :state_ND:
            turbomolecular pump.
        
        :state_VE4_open:
            state of the valve VE4.

        :state_VE4_close:
            state of the valve VE4.

        :state_throttling:
            enable of throttling the shutter.

        :state_heat:
            heating the substrate.

        :state_rotation:
            substrate rotation.

        Variables are responsible for storing the I, speed and temperature.
        
        :mes_current:
            substrate heating current.
        
        :mes_speed:
            rpm.
        
        :mes_temperature:
            temperature near the substrate.

        Set values for active unit.

        :seted_throttling:
            shutter opening level, %.

        :seted_cur_heat:
            heating current.

        :seted_rotational_speed:
            rotational speed.
        """

        self.state_NL = False
        self.state_ND = False
        self.state_VE4_open = False
        self.state_VE4_close = False
        self.sate_comand_open_VE4 = False
        self.sate_comand_close_VE4 = False
        self.state_VE4_move = False
        self.state_throttling = False
        self.state_heat = False
        self.state_rotation = False
        self.chmb_open = False

        self.mes_current = 0
        self.mes_speed = 0
        self.mes_temperature = 0

        self.seted_throttling = 0
        self.seted_cur_heat = 0
        self.seted_rot_speed = 0

        self.bus = bus
        self.msg_send_upr = can.Message(
            arbitration_id=self.id_blockRasp_command,
            is_extended_id=True,
            dlc=8,
            data=bytearray(8),
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

    def set_pump(self, pump: str, state: bool):
        """turns on / off pumps.
        """

        if pump == "NL":
            if state:
                self.state_NL = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x01]
            else:
                self.state_NL = False
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x02]

        if pump == "ND":
            if state:
                self.state_ND = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x03]
            else:
                self.state_ND = False
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x04]

        self.send_and_flush(self.msg_send_upr)

    def set_valve_VE4(self, state: bool, gap=None):
        """Open and close valve VE4.
        """
        if gap is None:
            if state:
                self.state_VE4_open = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x05]
            else:
                self.state_VE4_close = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x06]
        else:
            self.state_VE4_close, self.state_VE4_open = False, False
            self.msg_send_upr[:3] = [0x11, 0x00, 0x10]

        self.send_and_flush(self.msg_send_upr)

    def set_throttling(self, state: bool, value=0):
        """Enable throttling mode. (This mode is not used (reserve)
        """

        if state:
            self.state_throttling = True
            self.seted_throttling = value
            self.msg_send_upr.data[0] = b"\x26"[0]
            self.msg_send_upr.data[2] = value
        else:
            self.state_throttling = False
            self.msg_send_upr.data[:3] = b"\x27"[0]

        self.send_and_flush(self.msg_send_upr)

    def set_heat(self, state: bool, value=0):
        """Enable or disable heat of substrate
        """

        if state:
            self.state_heat = True
            self.seted_cur_heat = value
            self.msg_send_upr.data[0] = b"\x22"[0]
            self.msg_send_upr.data[2:4] = value.to_bytes(2, "little")
        else:
            self.state_heat = False
            self.msg_send_upr.data[0] = b"\x23"[0]

        self.send_and_flush(self.msg_send_upr)

    def set_rotation(self, state: bool, value=0):
        """Enable or disable rotatoin of substrate
        """

        if state:
            self.state_rotation = True
            self.seted_rot_speed = value
            self.msg_send_upr.data[0] = b"\x24"[0]
            self.msg_send_upr.data[2] = value
        else:
            self.state_rotation = False
            self.msg_send_upr.data[0] = b"\x25"[0]

        self.send_and_flush(self.msg_send_upr)

    def send_and_flush(self, msg):
        """Send fun with callbcak Eror
        """
        try:
            self.bus.send(msg)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            msg.data[:8] = bytearray(8)

    def return_states_mes(self):
        return (
            {
                "mes_current": self.mes_current,
                "mes_speed": self.mes_speed,
                "mes_temperature": self.mes_temperature,
            },
            {
                "state_NL": self.state_NL,
                "state_ND": self.state_ND,
                "state_VE4_open": self.state_VE4_open,
                "state_VE4_close": self.state_VE4_close,
                "sate_comand_open_VE4": self.sate_comand_open_VE4,
                "sate_comand_close_VE4": self.sate_comand_close_VE4,
                "state_VE4_move": self.state_VE4_move,
                "state_throttling": self.state_throttling,
                "state_heat": self.state_heat,
                "state_rotation": self.state_rotation,
                "chmb_open": self.chmb_open,
                "seted_throttling": self.seted_throttling,
                "seted_cur_heat": self.seted_cur_heat,
                "seted_rot_speed": self.seted_rot_speed,
            },
        )