# vuln in python2


def help():
    # help section for program usage & options
    print('Usage: python main.py')
    print('Available commands:\nhelp()\nstart()\nexit()\nconnect()')

def flag():
    for i in range(0,20):
        print("congrats, you found it")
    print('The flag is nothing')


def start():  # interactive mode, including listener & client setup
    print 'Hi lets get started from the beginning'

def bad_args():
    print('Bad Arguments')
    
def connect():
    print("connecting")
    print("mencoba untuk koneksi\n")
    print("tapi sayangnya fitur ini belum jadi")
def exit():
    print("exiting")
def console():
    while True:
        try:
            inp = input(">>> ").split('"')
        except:
            pass



def main():
    print('Welcome to Speeto console')
    print('Multiplatform speed test')
    print('')
    print('try to type "help" or "status"')
    print('type "start" for interactive mode')
    print('------------------------')
    help()

    console()


if __name__ == '__main__':
    main()
