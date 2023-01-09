'''

O(1)

O(M)


'''


class Logger:

    def __init__(self):
        self.msg_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg_dict:
            self.msg_dict[message] = timestamp
            return True
        if timestamp - self.msg_dict[message] >= 10:
            self.msg_dict[message] = timestamp
            return True
        else:
            return False


logger = Logger()


print(logger.shouldPrintMessage(1, 'foo'))
