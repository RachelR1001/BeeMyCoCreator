from flask import Flask, request, jsonify
from flask_cors import CORS

import takePhoto
import musicSetup as ms
import os
import sys
import time

# 导入 CORS
app = Flask(__name__)
CORS(app)  # 启用 CORS
testlist = [45, 35, 25, 57, 45, 38, 22, 33, 35, 50, 52, 30, 28, 24, 44, 46]

"""
Start Robotic Arm
"""

from xarm.wrapper import XArmAPI

# Connect to XARM.
ip = '192.168.1.215' # Robotic Arm IP
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)
arm.reset(wait=True)

music_Start = False

line_1_origin = (608.7, 230)
line_2_origin = (535.3, 263.6)
line_3_origin = (463.5, 224.4)
lines_origin = [line_1_origin, line_2_origin, line_3_origin]

receiving_melody = False
synchronized: bool = False  # 全局变量，改成

long_melody_sequence = []
is_playing_music = False

def end_arm():
    arm.reset(wait=True)
    arm.disconnect()
    # 清除屏幕
    os.system('cls')


# To be used in receive melody
def armPlayMusic(melody):
    global is_playing_music
    is_playing_music = True
    # if synchronized:
    # arm.set_position(X, Y - position * 80, z=130, roll=-180, pitch=0, yaw=0, speed=1000, wait=True)
    length = len(melody)
    i = 0
    for m in melody:
        # X, Y = 170, 320
        line_num, position = ms.get_target_position(m)
        print(line_num, position)
        X, Y = lines_origin[line_num - 1]
        arm.set_position(X, Y - position * 80, z=130, roll=-180, pitch=0, yaw=0, speed=1000, wait=True)
        arm.set_position(X, Y - position * 80, z=106.7, roll=-180, pitch=0, yaw=0, speed=1000, wait=True)
        arm.set_position(X, Y - position * 80, z=130, roll=-180, pitch=0, yaw=0, speed=1000, wait=True)
        i = 1 + i
    if not synchronized:
        arm.reset(wait=True)
    is_playing_music = False


# 106.7
# x- 457.4, y- 137.3
# 63
# 74.3距离
def parse_data(melo):
    list1 = []
    for mm in melo:
        list1.append(mm['pitch'])
    return list1


@app.route('/receive_melody', methods=['POST'])
def receive_melody():
    # For Synchronized Music Playing:
    global synchronized
    global long_melody_sequence
    global is_playing_music

    # Set Arm to original
    # arm.reset(wait=True)

    # Parse Data
    data = request.json
    m_data = data['melody']

    # Check if Synchronized
    if "notes" in m_data:
        m_data = m_data["notes"]
        synchronized = True
    print("Received melody data:", m_data)

    melody_sequence = parse_data(m_data)

    if music_Start:
        print("up m start")
        if synchronized:
            if not is_playing_music:
                long_melody_sequence = melody_sequence
                armPlayMusic(long_melody_sequence)
                print("Received melody long-new:", long_melody_sequence)
            else:
                long_melody_sequence.extend(melody_sequence)
                print("Received melody long-append:", long_melody_sequence)

        else:
            armPlayMusic(melody_sequence)
            print("Received melody normal:", melody_sequence)

    synchronized = False
    return jsonify({"status": "success"})


@app.route('/restart_robotarm', methods=['POST'])
def restart_robotarm():
    global arm
    print("switch mode")
    XX = arm.get_position()[1][0]
    YY = arm.get_position()[1][1]
    print(arm.get_position())
    print(XX)
    arm.set_position(XX, YY, z=160, roll=-180, pitch=0, yaw=0, speed=1000,wait=True)
    arm.disconnect()
    os.system('cls')
    time.sleep(2)
    arm = XArmAPI(ip)
    arm.motion_enable(enable=True)
    arm.set_mode(0)
    arm.set_state(state=0)
    time.sleep(2)
    arm.reset(wait=True)
    print("switch mode done")
    return jsonify({"status": "success"})


if __name__ == "__main__":
    # Take Photo.

    arm.set_position(x=210, y=0, z=590, roll=-180, pitch=0, yaw=0, speed=400, wait=True)

    #lines_origin2 = takePhoto.take_img()

    music_Start = True

    # melody_sequence = testlist
    # if music_Start:
    #   arm.reset(wait=True)
    #  armPlayMusic(melody_sequence)

    # end_arm()

    app.run(host='0.0.0.0', port=1234)
    music_Start = False

# 107.6
