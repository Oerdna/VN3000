import can


class BlockDC:
    """this class implements interaction with the control unit.
    """

    """id - the frame identifier used for arbitration on the bus.
    """
    id_blockUPR_command = 0x101E0010

    def __init__(self, bus: object):
        """Variables are responsible for storing the pressure value, I and U.

        Args:
            bus (object): [USB-CAN object]
        """
