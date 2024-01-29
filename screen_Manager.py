import pyautogui
import logging
import cv2
import win32gui

class screenManager:
    @staticmethod
    def checkActiveBar(app_title_name: str):
        activeBar = win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower()
        return app_title_name in activeBar
        
    @staticmethod
    def clickOnScreen(coordinateToClick: int):
        pyautogui.click(coordinateToClick)
        
    @staticmethod
    def scrollDown(screenValue: int):
        pyautogui.scroll(screenValue)
        
    @staticmethod
    def getMatchedImages(imageToSearch: str):
        try:
            return pyautogui.locateAllOnScreen(image=imageToSearch, grayscale=True, confidence=0.8)
            
        except Exception as ex:
            logging.info(f'Img not found. Err{ex}')