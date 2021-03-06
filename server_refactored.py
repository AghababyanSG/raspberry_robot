import socket
import struct
import fcntl
import threading
# import Motors_PWM2
import time
import RPi.GPIO as GPIO

FREQUENCY = 490


def get_interface_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                                        0x8915,
                                        struct.pack('256s', b'wlan0'[:15])
                                        )[20:24])


# def StopTcpServer():
#     try:
#         # server_socket1.shutdown(socket.SHUT_RDWR)
#         server_socket1.close()
#     except Exception as e:
#         print('\n' + "No client connection")


def StartTcpServer():
    HOST = str(get_interface_ip())
    server_socket1 = socket.socket()
    server_socket1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    server_socket1.bind((HOST, 5000))
    server_socket1.listen(1)
    # server_socket = socket.socket()
    # server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
    # server_socket.bind((HOST, 8000))
    # server_socket.listen(1)
    print('Server address: ' + HOST)
    conn, addr = server_socket1.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            if data == "forward":
                print("forward")
                start_motors("forward", 100, 100, 1)
            if data == "Back":
                print("Back")
                start_motors("back", 100, 100, 1)

            if not data:
                pass
                # StopTcpServer()
                # StartTcpServer()
                # pass
                # break
            # conn.sendall(data)


def start_motors(direction, right_pwm, left_pwm, engines_working_time):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([12, 13, 18, 19], GPIO.OUT)

    if direction == "forward":
        print('ATTACK!!!')
        # right_wheels("forward")
        # left_wheels("forward")
        GPIO.output([13, 18], GPIO.HIGH)

    elif direction == "back":
        right_wheels("back")
        left_wheels("back")
    else:
        pass


def right_wheels(direction):
    """
    Controls left wheels of robot
    :param direction: Shows direction to which they have to go
    :return: None
    """
    if direction == "forward":
        GPIO.output(13, GPIO.HIGH)
        time.sleep(1)
    elif direction == "back":
        GPIO.output(12, GPIO.HIGH)
        time.sleep(1)
    else:
        pass
    GPIO.cleanup()


def left_wheels(direction):
    """
    Controls left wheels of robot
    :param direction: Shows direction to which they have to go
    :return: None
    """
    if direction == "forward":
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
    elif direction == "back":
        GPIO.output(19, GPIO.HIGH)
        time.sleep(1)
    else:
        pass
    GPIO.cleanup()


if __name__ == '__main__':
    StartTcpServer()
