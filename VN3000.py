import can
import json
import sys
from blockUpr import BlockUPR
from blockRasp import BlockRasp


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

        try:
            self.bus = can.interface.Bus(bustype="systec", channel="0", bitrate=1000000)
        except can.CanError:
            print("Hardware or CAN interface initialization failed.")
            input()

        self.blk_upr = BlockUPR(self.bus)
        self.blk_rasp = BlockRasp(self.bus)

    def star_work(self):
        """Getting started, the foundation of the program"""
        print("ВН-3000")

        self.blk_upr.get_states()
        self.blk_rasp.get_states()

        self.blk_upr.set_valve(VE='VE3', state=True)
        self.blk_rasp.set_pump(pump='NL', state=True)

        
