import can
import struct


class Parser:
    """Accepts messages from the installation and returns notifications.
    """

    dict_id = {
        "id_blockUpr_events": 0x181E0E40,
        "id_blockUPR_measurements": 0x181E0E60,
        "id_blockRasp_measurements": 0x101E0060,
        "id_blockRasp_events": 0x101E0065,
    }

    data_mes_upr = {
        "pressure_ch": 0x01,
        "pressure_pmp": 0x02,
        "pressure_pg": 0x03,
        "mes_pg_zq1_zq2": 0x04,
        "wtf": 0x05,
        "state_block": 0x0A,
    }

    data_mes_rasp = {
        "current_and_speed": 0x0B,
        "system": 0x0A,
        "mes_current_and_speed": 0x01,
    }

    def __init__(self, blockUpr: object, blockRasp: object):
        self.blockUpr = blockUpr
        self.blockRasp = blockRasp

    def read_input(self, msg):
        if msg.arbitration_id == self.dict_id["id_blockUPR_measurements"]:
            self.blockUPR_measurements(msg)
        elif msg.arbitration_id == self.dict_id["id_blockUpr_events"]:
            self.blockUpr_events(msg)
        elif msg.arbitration_id == self.dict_id["id_blockRasp_measurements"]:
            self.blockRasp_measurements(msg)
        elif msg.arbitration_id == self.dict_id["id_blockRasp_events"]:
            self.blockRasp_events(msg)

    def blockUPR_measurements(self, msg):
        """Measurement processing by data[0]
        """
        if msg.data[0] == self.data_mes_upr["pressure_ch"]:
            self.blockUpr.pressure_ch = struct.unpack("<f", msg.data[4:8])[0]
            # return struct.unpack("<f", msg.data[4:8])[0]
        elif msg.data[0] == self.data_mes_upr["pressure_pmp"]:
            self.blockUpr.pressure_pmp = struct.unpack("<f", msg.data[4:8])[0]
            # return struct.unpack("<f", msg.data[4:8])[0]
        elif msg.data[0] == self.data_mes_upr["pressure_pg"]:
            self.blockUpr.pressure_pg = struct.unpack("<f", msg.data[4:8])[0]
            # return struct.unpack("<f", msg.data[4:8])[0]
        elif msg.data[0] == self.data_mes_upr["mes_pg_zq1_zq2"]:
            self.blockUpr.mes_pg_current = struct.unpack("<H", msg.data[6:8])[0]
            self.blockUpr.mes_ZQ1_voltage = struct.unpack("<H", msg.data[2:4])[0]
            self.blockUpr.mes_ZQ2_voltage = struct.unpack("<H", msg.data[4:6])[0]
        elif msg.data[0] == self.data_mes_upr["wtf"]:
            self.blockUpr.mes_pmt6_1 = struct.unpack("<H", msg.data[2:4])[0]
            self.blockUpr.mes_pmt6_2 = struct.unpack("<H", msg.data[4:6])[0]
        elif msg.data[0] == self.data_mes_upr["state_block"]:
            self.blockUpr.state_VE1 = True if msg.data[3] & 1 else False
            self.blockUpr.state_VE2 = True if msg.data[3] & 2 else False
            self.blockUpr.state_VE3 = True if msg.data[3] & 4 else False
            self.blockUpr.state_PG = True if msg.data[3] & 8 else False
            self.blockUpr.state_ZQ1 = True if msg.data[3] & 16 else False
            self.blockUpr.set_voltage_ZQ1 = struct.unpack("<H", msg.data[4:6])[0]
            self.blockUpr.state_ZQ2 = True if msg.data[3] & 32 else False
            self.blockUpr.set_voltage_ZQ2 = struct.unpack("<H", msg.data[6:8])[0]

    def blockUpr_events(self, msg):
        """State processing by data[0]
        """
        if msg.data[0] == 0x01:
            if msg.data[2] & 240 == 16:
                if msg.data[2] & 15 == 15:
                    self.blockUpr.state_VE1 = False
                elif msg.data[2] & 15 == 0:
                    self.blockUpr.state_VE1 = True
                elif msg.data[2] & 15 == 9:
                    self.blockUpr.state_ZQ1 = False
                elif msg.data[2] & 15 == 8:
                    self.blockUpr.state_ZQ1 = True
            elif msg.data[2] & 240 == 32:
                self.blockUpr.state_VE2 = False if msg.data[2] & 15 else True
            elif msg.data[2] & 240 == 48:
                self.blockUpr.state_VE3 = False if msg.data[2] & 15 else True
            elif msg.data[2] & 240 == 80:
                self.blockUpr.water_1 = False if msg.data[2] & 15 else True
            elif msg.data[2] & 240 == 96:
                self.blockUpr.water_2 = False if msg.data[2] & 15 else True
            elif msg.data[2] & 240 == 112:
                self.blockUpr.water_3 = False if msg.data[2] & 15 else True
            elif msg.data[2] & 240 == 144:
                if msg.data[2] & 15 == 15:
                    self.blockUpr.turbine_active = True
                elif msg.data[2] & 15 == 0:
                    self.blockUpr.turbine_active = False
                elif msg.data[2] & 15 == 9:
                    self.blockUpr.state_ZQ2 = False
                elif msg.data[2] & 15 == 8:
                    self.blockUpr.state_ZQ2 = True

    def blockRasp_measurements(self, msg):
        if msg.data[0] == self.data_mes_rasp["system"]:
            self.blockRasp.state_NT = True if msg.data[3] & 1 else False
            self.blockRasp.state_NF = True if msg.data[3] & 2 else False
            self.blockRasp.state_heat = True if msg.data[3] & 4 else False
            self.blockRasp.state_rotation = True if msg.data[3] & 8 else False
            # self.blockRasp.state_throttling = True if msg.data[3] & 64 else False
            self.blockRasp.state_comand_open_VE4 = True if msg.data[3] & 16 else False
            self.blockRasp.state_comand_close_VE4 = True if msg.data[3] & 32 else False
            self.blockRasp.state_VE4_open = True if msg.data[2] & 16 else False
            self.blockRasp.state_VE4_close = True if msg.data[2] & 32 else False
            if msg.data[2] & 64:
                self.blockRasp.state_VE4_open = False
            if msg.data[2] & 128:
                self.blockRasp.state_VE4_close = False
            self.blockRasp.state_chmb_open = True if msg.data[2] & 15 == 15 else False
        elif msg.data[0] == self.data_mes_rasp["current_and_speed"]:
            # self.blockRasp.seted_throttling = struct.unpack("<H", msg.data[2:4])[0]
            self.blockRasp.seted_cur_heat = struct.unpack("<H", msg.data[4:6])[0]
            self.blockRasp.seted_rot_speed = struct.unpack("<H", msg.data[6:8])[0]
        elif msg.data[0] == self.data_mes_rasp["mes_current_and_speed"]:
            self.blockRasp.mes_current = struct.unpack("<H", msg.data[4:6])[0]
            self.blockRasp.mes_speed = struct.unpack("<H", msg.data[6:8])[0]
            self.blockRasp.mes_temperature = struct.unpack("<H", msg.data[2:4])[0]

    def blockRasp_events(self, msg):
        if msg.data[0] == 0x01:
            if msg.data[2] & 240 == 0:
                if msg.data[2] & 15 == 1:
                    self.blockRasp.state_NF = True
                elif msg.data[2] & 15 == 2:
                    self.blockRasp.state_NF = False
                elif msg.data[2] & 15 == 3:
                    self.blockRasp.state_NT = True
                elif msg.data[2] & 15 == 4:
                    self.blockRasp.state_NT = False
                elif msg.data[2] & 15 == 5:
                    self.blockRasp.state_comand_open_VE4 = True
                elif msg.data[2] & 15 == 6:
                    self.blockRasp.state_comand_close_VE4 = True
                elif msg.data[2] & 15 == 8:
                    self.blockRasp.back_door_close = True
                elif msg.data[2] & 15 == 9:
                    self.blockRasp.back_door_close = False
                elif msg.data[2] & 15 == 10:
                    self.blockRasp.phase_electric = False
                elif msg.data[2] & 15 == 11:
                    self.blockRasp.phase_electric = True
                elif msg.data[2] & 15 == 12:
                    self.blockRasp.turbine_break = True
                elif msg.data[2] & 15 == 13:
                    self.blockRasp.turbine_break = False
                elif msg.data[2] & 15 == 14:
                    self.blockRasp.state_chmb_open = False
                elif msg.data[2] & 15 == 15:
                    self.blockRasp.state_chmb_open = True
            elif msg.data[2] & 240 == 16:
                if msg.data[2] & 15 == 0:
                    self.blockRasp.state_comand_close_VE4 = False
                    self.blockRasp.state_comand_open_VE4 = False
                # elif msg.data[2] & 15 == 1:
                # self.blockRasp.VE4_Error_time = True
                elif msg.data[2] & 15 == 5:
                    self.blockRasp.state_VE4_open = True
                    self.blockRasp.state_comand_open_VE4 = False
                elif msg.data[2] & 15 == 7:
                    self.blockRasp.state_VE4_close = True
                    self.blockRasp.state_comand_close_VE4 = False
                elif msg.data[2] & 15 == 6:
                    self.blockRasp.state_VE4_open = False
                elif msg.data[2] & 15 == 8:
                    self.blockRasp.state_VE4_close = False
            elif msg.data[2] & 240 == 32:
                if msg.data[2] & 15 == 2:
                    self.blockRasp.state_heat = True
                elif msg.data[2] & 15 == 3:
                    self.blockRasp.state_heat = False
                elif msg.data[2] & 15 == 4:
                    self.blockRasp.state_rotation = True
                elif msg.data[2] & 15 == 5:
                    self.blockRasp.state_rotation = False
