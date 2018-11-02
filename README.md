# Swiper
Machine Learning Tinder Bot

<img src="https://camo.githubusercontent.com/87706dea90dd1843973b211086a9865efc3698c6/687474703a2f2f692e696d6775722e636f6d2f45684c416737742e706e67" height="300px" width="400px"> <img src="https://1000logos.net/wp-content/uploads/2018/07/tinder-logo.png" width = "390px" height ="250px">

Uses a Tensorflow Model (tensorflow-for-poets-2) to classify images as left or right swipes

Python (pyautogui) handles the computer interactions for the mouse movement and clicks

A shell script loops and handles the python programs


To run, find the Run_Retrain_Models folder, in the terminal run the shell script to Retrain the model or to Run the model. Note that the script will work on the image currently in the same folder called test.png. 

To adjust the pixels selected on the script look at the folder "scripts" and the python files: "label_image_for_tinder.py" and "tinder_next_image.py"