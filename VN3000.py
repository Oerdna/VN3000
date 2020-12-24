import can
import os
import threading
import json
import time
from pprint import pprint
from blockUpr import BlockUPR
from blockRasp import BlockRasp
from blockDC import BlockDC
from blockRF import BlockRF
from Parser import Parser


class VN3000:
    """Class for installation"""

    def __init__(self):
        """
        Load settings for VN3000
        """

        with open("vn3000.json") as f_obj:
            templates = json.load(f_obj)

        self.dcBlock = templates["presetting"].get("dcBlock")
        self.rfBlock = templates["presetting"].get("rfBlock")
        self.highVoltageBlock = templates["presetting"].get("highVoltageBlock")
        self.pressureTurbine_start = templates["pressureSettings"].get(
            "pressureTurbine"
        )
        self.pressureSensorPG_enable = templates["pressureSettings"].get(
            "pressureIonVacuumi"
        )

        try:
            if os.name == "nt":
                self.bus = can.ThreadSafeBus(
                    bustype="systec", channel="0", bitrate=1000000
                )
            else:
                os.system(
                    "echo password|sudo -S ip link set can0 type can bitrate 1000000"
                )
                os.system("echo password|sudo -S ip link set up can0")
                self.bus = can.ThreadSafeBus(channel="can0", bustype="socketcan")
        except can.CanError:
            print("Hardware or CAN interface initialization failed.")
            input()

        self.blk_upr = BlockUPR(self.bus)
        self.blk_rasp = BlockRasp(self.bus)
        self.blk_dc = BlockDC(self.bus)
        self.blk_rf = BlockRF(self.bus)
        self.parser = Parser(
            blockUpr=self.blk_upr,
            blockRasp=self.blk_rasp,
            blockDc=self.blk_dc,
            blockRf=self.blk_rf,
        )

    def star_work(self):
        """Getting started, the foundation of the program"""
        print("VN3000 init:")

        self.blk_upr.get_states()
        self.blk_upr.get_measurements()
        self.blk_rasp.get_states()
        self.blk_rasp.get_measurements()
        self.blk_dc.get_states()
        self.blk_dc.get_measurements()
        self.blk_rf.get_states()
        self.blk_rf.get_measurements()

        self.reader_m4()
        time.sleep(1)

        upr = self.blk_upr.return_states_mes()
        ras = self.blk_rasp.return_states_mes()
        dc = self.blk_dc.return_states_mes()
        rf = self.blk_rf.return_states_mes()
        print("Status block Upr:")
        pprint(upr)
        print("Status block Rasp:")
        pprint(ras)
        print("Status block DC")
        pprint(dc)
        print("Status block RF")
        pprint(rf)

        # self.periodic_send()

    def get_measurements(self):
        self.blk_upr.get_measurements()
        self.blk_rasp.get_measurements()
        if self.blk_dc.block_dc_enable:
            self.blk_dc.get_measurements()
        if self.blk_rf.block_rf_enable:
            self.blk_rf.get_measurements()

    def periodic_send(self):
        self.get_measurements()
        self.t = threading.Timer(0.5, self.periodic_send)
        self.t.start()

    def end_work(self):
        """Close CAN-USB bus and clear other stuff"""
        self.noti.stop()
        # self.t.cancel()
        self.bus.shutdown()
        if os.name == "posix":
            os.system("echo password|sudo -S ip link set down can0")

    def check_phase(self):
        """Checking electrical phase"""
        if self.blk_rasp.phase_electric == False:
            return -11

    def enable_NF(self):
        """Enable pump NF:
            | Cheking: NF, VE4.
        """
        if self.blk_rasp.state_NF == False and (
            self.blk_rasp.state_VE4_close == True
            or self.blk_rasp.state_VE4_open == True
        ):
            self.blk_rasp.set_pump("NF", True)
        elif (
            self.blk_rasp.state_VE4_close == False
            and self.blk_rasp.state_VE4_open == False
        ):
            return -1

    def disable_NF(self):
        """Disable pump NF:
            | Cheking: NT, NF, VE2, VE3.
        """
        if (
            self.blk_rasp.state_NF == True
            and self.blk_rasp.state_NT == False
            and self.blk_upr.state_VE3 == False
            and self.blk_upr.state_VE2 == False
        ):
            self.blk_rasp.set_pump("NF", False)
        elif self.blk_rasp.state_NT == True:
            return -2
        elif self.blk_upr.state_VE2 == True:
            return -3
        elif self.blk_upr.state_VE3 == True:
            return -4

    def enable_NT(self):
        """Enable pump NT:
            | Cheking: NT, Preasure P2, Water 1.
        """
        if (
            self.blk_rasp.state_NT == False
            and self.blk_upr.pressure_pmp < self.pressureTurbine_start
            and self.blk_upr.water_1 == True
        ):
            self.blk_rasp.set_pump("NT", True)
        elif self.blk_upr.water_1 == False:
            self.blk_upr.set_sound(True)
            return -5
        elif self.blk_upr.pressure_pmp > self.pressureTurbine_start:
            return -6

    def disable_NT(self):
        """Disable pump NT:
            | Cheking: NT.
        """
        if self.blk_rasp.state_NT == True:
            self.blk_rasp.set_pump("NT", False)
            return -13

    def open_VE4(self):
        """Open butterfly valve VE4:
            | Cheking: VE4, VE1, Chamber, VE3, Pressure
        """
        if (
            (
                self.blk_rasp.state_VE4_close == True
                or (
                    self.blk_rasp.state_VE4_open == False
                    and self.blk_rasp.state_VE4_close == False
                )
            )
            and self.blk_upr.state_VE1 == False
            and self.blk_rasp.state_chmb_open == False
            and self.blk_upr.state_VE3 == False
            and self.blk_upr.pressure_ch < self.pressureTurbine_start
        ):
            self.blk_rasp.set_valve_VE4(True)
        elif self.blk_upr.state_VE1 == True:
            return -8
        elif self.blk_rasp.state_chmb_open == True:
            return -9
        elif self.blk_upr.state_VE3 == True:
            return -4
        elif self.blk_upr.pressure_ch > self.pressureTurbine_start:
            return -12

    def close_VE4(self):
        """Close butterfly valve VE4:
            | Cheking: VE4
        """
        if self.blk_rasp.state_VE4_open == True or (
            self.blk_rasp.state_VE4_open == False
            and self.blk_rasp.state_VE4_close == False
        ):
            self.blk_rasp.set_valve_VE4(False)

    def open_VE1(self):
        """Open valve VE1:
            | Cheking: VE1, VE4, VE3
        """
        if (
            self.blk_rasp.state_VE4_close == True
            and self.blk_upr.state_VE3 == False
            and self.blk_upr.state_VE1 == False
        ):
            self.blk_upr.set_valve("VE1", True)
        elif self.blk_rasp.state_VE4_close == False:
            return -7
        elif self.blk_upr.state_VE3 == True:
            return -4

    def close_VE1(self):
        """Close valve VE1:
            | Cheking: VE1
        """
        if self.blk_upr.state_VE1 == True:
            self.blk_upr.set_valve("VE1", False)

    def open_VE2(self):
        """Open valve VE2:
            | Cheking: VE2, VE3.
        """
        if self.blk_upr.state_VE2 == False and self.blk_upr.state_VE3 == False:
            self.blk_upr.set_valve("VE2", True)
        elif self.blk_upr.state_VE3 == True:
            return -4

    def close_VE2(self):
        """Close valve VE2. 
            | Cheking: VE2
        """
        if self.blk_upr.state_VE2 == True:
            self.blk_upr.set_valve("VE2", False)

    def open_VE3(self):
        """Open valve VE3:
            | Cheking: VE3, VE2, VE1, Chamber.
        """
        if (
            self.blk_upr.state_VE3 == False
            and self.blk_upr.state_VE2 == False
            and self.blk_upr.state_VE1 == False
            and self.blk_rasp.state_chmb_open == False
            and self.blk_rasp.state_VE4_close == True
        ):
            self.blk_upr.set_valve("VE3", True)
        elif self.blk_upr.state_VE2 == True:
            return -3
        elif self.blk_upr.state_VE1 == True:
            return -8
        elif self.blk_rasp.state_chmb_open == True:
            return -9

    def close_VE3(self):
        """Close valve VE3. 
            | Cheking: VE3
        """
        if self.blk_upr.state_VE3 == True:
            self.blk_upr.set_valve("VE3", False)

    def disable_sound(self):
        """Disable sound 
            | Cheking: sound
        """
        self.blk_upr.set_sound(False)

    def enable_PG(self):
        """Enable sensor PG:
            | Cheking: PG, Presure for sensor.
        """
        if (
            self.blk_upr.state_PG == False
            and self.blk_upr.pressure_ch < self.pressureSensorPG_enable
        ):
            self.blk_upr.set_sensor_PG(True)
        elif self.blk_upr.pressure_ch > self.pressureSensorPG_enable:
            return -10

    def disable_PG(self):
        """Disable sensor PG:
            | Cheking: PG
        """
        if self.blk_upr.state_PG == True:
            self.blk_upr.set_sensor_PG(False)

    def enable_inlent_ZQ1(self, value):
        """Open ZQ1 valve
        """
        self.blk_upr.set_gas_inlet("ZQ1", True, value)

    def change_ZQ1(self, value):
        """Change ZQ1 value
        """
        if 0 <= value <= 255:
            self.blk_upr.set_voltage_ZQ1 = value

    def get_ZQ1(self):
        return self.blk_upr.set_voltage_ZQ1

    def close_ZQ1(self):
        """Close ZQ1 valve
        """
        self.blk_upr.set_gas_inlet("ZQ1", False)

    def enable_inlent_ZQ2(self, value):
        """Open ZQ2 valve
        """
        self.blk_upr.set_gas_inlet("ZQ2", True, value)

    def change_ZQ2(self, value):
        """Change ZQ2 value
        """
        if 0 <= value <= 255:
            self.blk_upr.set_voltage_ZQ2 = value

    def get_ZQ2(self):
        return self.blk_upr.set_voltage_ZQ2

    def close_ZQ2(self):
        """Close ZQ2 valve
        """
        self.blk_upr.set_gas_inlet("ZQ2", False)

    def enable_heat_sub(self, value):
        """Enable heat of substrate
        """
        self.blk_rasp.set_heat(True, value)

    def change_heat_sub(self, value):
        """Chnage heat of substrate
        """
        if 0 <= value <= 5500:
            self.blk_rasp.seted_cur_heat = value

    def get_heat_sub(self):
        return self.blk_rasp.seted_cur_heat

    def disable_heat_sub(self):
        """Disable heat of substrate
        """
        self.blk_rasp.set_heat(False)

    def enable_rotation_sub(self, value):
        """Enable rotation of substrate
        """
        self.blk_rasp.set_rotation(True, value)

    def change_rotation_sub(self, value):
        """Change rotation of substrate
        """
        if 0 <= value <= 100:
            self.blk_rasp.seted_rot_speed = value

    def get_rotation_sub(self):
        return self.blk_rasp.seted_rot_speed

    def disable_rotation_sub(self):
        """Disable rotation of substrate
        """
        self.blk_rasp.set_rotation(False)

    def enable_dc_block(self):
        """Enable dc block
            | Cheking: block state, chamber, VE1, water
        """
        if (
            self.blk_dc.block_dc_state == True
            and self.blk_rasp.state_chmb_open == False
            and self.blk_upr.state_VE1 == False
            and self.blk_upr.water_2 == True
            and self.blk_dc.block_dc_enable == False
        ):
            self.blk_dc.state_block_dc(True)
        elif self.blk_upr.state_VE1 == True:
            return -8
        elif self.blk_upr.water_2 == False:
            return -14
        elif self.blk_rasp.state_chmb_open == True:
            return -9
        elif self.blk_dc.block_dc_state == False:
            return -16

    def disable_dc_block(self):
        """Disable dc block
        """
        if self.blk_dc.block_dc_enable == True:
            self.disable_dc_sputtering()
            self.blk_dc.state_block_dc(False)

    def enable_dc_sputtering(self, value):
        """Enable sputtering:
            | Cheking: block enable, water, VE1, chamber
        """
        if (
            self.blk_dc.block_dc_enable == True
            and self.blk_rasp.state_chmb_open == False
            and self.blk_upr.state_VE1 == False
            and self.blk_upr.water_2 == True
        ):
            self.blk_dc.current_dc(True, value)
        elif self.blk_rasp.state_chmb_open == True:
            return -9
        elif self.blk_upr.state_VE1 == True:
            return -8
        elif self.blk_upr.water_2 == False:
            return -14
        elif self.blk_dc.block_dc_enable == False:
            return -15

    def change_dc_sputtering(self, value):
        """Change current for dc block
        """
        if 0 <= value <= 255:
            self.blk_dc.range_current = value

    def get_dc_sputtering(self):
        return self.blk_dc.range_current

    def disable_dc_sputtering(self):
        """Disable sputtering
        """
        self.blk_dc.current_dc(False)

    def enable_rf_block(self):
        """Enable rf block
            | Cheking: block state, chamber, VE1, water
        """
        if (
            self.blk_rf.block_rf_state == True
            and self.blk_rasp.state_chmb_open == False
            and self.blk_upr.state_VE1 == False
            and self.blk_upr.water_2 == True
            and self.blk_rf.block_rf_enable == False
        ):
            self.blk_rf.state_block_rf(True)
        elif self.blk_upr.state_VE1 == True:
            return -8
        elif self.blk_upr.water_2 == False:
            return -14
        elif self.blk_rasp.state_chmb_open == True:
            return -9
        elif self.blk_rf.block_rf_state == False:
            return -17

    def disable_rf_block(self):
        """Disable rf block
        """
        if self.blk_rf.block_rf_enable == True:
            self.disable_rf_sputtering()
            self.blk_rf.state_block_rf(False)

    def cheking_rf_sputtering(self):
        """Cheking rf magnetron by pre- sputtering process
        """
        if (
            self.blk_rf.block_rf_enable == True
            and self.blk_rf.block_rf_ready == True
            and self.blk_rf.block_rf_sputtering == False
            and self.blk_rasp.state_chmb_open == False
            and self.blk_upr.state_VE1 == False
            and self.blk_upr.water_2 == True
        ):
            self.blk_rf.check_rf(True)
        elif self.blk_rasp.state_chmb_open == True:
            return -9
        elif self.blk_upr.state_VE1 == True:
            return -8
        elif self.blk_upr.water_2 == False:
            return -14
        elif self.blk_rf.block_rf_enable == False:
            return -18
        elif self.blk_rf.block_rf_ready == False:
            return -19

    def disable_cheking_rf_sputtering(self):
        """Disable pre- sputtering
        """
        if self.blk_rf.block_rf_sputtering:
            self.blk_rf.check_rf(False)

    def enable_rf_sputtering(self, value):
        """Enable sputtering:
            | Cheking: block enable, water, VE1, chamber
        """
        if (
            self.blk_rf.block_rf_enable == True
            and self.blk_rf.block_rf_ready == True
            and self.blk_rasp.state_chmb_open == False
            and self.blk_upr.state_VE1 == False
            and self.blk_upr.water_2 == True
        ):
            self.blk_rf.power_rf(True, value)
        elif self.blk_rasp.state_chmb_open == True:
            return -9
        elif self.blk_upr.state_VE1 == True:
            return -8
        elif self.blk_upr.water_2 == False:
            return -14
        elif self.blk_rf.block_rf_enable == False:
            return -18
        elif self.blk_rf.block_rf_ready == False:
            return -19

    def change_rf_sputtering(self, value):
        """Change current for dc block
        """
        if 0 <= value <= 500:
            self.blk_rf.range_power = value

    def get_rf_sputtering(self):
        return self.blk_rf.range_power

    def disable_rf_sputtering(self):
        """Disable sputtering
        """
        self.blk_rf.power_rf(False)

    def reset_rf_error(self):
        """reset error bool
        """
        self.blk_rf.error = False

    """
    Enable/disable capacity С1/2 increase/reduction
    """

    def Cap1upStart(self):
        self.blk_rf.cap_state("C1", "up", True)

    def Cap2upStart(self):
        self.blk_rf.cap_state("C2", "up", True)

    def Cap1upStop(self):
        self.blk_rf.cap_state("C1", "up", False)

    def Cap2upStop(self):
        self.blk_rf.cap_state("C2", "up", False)

    def Cap1downStart(self):
        self.blk_rf.cap_state("C1", "down", True)

    def Cap2downStart(self):
        self.blk_rf.cap_state("C2", "down", True)

    def Cap1downStop(self):
        self.blk_rf.cap_state("C1", "down", False)

    def Cap2downStop(self):
        self.blk_rf.cap_state("C2", "down", False)

    """
    Reading methodes
    """

    def reader_m2(self):
        """Method 2 for read recv msg from bus
        """
        print("Read from Bus: M2")
        msg = self.bus.recv(0.02)
        if msg is not None:
            print(msg.data)

    def reader_m4(self):
        """Method 4
        """
        print("Read from Bus: M4")
        self.noti = can.Notifier(self.bus, [self.parser.read_input])

    def get_values_for_update(self):
        """
        Return ALL Measurement
        """
        rasp = self.blk_rasp.return_mes()
        upr = self.blk_upr.return_mes()
        dc = self.blk_dc.return_mes()
        rf = self.blk_rf.return_mes()
        return {**rasp, **upr, **dc, **rf}

    def get_values_for_states(self):
        """
        Return ALL States
        """
        rasp = self.blk_rasp.return_states()
        upr = self.blk_upr.return_states()
        dc = self.blk_dc.return_states()
        rf = self.blk_rf.return_states()
        return {**rasp, **upr, **dc, **rf}
