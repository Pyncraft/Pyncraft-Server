import ursinanetworking as net
import json

def unlog(Class_, Context_, Message_):

    print(f"[{Class_} / {Context_}] {Message_}")

defaultport = 25800
unlog("Pynserver", "__main__", f"Default port is {defaultport}")
server = net.UrsinaNetworkingServer("localhost", 25800)

with open("dirt.wrld") as f:
    unlog("Pynserver", "__main__", "Loading world...")
    blocks = json.load(f)
    unlog("Pynserver", "__main__", "Loaded world.")


@server.event
def onClientConnected(Client):
    unlog("Pynserver", "onClientConnected", f"{Client} connected")
    Client.send_message("currentWorld", blocks)

@server.event
def placeBlock(Client, data):
    unlog("Pynserver", "__main__", f"Client {Client} placed block!")
    blocks[data["pos"]] = data["id"]
    server.broadcast("newBlock", data)

def destroyBlock(Client, data):
    unlog("Pynserver", "__main__", f"Client {Client} destroyed block!")
    del blocks[data]
    server.broadcast("destroyBlock", data)


@server.event
def onClientDisconnected(Client):
    unlog("Pynserver", "onClientDisconnected", f"{Client} disconnected")

unlog("Pynserver", "__main__", "Main loop started")
while True:
    server.process_net_events()