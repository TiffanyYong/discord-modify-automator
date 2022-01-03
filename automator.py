import pyautogui
import argparse
import time

def get_position():
    print(pyautogui.position())

def delete_channel(num, sx, sy):

    for i in range(num):
        pyautogui.moveTo(sx,sy,0.5)
        pyautogui.click(button='right')
        # move from channel name to delete channel button
        pyautogui.moveRel(66,307)
        pyautogui.click()
        if i == 0:
            pyautogui.click()

        # move to confirm delete channel button
        pyautogui.moveTo(858,523,0.5)
        pyautogui.click()

def role_sync(num, sx, sy):
    cury = sy

    for i in range(num):
        pyautogui.moveTo(sx,cury,0.5)
        pyautogui.click(button='right')

        # move from channel name to edit channel button
        pyautogui.moveRel(77,151,0.5)
        pyautogui.click()
        if i == 0:
            pyautogui.click()

        # move to permissions button
        pyautogui.moveTo(284,153,0.5)
        pyautogui.click()

        # move to sync button
        pyautogui.moveTo(1073,189,0.5)
        pyautogui.click()

        # move to sync permissions button
        pyautogui.moveTo(870,528,0.5)
        pyautogui.click()

        # move to escape
        pyautogui.moveTo(1188,96,0.5)
        pyautogui.click()

        cury = cury + 34

def delete_role(num, sx, sy):
    curx = sx
    cury = sy

    for i in range(num):
        pyautogui.moveTo(curx,cury,1.75)
        pyautogui.click(button='right')

        pyautogui.moveRel(69,95,0.5)
        pyautogui.click()
        if i == 0:
            pyautogui.click()
    
        # move to delete role confirmation
        pyautogui.moveTo(836,524,0.5)
        pyautogui.click()

def create_text(num, sx, sy):

    for i in range(num):
        # move to add channel button
        pyautogui.moveTo(sx,sy,1)
        pyautogui.click()
        if i == 0:
            pyautogui.click()

        # make channel private
        pyautogui.moveTo(912,637,0.3)
        pyautogui.click()

        # add channel name
        pyautogui.click(573,581)
        time.sleep(4)

        # click next and add role
        pyautogui.click(875,751)
        time.sleep(3)
        pyautogui.click(531,415)

        # create channel
        pyautogui.click(868,708)

def create_description(num, sx, sy, dx, dy):
    cury = sy
    descy = dy

    for i in range(num):
        pyautogui.moveTo(sx,cury,0.5)
        pyautogui.click(button='right')

        # click edit channel button
        pyautogui.moveRel(47,155,0.2)
        pyautogui.click()
        if i == 0:
            pyautogui.click()

        # edit channel topic
        pyautogui.moveTo(dx,descy)
        pyautogui.click(clicks=2)

        time.sleep(2)

        pyautogui.moveTo(505,256)
        pyautogui.click(clicks=2)
        time.sleep(2)

        # save changes and exit
        pyautogui.click(1085,852)
        pyautogui.moveTo(1187,104,0.2)
        pyautogui.click()
        
        cury = cury + 34
        descy = descy + 21


def create_voice(num, sx, sy):

    for i in range(num):
        # move to add channel button
        pyautogui.moveTo(sx,sy,1)
        pyautogui.click()
        if i == 0:
            pyautogui.click()

        # make channel private and change to voice
        pyautogui.moveTo(912,637,0.3)
        pyautogui.click()
        pyautogui.click(575,355)

        # add channel name
        pyautogui.click(573,581)
        time.sleep(4)

        # click next and add role
        pyautogui.click(875,751)
        time.sleep(3)
        pyautogui.click(531,415)

        # create channel
        pyautogui.click(868,708)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--xcoord')
    parser.add_argument('-y', '--ycoord')
    parser.add_argument('-x2', '--xcoord2')
    parser.add_argument('-y2', '--ycoord2')
    parser.add_argument('-n', '--num')
    parser.add_argument('-t', '--type')
    args = parser.parse_args()

    type = args.type
    if args.num is not None:
        num = int(args.num)
    if args.xcoord is not None:
        startx = int(args.xcoord)
    if args.xcoord2 is not None:
        extrax = int(args.xcoord2)
    if args.ycoord is not None:
        starty = int(args.ycoord)
    if args.ycoord2 is not None:
        extray = int(args.ycoord2)

    if type == 'pos':
        get_position()
    if type == 'delete':
        delete_channel(num, startx, starty)
    if type == 'role_sync':
        role_sync(num, startx, starty)
    if type == 'deleterole':
        delete_role(num, startx, starty)
    if type == 'text':
        create_text(num, startx, starty)
    if type == 'desc':
        create_description(num, startx, starty, extrax, extray)
    if type == 'voice':
        create_voice(num, startx, starty)
    

if __name__ == '__main__':
    main()