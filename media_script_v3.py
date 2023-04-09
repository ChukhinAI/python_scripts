from pynput import keyboard
from pynput.keyboard import Controller, KeyCode


double_click_checker = 0

with keyboard.Events() as events:
    for event in events:
        # if event.key == keyboard.Key.esc:
        #    break
        if str(event.key) == str(keyboard.KeyCode.from_vk(0x60)) and double_click_checker == 0:
            Controller().press(KeyCode.from_vk(0xB3))  # Play/Pause - working
            double_click_checker = 1
            # print('_______________________________________________________')
        elif str(event.key) == str(keyboard.KeyCode.from_vk(0x60)) and double_click_checker == 1:
            double_click_checker = 0

        if str(event.key) == str(keyboard.KeyCode.from_vk(0x61)) and double_click_checker == 0:
            Controller().press(KeyCode.from_vk(0xB1))  # Previous Track key - working
            double_click_checker = 1
            # print('_______________________________________________________')
        elif str(event.key) == str(keyboard.KeyCode.from_vk(0x61)) and double_click_checker == 1:
            double_click_checker = 0

        if str(event.key) == str(keyboard.KeyCode.from_vk(0x62)) and double_click_checker == 0:
            Controller().press(KeyCode.from_vk(0xB0))  # Next Track key - working
            double_click_checker = 1
            # print('_______________________________________________________')
        elif str(event.key) == str(keyboard.KeyCode.from_vk(0x62)) and double_click_checker == 1:
            double_click_checker = 0

        if str(event.key) == str(keyboard.KeyCode.from_vk(0x63)) and double_click_checker == 0:
            Controller().press(KeyCode.from_vk(0xAF))  # Volume up key - working
            double_click_checker = 1
            # print('_______________________________________________________')
        elif str(event.key) == str(keyboard.KeyCode.from_vk(0x63)) and double_click_checker == 1:
            double_click_checker = 0

        if str(event.key) == str(keyboard.KeyCode.from_vk(110)) and double_click_checker == 0:
            Controller().press(KeyCode.from_vk(0xAE))  # Volume down Track key - working
            double_click_checker = 1
            # print('_______________________________________________________')
        elif str(event.key) == str(keyboard.KeyCode.from_vk(110)) and double_click_checker == 1:
            double_click_checker = 0
