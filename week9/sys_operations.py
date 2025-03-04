import platform
import socket
import os

print("Current Machine Type:")
print(platform.machine())

print("--------------------\n")

print("Current Processor Type:")
print(platform.architecture())

print("--------------------\n")

print("Set Timeout of socket in seconds:")
print(socket.setdefaulttimeout(50))

print("--------------------\n")

print("Get Timeout of socket in seconds:")
print(socket.getdefaulttimeout())

print("--------------------\n")

print("Operating System Type:")
print(os.name)

print("--------------------\n")

print("Operating System Name:")
print(platform.system())

print("--------------------\n")