from time import sleep
# import datetime

# import machine
from machine import RTC, Pin, PWM

rtc = RTC()
rtc.datetime((2000,1,1,1,1,1,0,0))

while True:
    # Get the current time
    #     t = datetime.datetime.now()
    t=rtc.datetime()
    # Convert the hours, minutes, and seconds to binary (BCD)

    print("hours------" + str(t.hour))
    hours_as_digits = list(map(int, list(str(t.hour).zfill(2))))
    
    hours_10x_bin = bin(int(hours_as_digits[0]))[2:]
    hours_10x_bin = hours_10x_bin.zfill(2)
    led_h_10x_2 = list(map(int, list(hours_10x_bin)))[0]
    led_h_10x_1 = list(map(int, list(hours_10x_bin)))[1]
    print("led_h_10x_2 " + str(led_h_10x_2))
    print("led_h_10x_1 " + str(led_h_10x_1))

    hours_bin = bin(int(hours_as_digits[1]))[2:]
    hours_bin = hours_bin.zfill(4)
    led_h_8 = list(map(int, list(hours_bin)))[0]
    led_h_4 = list(map(int, list(hours_bin)))[1]
    led_h_2 = list(map(int, list(hours_bin)))[2]
    led_h_1 = list(map(int, list(hours_bin)))[3]
    print("led_h_8 " + str(led_h_8))
    print("led_h_4 " + str(led_h_4))
    print("led_h_2 " + str(led_h_2))
    print("led_h_1 " + str(led_h_1))


    print("minutes------" + str(t.minute))
    minutes_as_digits = list(map(int, list(str(t.minute).zfill(2))))
    
    minutes_10x_bin = bin(int(minutes_as_digits[0]))[2:]
    minutes_10x_bin = minutes_10x_bin.zfill(3)
    led_m_10x_4 = list(map(int, list(minutes_10x_bin)))[0]
    led_m_10x_2 = list(map(int, list(minutes_10x_bin)))[1]
    led_m_10x_1 = list(map(int, list(minutes_10x_bin)))[2]
    print("led_m_10x_4 " + str(led_m_10x_4))
    print("led_m_10x_2 " + str(led_m_10x_2))
    print("led_m_10x_1 " + str(led_m_10x_1))

    minutes_bin = bin(int(minutes_as_digits[1]))[2:]
    minutes_bin = minutes_bin.zfill(4)
    led_m_8 = list(map(int, list(minutes_bin)))[0]
    led_m_4 = list(map(int, list(minutes_bin)))[1]
    led_m_2 = list(map(int, list(minutes_bin)))[2]
    led_m_1 = list(map(int, list(minutes_bin)))[3]
    print("led_m_8 " + str(led_m_8))
    print("led_m_4 " + str(led_m_4))
    print("led_m_2 " + str(led_m_2))
    print("led_m_1 " + str(led_m_1))

    print("seconds------" + str(t.second))
    seconds_as_digits = list(map(int, list(str(t.second).zfill(2))))

    seconds_10x_bin = bin(int(seconds_as_digits[0]))[2:]
    seconds_10x_bin = seconds_10x_bin.zfill(3)
    led_s_10x_4 = list(map(int, list(seconds_10x_bin)))[0]
    led_s_10x_2 = list(map(int, list(seconds_10x_bin)))[1]
    led_s_10x_1 = list(map(int, list(seconds_10x_bin)))[2]
    print("led_s_10x_4 " + str(led_s_10x_4))
    print("led_s_10x_2 " + str(led_s_10x_2))
    print("led_s_10x_1 " + str(led_s_10x_1))

    seconds_bin = bin(int(seconds_as_digits[1]))[2:]
    seconds_bin = seconds_bin.zfill(4)
    led_s_8 = list(map(int, list(seconds_bin)))[0]
    led_s_4 = list(map(int, list(seconds_bin)))[1]
    led_s_2 = list(map(int, list(seconds_bin)))[2]
    led_s_1 = list(map(int, list(seconds_bin)))[3]
    print("led_s_8 " + str(led_s_8))
    print("led_s_4 " + str(led_s_4))
    print("led_s_2 " + str(led_s_2))
    print("led_s_1 " + str(led_s_1))

    # break
    # Sleep for one second
    sleep(1)
