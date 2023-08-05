class Channels:
    def __init__(self):
        self.default_queue={"galaxy","aot","sheep","spider","zero"}
        self.participant={
            "galaxy":0,
            "aot":0,
            "sheep":0,
            "spider":0,
            "zero":0
        }
    def add_channel(self,channel_name):
        self.default_queue.add(channel_name)
    def update_channel(self,channel):
        if channel in self.participant.keys():
            self.participant[channel] += 1
            print("Current participant: ",self.participant[channel])
        else: print("channel not exist")

    def show_channels(self):
        count =0
        for i in self.default_queue:
            print("{} " ,i)
            count += 1 
            if count == 3: 
                print("\n")
                count=0
        
