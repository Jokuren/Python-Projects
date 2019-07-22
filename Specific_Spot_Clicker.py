#Clicks on a spot determined by you.

import pyautogui, sys

Web_ID = False
Web_Code = False
Gen_Key = False
MID = False
MKEY = False
Activate = False
Error_OK = False
Win_Activatin = False

Test_Times = 0
Max_Count = 500

#For getting the initial position of the mouse. 
#try:
#    while True:
#        x, y = pyautogui.position()
#        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#        print(positionStr, end='')
#        print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#    print('\n')

while Win_Activatin == False:
    # Generate New ID and Key
    if(Gen_Key == False):
        pyautogui.click(x = 276, y = 819)
        Gen_Key = True
   # Copy User ID
    elif (Gen_Key == True and Web_ID == False):
        pyautogui.moveTo(x = 162, y = 767, duration = 0.5)
        pyautogui.doubleClick(x = 162, y = 767)
        pyautogui.hotkey('ctrl', 'c')
        Web_ID = True
        Gen_Key = True
    # Paste User ID
    elif (Gen_Key == True and Web_ID == True and MID == False):
        pyautogui.doubleClick(x = 1387, y = 565)
        pyautogui.hotkey('ctrl', 'v')
        Web_ID = True
        Gen_Key = True
        MID = True
    # Copy Key
    elif (Gen_Key == True and Web_ID == True and MID == True and Web_Code == False):
        pyautogui.moveTo(85, 786)
        pyautogui.drag(250, 0, 0.5, button='left')
        pyautogui.hotkey('ctrl', 'c')
        Web_ID = True
        Gen_Key = True
        MID = True
        Web_Code = True
    # Paste Key
    elif (Gen_Key == True and Web_ID == True and MID == True and Web_Code == True and MKEY == False):
        pyautogui.click(x = 1420, y = 638, clicks=3)
        pyautogui.hotkey('ctrl', 'v')
        Web_ID = True
        Gen_Key = True
        MID = True
        Web_Code = True
        MKEY = True
    # Try Activation
    elif (Gen_Key == True and Web_ID == True and MID == True and Web_Code == True and MKEY == True and Activate == False):
        pyautogui.click(x = 1497, y = 811)
        Web_ID = True
        Gen_Key = True
        MID = True
        Web_Code = True
        MKEY = True
        Activate = True
    # Click OK on Activation Error
    elif (Gen_Key == True and Web_ID == True and MID == True and Web_Code == True and MKEY == True and Activate == True and Error_OK == False):
        pyautogui.moveTo(x = 1160, y = 581, duration = 1)
        pyautogui.click()
        Web_ID = True
        Gen_Key = True
        MID = True
        Web_Code = True
        MKEY = True
        Activate = True
        Error_OK = True
        # End Program
    elif(Gen_Key == True and Web_ID == True and MID == True and Web_Code == True and MKEY == True and Activate == True and Error_OK == True and Test_Times != Max_Count):
        Web_ID = False
        Gen_Key = False
        MID = False
        Web_Code = False
        MKEY = False
        Activate = False
        Error_OK = False
        Test_Times += 1
    elif(Gen_Key == True and Web_ID == True and MID == True and Web_Code == True and MKEY == True and Activate == True and Error_OK == True and Test_Times == Max_Count):
        Win_Activatin = True