"""
quick example for ola dmx data receiving and osc sending.

based on
https://www.openlighting.org/ola/developer-documentation/python-api/#Receiving_DMX
and
https://pypi.python.org/pypi/python-osc#simple-client
http://stackoverflow.com/a/22152877/574981
"""

# https://docs.python.org/2.7/howto/pyporting.html#division
from __future__ import division

import sys

from ola.ClientWrapper import ClientWrapper

# python-osc
# from pythonosc import osc_message_builder
# from pythonosc import udp_client

# pyOSC
import OSC

# config
osc_target_ip = "192.168.178.55"
osc_target_port = 9000
ola_input_universe = 1


# dmx input handling
def NewData(data):
    global osc_client
    # print("data: {}".format(data))
    value = data[0] / 255
    # print("value: {}".format(value))
    # python-osc
    # osc_client.send_message("/filter", value)
    # pyOSC
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/1/fader1")
    oscmsg.append(value)
    osc_client.send(oscmsg)


##########################################
if __name__ == '__main__':

    print(42*'*')
    print('Python Version: ' + sys.version)
    print(42*'*')
    print(__doc__)
    print(42*'*')

    # init osc client (client=sender)
    global osc_client
    # python-osc
    # osc_client = udp_client.SimpleUDPClient(osc_target_ip, osc_target_port)
    # pyOSC
    osc_client = OSC.OSCClient()
    osc_client.connect((osc_target_ip, osc_target_port))

    # init ola client
    ola_wrapper = ClientWrapper()
    ola_client = ola_wrapper.Client()
    ola_client.RegisterUniverse(
        ola_input_universe,
        ola_client.REGISTER,
        NewData
    )

    print("running...")
    # run ola client
    ola_wrapper.Run()
