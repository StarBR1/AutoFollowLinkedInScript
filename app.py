from screen_Manager import screenManager
import os
import time
import random
import keyboard

imgPath1 = 'img.png'
imgPath2 = 'img2.png'
def run():
    followedCounter = 0

    try:
        if not os.path.exists(imgPath1 or imgPath2 ):
            print(f'{imgPath1 or imgPath2} not found')
            return

        while True:
            if screenManager.checkActiveBar(app_title_name="linkedin"):
                coordinates = screenManager.getMatchedImages(imageToSearch=imgPath1 or imgPath2)

                for coordinate in coordinates:
                    followedCounter += 1
                    screenManager.clickOnScreen(coordinateToClick=coordinate)
                    time.sleep(2)
                    print(f'click coordinates {coordinate}')
                
                screenManager.scrollDown(screenValue=-400)
                time.sleep(2)

            if keyboard.is_pressed('esc'):
                print(f'ESC pressed. Total Followed Counter: {followedCounter}')
                break

    except Exception as e:
        print(f'Error: {e}')

run()
