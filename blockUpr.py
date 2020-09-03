import can


class BlockUPR:
    """this class implements interaction with the control unit.
    """

    """id - the frame identifier used for arbitration on the bus.
    """
    id_blockUPR_command = 0x181E0E50

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
        self.mes_pmt6_1 = 0
        self.mes_pmt6_2 = 0

        self.state_VE1 = False
        self.state_VE2 = False
        self.state_VE3 = False
        self.state_PG = False
        self.state_ZQ1 = False
        self.state_ZQ2 = False
        self.state_sound = False

        self.water_1 = False
        self.water_2 = False
        self.water_3 = False
        self.turbine = False

        self.set_voltage_ZQ1 = 0
        self.set_voltage_ZQ2 = 0

        self.bus = bus
        self.msg_send_upr = can.Message(
            arbitration_id=self.id_blockUPR_command,
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

    def set_valve(self, VE: str, state: bool):
        """Opens and close valve.
        """

        if VE == "VE1":
            if state:
                self.state_VE1 = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x10]
            else:
                self.state_VE1 = False
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x1F]

        if VE == "VE2":
            if state:
                self.state_VE2 = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x20]
            else:
                self.state_VE2 = False
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x2F]

        if VE == "VE3":
            if state:
                self.state_VE3 = True
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x30]
            else:
                self.state_VE3 = False
                self.msg_send_upr.data[:3] = [0x11, 0x00, 0x3F]

        self.send_and_flush(self.msg_send_upr)

    def set_sound(self, state: bool):
        """toggle sound state.
        """

        if state:
            self.state_sound = True
            self.msg_send_upr.data[0] = b"\xa0"[0]

        if state:
            self.state_sound = False
            self.msg_send_upr.data[0] = b"\xaf"[0]

        self.send_and_flush(self.msg_send_upr)

    def set_sensor_PG(self, state: bool):
        """toggle PG sensor state.
        """

        if state:
            self.state_PG = True
            self.msg_send_upr.data[0] = b"\x22"[0]

        if state:
            self.state_PG = False
            self.msg_send_upr.data[0] = b"\x23"[0]

        self.send_and_flush(self.msg_send_upr)

    def set_gas_inlet(self, name: str, state: bool, value=0):
        """gas flow control.
        """

        if name == "ZQ1":
            if state:
                self.state_ZQ1 = True
                self.msg_send_upr[0] = b"\x40"[0]
                self.set_voltage_ZQ1 = value
                self.msg_send_upr[2] = value
            else:
                self.state_ZQ1 = False
                self.msg_send_upr[0] = b"\x4f"[0]

        if name == "ZQ2":
            if state:
                self.state_ZQ2 = True
                self.msg_send_upr[0] = b"\x50"[0]
                self.set_voltage_ZQ2 = value
                self.msg_send_upr[2] = value
            else:
                self.state_ZQ2 = False
                self.msg_send_upr[0] = b"\x5f"[0]

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
                "pressure_ch": self.pressure_ch,
                "pressure_pmp": self.pressure_pmp,
                "pressure_pg": self.pressure_pg,
                "mes_pg_current": self.mes_pg_current,
                "mes_ZQ1_voltage": self.mes_ZQ1_voltage,
                "mes_ZQ2_voltage": self.mes_ZQ2_voltage,
            },
            {
                "state_VE1": self.state_VE1,
                "state_VE2": self.state_VE2,
                "state_VE3": self.state_VE3,
                "state_PG": self.state_PG,
                "state_ZQ1": self.state_ZQ1,
                "state_ZQ2": self.state_ZQ2,
                "state_sound": self.state_sound,
                "set_voltage_ZQ1": self.set_voltage_ZQ1,
                "set_voltage_ZQ2": self.set_voltage_ZQ2,
            },
        )
