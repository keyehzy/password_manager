import re 
import os
import json

class actions:
    def __init__(self, file):
        self.file = file

    def list_entries(self, data):
        for k in data.keys():
            usr, pwd = k, data[k]
            print(usr + ':' + pwd)
        return

    def del_entry(self, data):
       #print('insert master pass')
        print('which usr')
        usr = input()
        if usr in data:
            data.pop(usr)
        else:
            print('no key found')
        self.json_write(data)
        return

    def get_pass(self, data):
        print('get pwd for usr:')
        usr = input()
        if usr in data:
            print(usr + ':' + data[usr])
        else:
            print('no key found')
        return

    def insert_pass(self, data):
        print('insert usr:pwd') 
        usr, pwd = map(str, input().split(':'))
        if usr in data:
            print('already has key')
        else:
            data[usr] = pwd

        self.json_write(data)
        return
        
    def json_write(self, data):
        with open(self.file, 'w') as outfile:
            json.dump(data, outfile)
        return

    def check_and_actions(self):
        if os.path.isfile(self.file):
            with open(self.file, 'r') as infile:
                data = json.load(infile)
                while True:
                    print('actions: [i]nsert [g]et [l]ist [d]el')
                    act = input()
                    if act == 'i': 
                        self.insert_pass(data)
                    if act == 'g': 
                        self.get_pass(data)
                    if act == 'l': 
                        self.list_entries(data)
                    if act == 'd': 
                        self.del_entry(data)
                    if act == '':
                        break
                return
        else:
            print('no file found')
