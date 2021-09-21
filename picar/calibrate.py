from .utils import reset_mcu,delay
from .picarx import Picarx
from pynput import keyboard

def calibrate_motors(px):
    cal = [0,0]
    print("Let's calibrate the left motor.")
    print("Observe the direction of the left wheel.")
    delay(500)
    px.set_motor_speed(1,50)
    delay(3000)
    px.stop()
    ans = input('Did the left wheel spin in the forward direction?(y/n): ')
    if ans.lower() in ['n','no']:
        cal[0] = 1
    print("Let's calibrate the right motor.")
    print("Observe the direction of the right wheel.")
    delay(500)
    px.set_motor_speed(2,-50)
    delay(3000)
    px.stop()
    ans = input('Did the right wheel spin in the forward direction?(y/n): ')
    if ans.lower() in ['n','no']:
        cal[1] = 1
    print(cal)
    px.motor_direction_calibration(1,cal[0])
    px.motor_direction_calibration(2,cal[1])

def calibrate_camera_tilt(px):
    cal_angle = 0
    print("Let's calibrate the camera tilt angle.")
    px.tilt_camera(cal_angle)
    print("The camera tilt angle has been set to 0 degrees")
    print("Use the up and down arrow to adjust the camera tilt.")
    print("Press the SHIFT key to end camera tilt calibration.")
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.up:
                cal_angle += 1
                px.tilt_camera(cal_angle)
            elif event.key == keyboard.Key.down:
                cal_angle -= 1
                px.tilt_camera(cal_angle)
            elif event.key == keyboard.Key.shift:
                break
    px.camera_servo1_angle_calibration(-cal_angle)
    
def calibrate_camera_pan(px):
    cal_angle = 0
    print("Let's calibrate the camera pan angle.")
    px.pan_camera(cal_angle)
    print("The camera tilt angle has been set to 0 degrees")
    print("Use the left and right arrow to adjust the camera pan.")
    print("Press the SHIFT key to end camera pan calibration.")
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.right:
                cal_angle += 1
                px.pan_camera(cal_angle)
            elif event.key == keyboard.Key.left:
                cal_angle -= 1
                px.pan_camera(cal_angle)
            elif event.key == keyboard.Key.shift:
                break;
    px.camera_servo1_angle_calibration(-cal_angle)

def calibrate_turn_servo(px):
    cal_angle = 0
    print("Let's calibrate the front wheel direction.")
    px.turn_wheels(cal_angle)
    print("The front wheels angle has been set to 0 degrees")
    print("Use the left and right arrow to adjust the front wheels.")
    print("Press the SHIFT key to end.")
    is_done = False
    while not is_done:
        with keyboard.Events() as events:
            for event in events:
                if event.key == keyboard.Key.right:
                    cal_angle += 1
                    px.turn_wheels(cal_angle)
                elif event.key == keyboard.Key.left:
                    cal_angle -= 1
                    px.turn_wheels(cal_angle)
                elif event.key == keyboard.Key.shift:
                    break
        px.forward(50)
        delay(2000)
        px.stop()
        ans = input("Did the car travel in a straight line? ")
        if ans.lower() in ['y','yes']:
            is_done = True
            px.dir_servo_angle_calibration(cal_angle)
        
    
def calibrate():
    reset_mcu()
    px = Picarx()
    
    calibrate_motors(px)
    calibrate_camera_tilt(px)
    calibrate_camera_pan(px)
    calibrate_turn_servo(px)
