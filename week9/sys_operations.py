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

print("Current Process ID:")
print(os.getpid())

print("--------------------\n")

file_name = "fdpractice.txt"
# Print the PID of the process before forking
print(f"[Before Fork] Process ID: {os.getpid()}")

#Open the file using os.open
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process ID: {os.getpid()} opened file_handle: {file_handle}]")

#Convert the file handle into a file object for writing
file_object_TextIO = os.fdopen(file_handle, "w+")

#Write text to the file
file_object_TextIO.write("Lab Tues 10-12")
file_object_TextIO.flush() # Ensure content is written immediately

print(f"[Before Fork] Process ID: {os.getpid()}")



