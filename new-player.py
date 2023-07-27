#!/usr/bin/python
""" show classic telnet star-wars"""
from time import sleep
DELAY_NORMAL = 67/1000


def main(film):
    """ main..."""
    with open(film, 'r', encoding='ascii') as F:
        frame_sleep = int(F.readline())*DELAY_NORMAL
        print(frame_sleep)
        while frame_sleep > 0.0:
            print(frame_sleep)
            scr =  "\033c" + ''.join([ F.readline() for _ in range(13) ])
            print(scr, end='')
            sleep(frame_sleep)
            frame_sleep = int(F.readline())*DELAY_NORMAL

main("star-wars.ascii")
