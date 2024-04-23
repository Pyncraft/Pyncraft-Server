import ursinanetworking as net

client = net.UrsinaNetworkingClient("localhost", 25800)


@client.event
def CurrentWorld(data):
    print(f"{data} CurrentWorld")

@client.event
def newBlock(data):
    print(f"{data} newBlock")

@client.event
def onConnectionEstablished():
    print("I'm connected to the server !")

@client.event
def onConnectionError(Reason):
    print(f"Error ! Reason : {Reason}")


while True:
    client.process_net_events()