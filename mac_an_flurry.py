import subprocess
import optparse

opt_object = optparse.OptionParser()
opt_object.add_option("-i", "--interface", dest="interface", help="interface to change")
opt_object.add_option("-m", "--mac", dest="mac_address", help="new mac adress")

(user_inputs, args) = opt_object.parse_args()

user_interface = user_inputs.interface
user_mac_address = user_inputs.mac_address


subprocess.call(["ifconfig", user_interface, "down"])
subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
subprocess.call(["ifconfig", user_interface, "up"])
