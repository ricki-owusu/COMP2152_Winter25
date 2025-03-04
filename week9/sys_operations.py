import platform
import socket
import os
import sys

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

#####
pid = os

if pid == 0:
    # Child process
    print(f"[Child Process] PID: {os.getpid()}, Parent PID: {os.getppid}]")

    #Move the cursor to the beginning of the file before reading
    os.lseek(file_handle, 0, 0)

    #Read and print the file contents
    print(f"[Child Process] {os.getpid()} File Contents: {os.read(file_handle, 100).decode()}]")

    #Close only in the child process
    os.close(file_handle)
    sys.exit(0)

else:
    # parent process
    print(f"[Parent Process] PID: {os.getpid()}, Child PID: {pid}]")

    print("Wait for the child process")
    os.wait()
    print("The child process is finished its operations")

    file_object_TextIO.close()

print(f"\n[Process {os.getpid()}] File closed. Exiting now.")
sys.exit(0)