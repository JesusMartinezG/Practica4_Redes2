import http.client

# get http server ip
from pip._vendor.distlib.compat import raw_input

http_server = '127.0.0.1:8000'
# create a connection
conn = http.client.HTTPConnection(http_server)

while 1:
    cmd = raw_input('input command (ex. GET index.html): ')
    cmd = cmd.split()

    if cmd[0] == 'exit':  # tipe exit to end it
        break

        # request command to server
    conn.request(cmd[0], cmd[1])

    # get response from server
    rsp = conn.getresponse()

    # print server response and data
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)

conn.close()