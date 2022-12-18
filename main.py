from machine import RTC, Pin, PWM
import network
import socket
import time
import struct

# from machine import Pin

NTP_DELTA = 2208988800
host = "217.196.145.42"

led = Pin("LED", Pin.OUT)
pin_h_10x_1 = Pin(0,Pin.OUT)
pin_h_10x_2 = Pin(1,Pin.OUT)

pin_h_1 = Pin(2,Pin.OUT)
pin_h_2 = Pin(3,Pin.OUT)
pin_h_4 = Pin(4,Pin.OUT)
pin_h_8 = Pin(5,Pin.OUT)

pin_m_10x_1 = Pin(6,Pin.OUT)
pin_m_10x_2 = Pin(7,Pin.OUT)
pin_m_10x_4 = Pin(8,Pin.OUT)

pin_m_1 = Pin(9,Pin.OUT)
pin_m_2 = Pin(10,Pin.OUT)
pin_m_4 = Pin(11,Pin.OUT)
pin_m_8 = Pin(12,Pin.OUT)

pin_s_10x_1 = Pin(13,Pin.OUT)
pin_s_10x_2 = Pin(14,Pin.OUT)
pin_s_10x_4 = Pin(15,Pin.OUT)

pin_s_1 = Pin(16,Pin.OUT)
pin_s_2 = Pin(17,Pin.OUT)
pin_s_4 = Pin(18,Pin.OUT)
pin_s_8 = Pin(19,Pin.OUT)

ssid = 'ssid'
password = 'pw'
rtc = RTC()

def set_time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        msg = None
        res = None
        try:
            s.settimeout(1)
            res = s.sendto(NTP_QUERY, addr)
            msg = s.recv(48)
            # print(msg)
            time.sleep(2)
            if msg == None:
               print("data not received")
            else:
               break
        except OSError as exc:
            if exc.args[0] == 110: # ETIMEDOUT
                print("Error reading NTP server")
            
    # print(msg)
    s.close()
    # try:
    #     s.settimeout(1)
    #     res = s.sendto(NTP_QUERY, addr)
    #     msg = s.recv(48)
    # finally:
    #     s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    t = val - NTP_DELTA
    tm = time.gmtime(t)
    rtc.datetime((tm[0], tm[1], tm[2], tm[6]+1, tm[3]+1, tm[4], tm[5], 0))

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

led.on()
set_time()
# print(time.localtime())
led.off()

# set real time clock

def zfl(s, width):
    # Pads the provided string with leading 0's to suit the specified 'chrs' length
    # Force # characters, fill with leading 0's
    return '{:0>{w}}'.format(s, w=width)

