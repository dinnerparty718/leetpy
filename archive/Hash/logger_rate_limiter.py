class Logger:

    def __init__(self):
        self.m = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.m:
            self.m[message] = timestamp + 10
            return True
        elif message in self.m and timestamp > self.m[message]:
            self.m[message] = timestamp + 10
            return True
        else:
            return False

        # Your Logger object will be instantiated and called as such:
        # obj = Logger()
        # param_1 = obj.shouldPrintMessage(timestamp,message)


obj = Logger()
