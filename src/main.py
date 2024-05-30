import src.entropy_queue as en
import sys

def main(host, port):
    eQueue = en.EntropyQueue(host, port)
    eQueue.initSocketConnection()

def usage():
        print("            Usage: main.py <host> <port>")
        print("            host: Host address to bind the queue")
        print("            port: Port to listen on")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Script needs at least two arguments")
        usage()
        exit(1)
    
    try: 
        port = int(sys.argv[2])
    except ValueError:
        print(f"Invalid Argument for port {sys.argv[2]}")
        usage()
    main(sys.argv[1], port)