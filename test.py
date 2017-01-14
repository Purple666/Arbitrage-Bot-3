import threading


def hello():
    print('ciao')
    t = threading.Timer(5.0,hello)
    t.start()
    
hello()