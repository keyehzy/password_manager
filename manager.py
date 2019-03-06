import re 
import os
import json
from secure import secure

class actions:
    def __init__(self, file, key_file):
        self.file = file
        self.secure = secure
        with open(key_file, 'r') as infile:
            self.key = json.load(infile)['key']

    def list_entries(self, data):
        return {print(k + ':' + data[k]) for k in data.keys()}

    def del_entry(self, data):
        if(self.key):
            print('which usr')
            usr = secure.encode(self.key, input())
            if usr in data:
                data.pop(usr)
                self.json_write(data)
            else:
                print('no key found')
        return

    def get_pass(self, data):
        if(self.key):
            print('get pwd for usr:')
            usr = secure.encode(self.key, input())
            if usr in data:
                print(secure.decode(self.key, usr) + ':' + secure.decode(self.key, data[usr]))
            else:
                print('no key found')
        return

    def insert_pass(self, data):
        if(self.key):
            print('insert usr:pwd') 
            usr, pwd = map(str, input().split(':'))
            if usr in data:
                print('already has key')
            else:
                data[secure.encode(self.key, usr)] = secure.encode(self.key, pwd)
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
        else:
            print('no file found')
        return
