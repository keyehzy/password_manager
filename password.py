#!/usr/bin/env python3
import pass_man

# TODO: encrypt entry keys and decrypt only when releasing to keyboard
def start():
    file = 'pass.json'
    man = pass_man.actions(file)
    man.check_and_actions()

if __name__ == '__main__':
    start()

