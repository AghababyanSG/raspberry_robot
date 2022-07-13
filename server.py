import socket
import struct
import fcntl
import threading
import Motors_PWM2
import time
import RPi.GPIO as GPIO

FREQUENCY = 490

def get_interface_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                                            0x8915,
                                            struct.pack('256s',b'wlan0'[:15])
                                            )[20:24])
def StopTcpServer():
        try:
            #server_socket1.shutdown(socket.SHUT_RDWR)
            server_socket1.close()            
        except Exception as e:
            print ('\n'+"No client connection")
def StartTcpServer():
    
    

    HOST = str(get_interface_ip())
    server_socket1 = socket.socket()
    server_socket1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
    server_socket1.bind((HOST, 5000))
    server_socket1.listen(1)
    #server_socket = socket.socket()
    #server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
    #server_socket.bind((HOST, 8000))              
    #server_socket.listen(1)
    print('Server address: '+HOST)
    conn, addr = server_socket1.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            if data=="Forward":
                print("forward")
                Start_Motors("forward", 100, 100, 1)
            if data=="Back":
                print("Back")
                Start_Motors("back", 100, 100, 1)
                
            if not data:
                pass
                #StopTcpServer()
                #StartTcpServer()
                #pass
                #break
            #conn.sendall(data)
def Start_Motors(forward, Right, Left, Time):
    GPIO_PWM_0 = 12
    GPIO_PWM_1 = 13
    GPIO_PWM_L0 = 18
    GPIO_PWM_L1 = 19
    #WORK_TIME = 2

    FREQUENCY = 490

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(GPIO_PWM_0, GPIO.OUT)
    GPIO.setup(GPIO_PWM_1, GPIO.OUT)
    GPIO.setup(GPIO_PWM_L0, GPIO.OUT)
    GPIO.setup(GPIO_PWM_L1, GPIO.OUT)
    
    if forward=='forward':
        print('received data!!!')
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(2)
        GPIO.cleanup()
    elif forward=='back':
        pwmOutput_0 = GPIO.PWM(GPIO_PWM_1, FREQUENCY)
        pwmOutput_1 = GPIO.PWM(GPIO_PWM_L0, FREQUENCY)
        GPIO.output(GPIO_PWM_L1, 0)
        GPIO.output(GPIO_PWM_0, 0)
        pwmOutput_0.start(Right)
        pwmOutput_1.start(Left)
        time.sleep(Time)
        pwmOutput_0.stop(Right)
        pwmOutput_1.stop(Left)
        time.sleep(1)
        GPIO.cleanup()

if __name__ == '__main__':
    StartTcpServer()


#t=threading.Thread(target=StartTcpServer)
#t.start()
