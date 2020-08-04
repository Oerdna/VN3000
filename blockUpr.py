import can


class BlockUPR:
    """this class implements interaction with the control unit.
    """

    """id - the frame identifier used for arbitration on the bus.
    """
    id_blockUPR_command = 0x181E0E50
    id_blockUPR_measurements = 0x181E0E60
    id_blockUPR_events = 0x181E0E40

    def __init__(self, bus: object):
        """Variables are responsible for storing the pressure value, I and U.
        
        :pressure_ch:
            in chamber.

        :pressure_pmp:
            near the pump.

        :pressure_pg:
            in the chamber, ionization sensor, work carefully.
        
        :pg_current:
            ionization gauge current.
        
        :ZQ1_voltage_mes & ZQ2_voltage_mes:
            effective voltage applyed to the piezoelectric.

        States of the working units of the block.

        :state_VE1:
            sink.

        :state_VE2:
            valve to the turbine.

        :state_VE3:
            valve to the chamber.

        :state_PG:
            ionization sensor.

        :state_ZQ1 & state_ZQ2:
            gas inlet 1 and gas inlet 2.

        :state_sound:
            sound signal.

        Seted voltage applied to the valve.

        :voltage_ZQ1 & voltage_ZQ2:
            valve ZQ1 & valve ZQ2.
        """
        self.pressure_ch = 0
        self.pressure_pmp = 0
        self.pressure_pg = 0
        self.mes_pg_current = 0
        self.mes_ZQ1_voltage = 0
        self.mes_ZQ2_voltage = 0

        self.state_VE1 = False
        self.state_VE2 = False
        self.state_VE3 = False
        self.state_PG = False
        self.state_ZQ1 = False
        self.state_ZQ2 = False
        self.state_sound = False

        self.set_voltage_ZQ1 = 0
        self.set_voltage_ZQ2 = 0

        self.bus = bus
        self.msg_send_upr = can.Message(
            arbitration_id=self.id_blockUPR_command,
            is_extended_id=True,
            dlc=8,
            data=bytearray(8),
        )
        self.msg_get_measurements = can.Message(
            arbitration_id=self.id_blockUPR_measurements, is_extended_id=True, dlc=8
        )
        self.msg_get_events = can.Message(
            arbitration_id=self.id_blockUPR_events, is_extended_id=True, dlc=8
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

    def set_valve(self, VE: str, state: bool):
        """Opens and close valve.
        """

        if VE == 'VE1':
            if state:
                self.state_VE1 = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x10]
            else:
                self.state_VE1 = False
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x1F]

        if VE == 'VE2':
            if state:
                self.state_VE2 = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x20]
            else:
                self.state_VE2 = False
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x2F]

        if VE == 'VE3':
            if state:
                self.state_VE3 = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x30]
            else:
                self.state_VE3 = False
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x3F]

        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[:3] = bytearray(3)

    def set_sound(self, state: bool):
        """toggle sound state.
        """

        if state:
            self.state_sound = True
            self.msg_send_upr.data[0] = b"\xa0"[0]

        if state:
            self.state_sound = False
            self.msg_send_upr.data[0] = b"\xaf"[0]

        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[0] = b"\x00"[0]

    def set_sensor_PG(self, state: bool):
        """toggle PG sensor state.
        """

        if state:
            self.state_PG = True
            self.msg_send_upr.data[0] = b"\x22"[0]

        if state:
            self.state_PG = False
            self.msg_send_upr.data[0] = b"\x23"[0]

        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[0] = b"\x00"[0]

    def set_gas_inlet(self, name: str, state: bool, value=0):
        """gas flow control.
        """

        if name == 'ZQ1':
            if state:
                self.state_ZQ1 = True
                self.msg_send_upr[0] = b"\x40"
                self.set_voltage_ZQ1 = value
                self.msg_send_upr[2] = value
            else:
                self.state_ZQ1 = False
                self.msg_send_upr[0] = b"\x4f"

        if name == 'ZQ2':
            if state:
                self.state_ZQ2 = True
                self.msg_send_upr[0] = b"\x50"
                self.set_voltage_ZQ2 = value
                self.msg_send_upr[2] = value
            else:
                self.state_ZQ2 = False
                self.msg_send_upr[0] = b"\x5f"

        try:
            self.bus.send(self.msg_send_upr)
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
        finally:
            self.msg_send_upr.data[:3] = bytearray(3)