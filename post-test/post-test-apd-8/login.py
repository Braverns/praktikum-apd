from time import sleep
import os
from data import *

def userpass(x):
    uns = input(f'|{x }Username anda: ').lower()
    print('\033[F', end='')   
    print(f'|{x }Username anda: {uns:<{90 - len(x)}}|')
    pws = input(f'|{x }Password anda: ').lower()
    print('\033[F', end='')   
    print(f'|{x }Password anda: {pws:<{90 - len(x)}}|')
    print(tengah)
    sleep(1)
    return uns, pws

def adminpass():
    un = input('|Username anda: ').strip().lower().replace(' ', '')
    print('\033[F', end='')   
    print(f'|Username anda: {un:<{90}}|')
    pw = input('|Password anda: ').strip().lower().replace(' ', '')
    print('\033[F', end='')   
    print(f'|Password anda: {pw:<{90}}|')
    print(tengah)
    sleep(1)
    return un, pw