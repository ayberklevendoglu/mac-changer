import subprocess
import optparse
import re


def get_user_input():
    opt_object = optparse.OptionParser()
    opt_object.add_option("-i", "--interface", dest="interface", help="interface to change")
    opt_object.add_option("-m", "--mac", dest="mac_address", help="new mac adress")

    return opt_object.parse_args()


def change_mac_adress(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def control_new_mac(user_interface):
    ifconfig = subprocess.check_output(["ifconfig", user_interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig.decode("utf-8"))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


(user_input, args) = get_user_input()
change_mac_adress(user_input.interface, user_input.mac_address)
final_mac = control_new_mac(user_input.interface)

if final_mac == user_input.mac_address:
    print("You have succesfully changed your MAC address.")
    print(f"New MAC address is{final_mac}")
else:
    print("Failed to change your MAC address.")
