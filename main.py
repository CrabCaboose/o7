import socket
import machine
import network
import time
import gc

# Set the time to 10:30:00 AM
# Get the current time
#local_time = time.localtime(current_time)
#print(f"Local time: {local_time.tm_hour}:{local_time.tm_min}:{local_time.tm_sec}")


# dat = open("data.json")
# data = dat.read()
# dat.close()
boardpin = machine.ADC(26)
ssid = "o7"
password = "123456789"
gc.collect()
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)
while not ap.active():
    0
print("Connection successful")
print(ap.ifconfig())
led = machine.Pin("LED", machine.Pin.OUT)


def web_page():
    A = b"HTTP/1.1 200 OK\r\n\r\n" + open("index.html").read()
    return A


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 80))
s.listen(5)


def send_file_in_chunks(file_path, client_socket, chunk_size=16384):
    A = file_path
    E = "HTTP/1.1 200 OK\r\n\r\n"
    client_socket.send(E.encode())
    print(A)
    try:
        print("Serving file: " + A)
        #conn.sendall(b"HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n")
        with open(A, "rb") as D:
            while True:
                B = D.read(chunk_size)
                #print(B)
                if not B:
                    break
                conn.sendall(B)
                #else:
                    #conn.sendall(b"HTTP/1.0 404 Not Found\r\n\r\n<h1>404 - Not Found</h1>")
    except OSError as C:
        #conn.sendall(b"HTTP/1.0 400 Bad Request\r\n\r\n<h1>400 - Bad Request</h1>")
        print(C)
        conn.close()


while True:
    led.toggle()
    time.sleep(0.5)
    adcval = boardpin.read_u16()
    volt = (3.3 / 65535) * adcval
    temperature = (100*volt)-50
    temperature = temperature * 1.8 + 32
    conn, addr = s.accept()
    #print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    reques = request.decode().splitlines()[0]
    #print("Request:", reques)
    path = reques.split(" ")[1]
    #print("Path is: " + path)
    #print("Content = %s" % str(request))
    if path == "/Chart.js":
        print('sending chart library')
        send_file_in_chunks("Chart.js", conn)
    elif path == "/temp":
        response = "HTTP/1.1 200 OK\r\n\r\n" + str(temperature)
        conn.send(response)
    elif "/time/" in path:
        #print(path)
        timer = int(int(path.split("/")[2])/1000)
        print("Time: " + str(timer))
        current_time = time.localtime(timer)
        print(current_time)
    else:
        response = web_page()
        conn.sendall(response)
    conn.close()
