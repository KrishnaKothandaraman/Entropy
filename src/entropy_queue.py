from src.entropy_node import Node
from typing import List, Optional
import socket, time
import json
import enum

class StatusType(enum.Enum):
    SUCCESS = enum.auto()
    FAIL    = enum.auto()

class JsonDecodeResult:
    status: StatusType
    result: dict
    error: str

    def __init__(self):
        self.status = 0 
        self.result = None
        self.error = ""

    def setSuccess(self, result):
        self.status = StatusType.SUCCESS
        self.result = result
    
    def setFailure(self, error_message: str):
        self.status = StatusType.FAIL
        self.error  = error_message
    
    def getSuccessResult(self):
        return self.result
    
    def getFailResult(self):
        return self.error
    
    def isSuccess(self) -> bool:
        return True if self.status == StatusType.SUCCESS else False


# First in First Out
class EntropyQueue:
    def __init__(self, host="localhost", port=5001):
        self.items: List[Node] = []
        self.head: Node = None
        self.tail: Node = None
        self.host = host
        self.port = port
        self.socket = None

    def parseMessageToJson(self, data: bytes) -> JsonDecodeResult:
        jsonDecodeResult = JsonDecodeResult()
        try:
            # TODO: Can add validations here to make sure the message follows the protocol
            raw_string = data.decode("utf-8")
            raw_string = json.loads(raw_string)
            jsonDecodeResult.setSuccess(raw_string)
        except UnicodeDecodeError as e:
            err = f"ERROR: Could not decocde message: {data}"
            print(err)
            jsonDecodeResult.setFailure(err)
        except json.decoder.JSONDecodeError as e:
            err = f"ERROR: Invalid JSON : {raw_string}"
            print(err)
            jsonDecodeResult.setFailure(err)
        except Exception as e:
            print(e)
        finally:
            return jsonDecodeResult
        
    def initSocketConnection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            # TODO: Accept only one connection for now. Will expand this to multiple consumers and receivers later
            print(f"INFO: Queue coming up. Listening for a new connection.....")
            s.listen(1)
            conn, addr = s.accept()
            print(f"INFO: Connection received from: {addr}")
            with conn:
                while True:
                    print(f"Listening for data....")
                    data = conn.recv(1024)
                    print(f"Received {data}")
                    parseResult : JsonDecodeResult = self.parseMessageToJson(data)
                    if parseResult.isSuccess():
                        jsonMessage = parseResult.getSuccessResult()
                        print(f"Received {jsonMessage}")
                        if jsonMessage["type"] == "quit":
                            break
                        conn.sendall("Done".encode("utf-8"))
                    else:
                        error_message = parseResult.getFailResult()
                        print(f"Error: {error_message}")
                        conn.sendall(error_message.encode("utf-8"))

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.printQueue()

    def dequeue(self) -> Optional[Node]:
        return_node = None
        if not self.head:
            return_node = None
        
        elif self.head == self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            return_node = old_head
        else:
            old_head = self.head
            self.head = self.head.next
            self.head.prev = None
            return_node = old_head
        self.printQueue()
        return return_node

    def printQueue(self):
        cur_head = self.head
        if not cur_head:
            print("None")
        while cur_head:
            if cur_head == self.head == self.tail:
                print(f"None <- {cur_head.value} -> None")
            elif cur_head == self.head:
                print(f"None <- {cur_head.value} <-> ", end = "")
            elif cur_head == self.tail:
                print(f"{cur_head.value} -> None")
            else:
                print(f"{cur_head.value} <-> ", end="")
            cur_head = cur_head.next

    


