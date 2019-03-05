#!/usr/bin/env python3
import re 
import os
import json
class pass_man:
    def __init__(self, file):
        self.file = file

    def list_entries(self, data):
        for k in data.keys():
            usr, pwd = k, data[k]
            print(usr + ':' + pwd)
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

        with open(self.file, 'w') as outfile:
            json.dump(data, outfile)
        return

    def check_and_actions(self):
        if os.path.isfile(self.file):
            with open(self.file, 'r') as infile:
                data = json.load(infile)
                print('actions: [i]nsert [g]et [l]ist')
                act = input()
                if act == 'i': 
                    self.insert_pass(data)
                if act == 'g': 
                    self.get_pass(data)
                if act == 'l': 
                    self.list_entries(data)
                return
        else:
            print('no file found')

def start():
    file = 'pass.json'
    man = pass_man(file)
    man.check_and_actions()

if __name__ == '__main__':
    start()

