#!/usr/bin/env python3
import manager

# TODO: encrypt entry keys and decrypt only when releasing to keyboard
def start():
    file = 'pass.json'
    key_file = 'key.json'
    man = manager.actions(file, key_file)
    man.check_and_actions()

if __name__ == '__main__':
    start()

