import datetime
import socket
import re
from lib.settings import *



def miniaturize_payload(payload):
    return payload.replace("\n", ";")

def paste_site_upload(payload):
    paste_site = "termbin.com"
    try:
        s0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s0.connect((paste_site, 9999))
        s0.sendall(payload.encode("utf-8"))
        print_info("Successfully Uploaded to: {}".format(paste_site), "+")
        resp = s0.recv(1024)
        return resp.decode("ascii").replace('\x00','').strip()
    except:
        print_info("Error Uploading to Paste Site: {} Is it Down?".format(paste_site), "-")

def print_info(info, reason):
    color = {"-" : RED, "+" : GREEN, "!" : YELLOW}
    print("{}[{}] [{}] {}".format(color[reason], 
        datetime.datetime.now().strftime('%X'), reason, info))