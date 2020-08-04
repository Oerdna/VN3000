import can


class BlockRasp:
    """this class implements interaction with the distribution unit.
    """

    """id - the frame identifier used for arbitration on the bus.
    """
    id_blockRasp_command = 0x101E0070
    id_blockRasp_measurements = 0x101E0060
    id_blockRasp_events = 0x101E0065

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
        self.state_throttling = False
        self.state_heat = False
        self.state_rotation = False

        self.mes_current = 0
        self.mes_speed = 0
        self.mes_temperature = 0

        self.seted_throttling = 0
        self.seted_cur_heat = 0
        self.seted_rotational_speed = 0

        self.bus = bus
        self.msg_send_upr = can.Message(
            arbitration_id=self.id_blockRasp_command,
            is_extended_id=True,
            dlc=8,
            data=bytearray(8),
        )
        self.msg_get_measurements = can.Message(
            arbitration_id=self.id_blockRasp_measurements, is_extended_id=True, dlc=8
        )
        self.msg_get_events = can.Message(
            arbitration_id=self.id_blockRasp_events, is_extended_id=True, dlc=8
        )

    def get_states(self):
        """call to get the actual states of the units.
        """

        self.msg_send_upr.data[0] = b"\x0f"[0]
        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[0] = b"\x00"[0]

    def get_measurements(self):
        """called to get values from sensors.
        """

        self.msg_send_upr.data[0] = b"\xff"[0]
        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[0] = b"\x00"[0]

    def set_pump(self, pump: str, state: bool):
        """turns on / off pumps.
        """

        if pump == 'NL':
            if state:
                self.state_NL = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x01]
            else:
                self.state_NL = False
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x02]

        if pump == 'ND':
            if state:
                self.state_ND = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x03]
            else:
                self.state_ND = False
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x04]

        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[:3] = bytearray(3)

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

        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[:3] = bytearray(3)

    def set_throttling(self, state: bool, value=0):
        """Enable throttling mode. (This mode is not used (reserve)
        """

        if state:
            self.state_throttling = True
            self.seted_throttling = value
            self.msg_send_upr.data[0] = b"\x26"
            self.msg_send_upr.data[2] = value
        else:
            self.state_throttling = False
            self.msg_send_upr.data[:3] = b"\x27"

        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[:3] = bytearray(3)

    def set_heat(self, state: bool, value=0):
        """Enable or disable heat of substrate
        """

        if state:
            self.state_heat = True
            self.seted_cur_heat = value
            self.msg_send_upr.data[0] = b"\x22"
            self.msg_send_upr.data[2:4] = value.to_bytes(2, 'little')
        else:
            self.state_heat = False
            self.msg_send_upr.data[0] = b"\x23"

        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[:4] = bytearray(4)

    def set_rotation(self, state: bool, value=0):
        """Enable or disable rotatoin of substrate
        """

        if state:
            self.state_rotation = True
            self.seted_rotational_speed = value
            self.msg_send_upr.data[0] = b"\x24"
            self.msg_send_upr.data[2] = value
        else:
            self.state_rotation = False
            self.msg_send_upr.data[0] = b"\x25"

        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[:3] = bytearray(3)