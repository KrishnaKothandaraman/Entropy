import src.entropy_queue as en

def main():
    eQueue = en.EntropyQueue()
    print("Printing Queue")
    eQueue.enqueue(15)
    eQueue.enqueue(20)
    eQueue.enqueue(25)

    eQueue.dequeue()

    eQueue.enqueue(30)
    eQueue.dequeue()
    eQueue.dequeue()
    eQueue.dequeue()
    eQueue.dequeue()
    eQueue.dequeue()

if __name__ == "__main__":
    main()