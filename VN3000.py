import can
import json
import time
from blockUpr import BlockUPR
from blockRasp import BlockRasp
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

        try:
            self.bus = can.interface.Bus(bustype="systec", channel="0", bitrate=1000000)
        except can.CanError:
            print("Hardware or CAN interface initialization failed.")
            input()

        self.blk_upr = BlockUPR(self.bus)
        self.blk_rasp = BlockRasp(self.bus)
        self.parser = Parser(self.blk_upr, self.blk_rasp)

    def star_work(self):
        """Getting started, the foundation of the program"""
        print("ВН-3000")

        self.blk_upr.get_states()
        self.blk_upr.get_measurements()
        self.blk_rasp.get_states()
        self.blk_rasp.get_measurements()

        self.reader_m4()

        time.sleep(1)
        k, m = self.blk_upr.return_states_mes()
        l, f = self.blk_rasp.return_states_mes()
        print(k)
        print(m)
        print(l)
        print(f)

        self.bus.shutdown()

    def reader_m1(self):
        """Method 1 for read recv msg from bus
        """

        print("Read from Bus: M1")

        try:
            while True:
                msg = self.bus.recv(1)
                if msg is not None:
                    print(msg)

        except KeyboardInterrupt:
            pass  # exit normally (tap ctrl+c)

    def reader_m2(self):
        """Method 2 for read recv msg from bus
        """

        print("Read from Bus: M2")

        msg = self.bus.recv(0.5)
        if msg is not None:
            print(msg.data)

    def reader_m3(self):
        """Method 3 for read recv msg from bus, может понадобиться создание декоратора/ или нет
        """

        print("Read from Bus: M3")

        try:
            for msg in self.bus:
                print(msg.data)
                # pass
        except KeyboardInterrupt:  # надо найти прерывание по времени!
            pass

    def reader_m4(self):
        """Method 4
        """

        print("Read from Bus: M4")

        # reader = can.BufferedReader()
        noti = can.Notifier(self.bus, [self.parser.read_input, can.Printer()])
        # msg = reader.get_message()
        # print(msg)
