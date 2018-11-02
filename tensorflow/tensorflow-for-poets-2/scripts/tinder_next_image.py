
import pyautogui
from PIL import Image
import os

im1 = pyautogui.screenshot('/Users/sujeethan/tensorflow/tensorflow-for-poets-2/tf_files/Run_Retrain_Models/test.png')
im1 = im1.crop((1427,167,2177,1302))
im1.save('/Users/sujeethan/tensorflow/tensorflow-for-poets-2/tf_files/Run_Retrain_Models/test.png') 