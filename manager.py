import re
import os
import json
from secure import secure

# TODO insert context entries, that is specify where you want to put the passwords
class actions:
    def __init__(self, file, key_file):
        self.file = file
        self.secure = secure
        with open(key_file, 'r') as infile:
            self.key = json.load(infile)['key']
        return

    def list_context(self, data):
        for entry in data:
            print(entry)
        return

    def list_entries(self, data):
        print('context:')
        ct = input()
        for entry in data[ct].keys():
            print(secure.decode(self.key, entry) + ':' + secure.decode(self.key, data[ct][entry]))
        return

    def del_entry(self, data):
        if(self.key):
            print('context:')
            ct = input()
            print('which usr')
            usr = secure.encode(self.key, input())
            if ct in data:
                if usr in data[ct]:
                    data[ct].pop(usr)
                    self.json_write(data)
                else:
                    print('no key found')
            else:
                print('no context found')
        return

    def get_pass(self, data):
        if(self.key):
            print('context:')
            ct = input()
            print('get pwd for usr:')
            usr = secure.encode(self.key, input())
            if ct in data:
                if usr in data[ct]:
                    dec_usr, dec_pwd = secure.decode(self.key, usr), secure.decode(self.key, data[ct][usr])
                    print(dec_usr + ':' + dec_pwd)
                    os.system("echo %s | clip" % dec_pwd)
                else:
                    print('no key found')
            else:
                print('no context found')
        return

    def insert_pass(self, data):
        if(self.key):
            print('context:')
            ct = input()
            print('insert usr:pwd')
            usr, pwd = map(str, input().split(':'))
            usr, pwd = secure.encode(self.key, usr), secure.encode(self.key, pwd)
            if ct in data:
                if usr in data[ct]:
                    print('already has key')
                else:
                    new = data[ct]
                    new[usr] = pwd
                    data[ct] = new
                    self.json_write(data)
            else:
                new = {}
                new[usr] = pwd
                data[ct] = new
                self.json_write(data)
        return

    def json_write(self, data):
        with open(self.file, 'w') as outfile:
            json.dump(data, outfile, indent=4)
        return

    def check_and_actions(self):
        if os.path.isfile(self.file):
            with open(self.file, 'r') as infile:
                data = json.load(infile)
            while True:
                print('actions: [i]nsert [g]et [l]ist [d]el [c]ontexts')
                act = input()
                if act == 'i':
                    self.insert_pass(data)
                if act == 'g':
                    self.get_pass(data)
                if act == 'l':
                    self.list_entries(data)
                if act == 'd':
                    self.del_entry(data)
                if act == 'c':
                    self.list_context(data)
                if act == '':
                    break
        else:
            print('no file found')
        return