while True:
    # Get the current time
    #     t = datetime.datetime.now()
    t=rtc.datetime()
    print(t)
    # Convert the hours, minutes, and seconds to binary (BCD)

    # print("hours------" + str(t[4]))

    hours_as_digits = list(map(int, list(zfl(str(t[4]),2))))

    hours_10x_bin = bin(int(hours_as_digits[0]))[2:]
    hours_10x_bin = zfl(hours_10x_bin,2)
    led_h_10x_2 = list(map(int, list(hours_10x_bin)))[0]
    led_h_10x_1 = list(map(int, list(hours_10x_bin)))[1]
    pin_h_10x_2.value(led_h_10x_2)
    pin_h_10x_1.value(led_h_10x_1)
    # print("led_h_10x_2 " + str(led_h_10x_2))
    # print("led_h_10x_1 " + str(led_h_10x_1))

    hours_bin = bin(int(hours_as_digits[1]))[2:]
    hours_bin = zfl(hours_bin,4)
    led_h_8 = list(map(int, list(hours_bin)))[0]
    led_h_4 = list(map(int, list(hours_bin)))[1]
    led_h_2 = list(map(int, list(hours_bin)))[2]
    led_h_1 = list(map(int, list(hours_bin)))[3]
    pin_h_8.value(led_h_8)
    pin_h_4.value(led_h_4)
    pin_h_2.value(led_h_2)
    pin_h_1.value(led_h_1)

    # print("led_h_8 " + str(led_h_8))
    # print("led_h_4 " + str(led_h_4))
    # print("led_h_2 " + str(led_h_2))
    # print("led_h_1 " + str(led_h_1))

    # print("minutes------" + str(t[5]))
    minutes_as_digits = list(map(int, list(zfl(str(t[5]),2))))
    
    minutes_10x_bin = bin(int(minutes_as_digits[0]))[2:]
    minutes_10x_bin = zfl(minutes_10x_bin,3)
    led_m_10x_4 = list(map(int, list(minutes_10x_bin)))[0]
    led_m_10x_2 = list(map(int, list(minutes_10x_bin)))[1]
    led_m_10x_1 = list(map(int, list(minutes_10x_bin)))[2]
    pin_m_10x_4.value(led_m_10x_4)
    pin_m_10x_2.value(led_m_10x_2)
    pin_m_10x_1.value(led_m_10x_1)
    # print("led_m_10x_4 " + str(led_m_10x_4))
    # print("led_m_10x_2 " + str(led_m_10x_2))
    # print("led_m_10x_1 " + str(led_m_10x_1))

    minutes_bin = bin(int(minutes_as_digits[1]))[2:]
    minutes_bin = zfl(minutes_bin,4)
    led_m_8 = list(map(int, list(minutes_bin)))[0]
    led_m_4 = list(map(int, list(minutes_bin)))[1]
    led_m_2 = list(map(int, list(minutes_bin)))[2]
    led_m_1 = list(map(int, list(minutes_bin)))[3]
    pin_m_8.value(led_m_8)
    pin_m_4.value(led_m_4)
    pin_m_2.value(led_m_2)
    pin_m_1.value(led_m_1)
    # print("led_m_8 " + str(led_m_8))
    # print("led_m_4 " + str(led_m_4))
    # print("led_m_2 " + str(led_m_2))
    # print("led_m_1 " + str(led_m_1))

    # print("seconds------" + str(t[6]))
    seconds_as_digits = list(map(int, list(zfl(str(t[6]),2))))

    seconds_10x_bin = bin(int(seconds_as_digits[0]))[2:]
    seconds_10x_bin = zfl(seconds_10x_bin,3)
    led_s_10x_4 = list(map(int, list(seconds_10x_bin)))[0]
    led_s_10x_2 = list(map(int, list(seconds_10x_bin)))[1]
    led_s_10x_1 = list(map(int, list(seconds_10x_bin)))[2]
    pin_s_10x_4.value(led_s_10x_4)
    pin_s_10x_2.value(led_s_10x_2)
    pin_s_10x_1.value(led_s_10x_1)
    # print("led_s_10x_4 " + str(led_s_10x_4))
    # print("led_s_10x_2 " + str(led_s_10x_2))
    # print("led_s_10x_1 " + str(led_s_10x_1))

    seconds_bin = bin(int(seconds_as_digits[1]))[2:]
    seconds_bin = zfl(seconds_bin,4)
    led_s_8 = list(map(int, list(seconds_bin)))[0]
    led_s_4 = list(map(int, list(seconds_bin)))[1]
    led_s_2 = list(map(int, list(seconds_bin)))[2]
    led_s_1 = list(map(int, list(seconds_bin)))[3]
    pin_s_8.value(led_s_8)
    pin_s_4.value(led_s_4)
    pin_s_2.value(led_s_2)
    pin_s_1.value(led_s_1)
    # print("led_s_8 " + str(led_s_8))
    # print("led_s_4 " + str(led_s_4))
    # print("led_s_2 " + str(led_s_2))
    # print("led_s_1 " + str(led_s_1))

    # break
    # Sleep for one second
    time.sleep(1)
