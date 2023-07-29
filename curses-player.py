#!/usr/bin/python
""" show classic telnet star-wars"""
from time import sleep
import curses


DELAY_NORMAL = 67 # ms/1000



def play(win,debug, film):
    """ main..."""
    Frame=0

    with open(film, 'r', encoding='ascii') as F:
        f_lines=F.readlines()
    MaxFrames=int(len(f_lines)/14)

    while Frame<MaxFrames:
        f_pos=Frame*14
        fs_int = int(f_lines[f_pos])
        frame_sleep = fs_int*DELAY_NORMAL
        Frame+=1
        f_pos+=1
        win.erase()
        for lin in range(13):
            win.addstr(lin, 0, f_lines[f_pos+lin] )
        win.refresh()
        key=debug.getch()
        if key != -1:
            frame_sleep=0
            curses.ungetch(key)
            key=debug.getkey()
            if key=='q':
                return
            if key=='KEY_RIGHT':
                Frame+=10
                if Frame>MaxFrames:
                    Frame=MaxFrames
            if key=='KEY_LEFT':
                Frame-=10
                if Frame<0:
                    Frame=0
            if key=='KEY_UP':
                Frame+=100
                if Frame>MaxFrames:
                    Frame=MaxFrames
            if key=='KEY_DOWN':
                Frame-=100
                if Frame<0:
                    Frame=0
        debug.erase()
        debug.addstr(0,0, f'> Frame: {Frame:3d}/{MaxFrames}, delay: {fs_int} key: {key}  <')
        debug.refresh()
        curses.napms(frame_sleep)

        #print(scr, end='')

def main(stdscr):
# curses.init_color(color_number, r, g, b)¶
    curses.curs_set(0) # hide cur
    winb  = curses.newwin(16, 80, 0, 0)
    win   = curses.newwin(14, 77, 1, 1)
    debugb= curses.newwin(4, 62, 18, 10)
    debug = curses.newwin(2, 60, 19, 11)
    winb.border()
    winb.refresh() # use box?
    debugb.border()
    debugb.refresh() # use box?
    curses.set_escdelay(10)

    debug.nodelay(True)
    debug.keypad(True)


    Frame=1
    fs_int=100
    key=1
    while False:
        Frame+=1
        debug.addstr(0,0, f'> Frame: {Frame:3d}, delay: {fs_int} key: {key}  <')
        debug.refresh()
        key=debug.getch()
        if key != -1:
            curses.ungetch(key)
            key=debug.getkey()
            if key=='q':
                return
            if key=='KEY_RIGHT':
                fs_int-=10
            if key=='KEY_LEFT':
                fs_int+=10
        curses.napms(fs_int)

    play(win, debug, "star-wars.ascii")


""" start here """
curses.wrapper(main)


