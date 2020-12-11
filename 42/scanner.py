from socket import gethostbyname, socket, SOCK_STREAM, AF_INET

target = input('Enter the host to scan: ')
port = input("Enter port to scan: ")
port = int(port)
t_IP = gethostbyname(target)

print (f'\nPlease wait while we scan {t_IP}.')
s = socket(AF_INET, SOCK_STREAM)
conn = s.connect_ex((t_IP, port))
if int(conn) == 0:
    print(f"\n{t_IP} has {port} OPEN.\n")
else:
    print(f"\n{t_IP} has {port} CLOSED.\n")
s.close()