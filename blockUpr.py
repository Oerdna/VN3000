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
        
        :water_1:
            sensor water activ.

        :water_2:
            sensor water activ.

        :water_3:
            sensor water activ.

        :turbine_active:
            turbine is ready.

        Seted voltage applied to the valve.

        :voltage_ZQ1 & voltage_ZQ2:
            valve ZQ1 & valve ZQ2.
        """
        self.pressure_ch = 0.02
        self.pressure_pmp = 0.02
        self.pressure_pg = 0.02
        self.mes_pg_current = 0
        self.mes_ZQ1_voltage = 0
        self.mes_ZQ2_voltage = 0
        self.mes_pmt6_1 = 0
        self.mes_pmt6_2 = 0

        """
        States of nodes
        """
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
        self.turbine_active = False

        """
        Gas inlent value
        """
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
        msg = self.msg_send_upr
        msg.data[0] = b"\x0f"[0]
        self.send_and_flush(msg)

    def get_measurements(self):
        """called to get values from sensors.
        """
        msg = self.msg_send_upr
        msg.data[0] = b"\xff"[0]
        self.send_and_flush(msg)

    def set_valve(self, VE: str, state: bool):
        """Opens and close valve.
        """
        if VE == "VE1":
            if state:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x10]
            else:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x1F]
        elif VE == "VE2":
            if state:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x20]
            else:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x2F]
        elif VE == "VE3":
            if state:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x30]
            else:
                msg = self.msg_send_upr
                msg.data[:3] = [0x11, 0x00, 0x3F]
        self.send_and_flush(msg)

    def set_sound(self, state: bool):
        """toggle sound state.
        """
        if state:
            msg = self.msg_send_upr
            msg.data[0] = b"\xa0"[0]
        else:
            msg = self.msg_send_upr
            msg.data[0] = b"\xaf"[0]
        self.send_and_flush(msg)

    def set_sensor_PG(self, state: bool):
        """toggle PG sensor state.
        """
        if state:
            msg = self.msg_send_upr
            msg.data[0] = b"\x22"[0]
        else:
            msg = self.msg_send_upr
            msg.data[0] = b"\x23"[0]
        self.send_and_flush(msg)

    def set_gas_inlet(self, name: str, state: bool, value: int = 0):
        """gas flow control.
        """
        if name == "ZQ1":
            if state:
                msg = self.msg_send_upr
                msg.data[0] = b"\x40"[0]
                msg.data[2] = value
            else:
                msg = self.msg_send_upr
                msg.data[0] = b"\x4f"[0]
        elif name == "ZQ2":
            if state:
                msg = self.msg_send_upr
                msg.data[0] = b"\x50"[0]
                msg.data[2] = value
            else:
                msg = self.msg_send_upr
                msg.data[0] = b"\x5f"[0]
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
            "pressure_ch": self.pressure_ch / 133,
            "pressure_pmp": self.pressure_pmp / 133,
            "pressure_pg": self.pressure_pg / 133,
            "mes_pg_current": self.mes_pg_current / 1250,
            "mes_ZQ1_voltage": self.mes_ZQ1_voltage,
            "mes_ZQ2_voltage": self.mes_ZQ2_voltage,
            "mes_pmt6_1": self.mes_pmt6_1 / 146.3,
            "mes_pmt6_2": self.mes_pmt6_2 / 146.3,
            "state_VE1": self.state_VE1,
            "state_VE2": self.state_VE2,
            "state_VE3": self.state_VE3,
            "state_PG": self.state_PG,
            "state_ZQ1": self.state_ZQ1,
            "state_ZQ2": self.state_ZQ2,
            "state_sound": self.state_sound,
            "set_voltage_ZQ1": self.set_voltage_ZQ1,
            "set_voltage_ZQ2": self.set_voltage_ZQ2,
            "water_1": self.water_1,
            "water_2": self.water_2,
            "water_3": self.water_3,
            "turbine_active": self.turbine_active,
        }

    def return_mes(self):
        return {
            "pressure_ch": self.pressure_ch / 133,
            "pressure_pmp": self.pressure_pmp / 133,
            "pressure_pg": self.pressure_pg / 133,
            "mes_pg_current": self.mes_pg_current / 1250,
            "mes_ZQ1_voltage": self.mes_ZQ1_voltage,
            "mes_ZQ2_voltage": self.mes_ZQ2_voltage,
            "mes_pmt6_1": self.mes_pmt6_1 / 146.3,
            "mes_pmt6_2": self.mes_pmt6_2 / 146.3,
            "state_VE1": self.state_VE1,
            "state_VE2": self.state_VE2,
            "state_VE3": self.state_VE3,
            "state_ZQ1": self.state_ZQ1,
            "state_ZQ2": self.state_ZQ2,
            "water_1": self.water_1,
            "water_2": self.water_2,
            "water_3": self.water_3,
            "turbine_active": self.turbine_active,
        }

    def return_states(self):
        return {
            "state_VE1": self.state_VE1,
            "state_VE2": self.state_VE2,
            "state_VE3": self.state_VE3,
            "state_PG": self.state_PG,
            "state_ZQ1": self.state_ZQ1,
            "state_ZQ2": self.state_ZQ2,
            "set_voltage_ZQ1": self.set_voltage_ZQ1,
            "set_voltage_ZQ2": self.set_voltage_ZQ2,
        }
