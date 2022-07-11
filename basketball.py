import pickle

def read_records():
    infile = open("game.dat","rb")

    while True:
        try:
            participants = pickle.load(infile)
            print(participants[0], participants[1])
        except EOFError:
            break
    infile.close()

read_records()