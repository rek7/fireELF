import glob
import importlib
import sys

from lib.misc import print_info



def load_payload(path):
    try:
        return importlib.import_module(path)
    except Exception as e:
        return False

def gather_payloads(payload_dir):
    payload_to_name = {}
    for filepath in glob.iglob("{}*.py".format(payload_dir)):
        payload_import_name = filepath[:-3].replace("/", ".")
        payload = load_payload(payload_import_name)
        if payload:
            try:
                name = payload.desc["name"].lower()
                payload_to_name[name] = payload
                print_info("Loaded Payload: '{}'".format(name), "!")
                continue
            except Exception as e:
                print_info("Error Loading Payload", "-")
        print_info("Unable to Load: {}".format(payload_import_name), "-")
    return payload_to_name

def generate(executable, is_url, payload_dir, payload_to_use):
    payloads = gather_payloads(payload_dir)
    if payloads:
        if payload_to_use:
            if payload_to_use in payloads:
                print_info("Using Payload: '{}'".format(payload_to_use), "!")
                return payloads[payload_to_use].main(is_url, executable)
            else:
                print_info("not found", "-")
        else:
            print("-"*20)
            for name, payload in payloads.items():
                info = payload.desc
                print("Payload Name: '{}'".format(name))
                print("\tPayload Description: '{}'".format(info["description"]))
                print("\tCompatible Architectures: '{}'".format(info["archs"]))
                print("\tRequired Python Version on Target: {}".format(info["python_vers"]))
                print("-"*20)
            while True:
                choice = input("Choose Payload (Q to Quit)>> ").lower()
                if choice == "q":
                    break
                else:
                    if choice in payloads:
                        print_info("Using Payload: '{}'".format(choice), "!")
                        return payloads[choice].main(is_url, executable)
                    else:
                        print_info("Payload Not Found", "-")
    else:
        print_info("No Useable Payloads", "-")