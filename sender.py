import socket 
import time
# import socket module /library to create 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# what is my receiver address
recv_addr=("192.168.1.12",9999)
# Now i want to send message
while 2 > 1 :
    user_data=input("enter your message :- ")
    # converting data into ascii code
    newdata=user_data.encode('ascii')
    # now you can send data 
    s.sendto(newdata, recv_addr)
    time.sleep(2)
    print("your message has been sent..")
    # now waiting for reply 
    print(s.recvfrom(10))
