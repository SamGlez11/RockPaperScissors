import pickle
import socket
from _thread import *
from player import Player
import sys
from game import Game

server = "100.84.22.169"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for connection, server started...")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        data = conn.recv(4096 * 4).decode()
        try:
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print ("Connected to: ", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating game ")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))
"""
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + ',' + str(tup[1])
No longer nedded ^^
'''

'''
THIS IS FOR SQUARES MOVING
players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 255, 0))]
def threaded_client(conn, player):
    #conn.send(str.encode(make_pos(pos[player])))
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            #data = read_pos(conn.recv(1024).decode())
            data = pickle.loads(conn.recv(1024))
            #pos[player] = data
            players[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    #reply = pos[0]
                    reply = players[0]
                else:
                    #reply = pos[1]
                    reply = players[1]

                print("Received:", data)
                print ("Sending : ", reply)

            #conn.sendall(str.encode(make_pos(reply)))
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Connection closed")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
"""