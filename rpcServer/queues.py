class Queues:
    def __init__(self):
        super().__init__()
        self.default_queues=["ecdsa","serpent"]

    def check_queue(self,queue):
        if queue in self.default_queues:
            return True
        return False
    
    def display_queue_info(self):
        print("")
        print("QUEUES DETAILS")
        print("================")
        print("galaxy:","Search for host IP for any website")
        print("serpent:","Serpent should be chosen because it is the most secure of the AES finalists.😎")

