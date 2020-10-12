import can


class BlockRasp:
    """this class implements interaction with the distribution unit.
    """

    """id - the frame identifier used for arbitration on the bus.
    """
    id_blockRasp_command = 0x101E0070

    def __init__(self, bus: object):
        """States of the working units of the block.

        :state_NF:
            foreline pump.

        :state_NT:
            turbomolecular pump.
        
        :state_VE4_open:
            state of microswitch the valve VE4.

        :state_VE4_close:
            state of microswitch the valve VE4.

        :state_throttling:
            enable of throttling the shutter.

        :state_heat:
            heating the substrate.

        :state_rotation:
            substrate rotation.
        
        :state_chmb_open:
            chamber is open.

        :back_door_close:
            back door is close.

        :phase_electric:
            phase electric is have.

        :turbine_break:
            turbine is break

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

        self.state_NF = False
        self.state_NT = False
        self.state_VE4_open = False
        self.state_VE4_close = False
        self.state_comand_open_VE4 = False
        self.state_comand_close_VE4 = False
        self.state_throttling = False
        self.state_heat = False
        self.state_rotation = False
        self.state_chmb_open = False
        self.back_door_close = False
        self.phase_electric = False
        self.turbine_break = False

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
        msg = self.msg_send_upr
        msg.data[0] = b"\x0f"[0]
        self.send_and_flush(msg)

    def get_measurements(self):
        """called to get values from sensors.
        """
        msg = self.msg_send_upr
        msg.data[0] = b"\xff"[0]
        self.send_and_flush(msg)

    def set_pump(self, pump: str, state: bool):
        """turns on / off pumps.
        """
        if pump == "NF":
            if state:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x01]
            else:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x02]
        elif pump == "NT":
            if state:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x03]
            else:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x04]
        self.send_and_flush(msg)

    def set_valve_VE4(self, state: bool, gap=None):
        """Open and close valve VE4.
        """
        if gap is None:
            if state:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x05]
            else:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x06]
        else:
            msg = self.msg_send_upr
            msg.data[:3] = [0x11, 0x00, 0x10]
        self.send_and_flush(msg)

    def set_throttling(self, state: bool, value: int = 0):
        """USELESS, NEED POTENTIOMETER ||
        Enable throttling mode. (This mode is not used (reserve))    
        """
        if state:
            msg = self.msg_send_upr
            msg.data[0] = b"\x26"[0]
            msg.data[2] = value
        else:
            msg = self.msg_send_upr
            msg.data[:3] = b"\x27"[0]
        self.send_and_flush(msg)

    def set_heat(self, state: bool, value: int = 0):
        """Enable or disable heat of substrate
        """
        if state:
            msg = self.msg_send_upr
            msg.data[0] = b"\x22"[0]
            msg.data[2:4] = value.to_bytes(2, "little")
        else:
            msg = self.msg_send_upr
            msg.data[0] = b"\x23"[0]
        self.send_and_flush(msg)

    def set_rotation(self, state: bool, value: int = 0):
        """Enable or disable rotatoin of substrate
        """
        if state:
            msg = self.msg_send_upr
            msg.data[0] = b"\x24"[0]
            msg.data[2] = value
        else:
            msg = self.msg_send_upr
            msg.data[0] = b"\x25"[0]
        self.send_and_flush(msg)

    def send_and_flush(self, msg):
        """Send fun with callbcak Eror
        """
        try:
            self.bus.send(msg)
            # print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")

    def return_states_mes(self):
        return {
            "mes_current": self.mes_current,
            "mes_speed": self.mes_speed,
            "mes_temperature": self.mes_temperature,
            "state_NF": self.state_NF,
            "state_NT": self.state_NT,
            "state_VE4_open": self.state_VE4_open,
            "state_VE4_close": self.state_VE4_close,
            "state_comand_open_VE4": self.state_comand_open_VE4,
            "state_comand_close_VE4": self.state_comand_close_VE4,
            "state_throttling": self.state_throttling,
            "state_heat": self.state_heat,
            "state_rotation": self.state_rotation,
            "state_chmb_open": self.state_chmb_open,
            "seted_throttling": self.seted_throttling,
            "seted_cur_heat": self.seted_cur_heat,
            "seted_rot_speed": self.seted_rot_speed,
            "back_door_close": self.back_door_close,
            "phase_electric": self.phase_electric,
            "turbine_break": self.turbine_break,
        }

    def return_mes(self):
        return {
            "mes_current": self.mes_current,
            "mes_speed": self.mes_speed,
            "mes_temperature": self.mes_temperature,
            "state_NF": self.state_NF,
            "state_NT": self.state_NT,
            "state_VE4_open": self.state_VE4_open,
            "state_VE4_close": self.state_VE4_close,
            "state_comand_open_VE4": self.state_comand_open_VE4,
            "state_comand_close_VE4": self.state_comand_close_VE4,
            "state_chmb_open": self.state_chmb_open,
        }

    def return_states(self):
        return {
            "state_NF": self.state_NF,
            "state_NT": self.state_NT,
            "state_VE4_open": self.state_VE4_open,
            "state_VE4_close": self.state_VE4_close,
            "state_comand_open_VE4": self.state_comand_open_VE4,
            "state_comand_close_VE4": self.state_comand_close_VE4,
            "state_heat": self.state_heat,
            "state_rotation": self.state_rotation,
            "state_chmb_open": self.state_chmb_open,
            "seted_cur_heat": self.seted_cur_heat,
            "seted_rot_speed": self.seted_rot_speed,
        }
