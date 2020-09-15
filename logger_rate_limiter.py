class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.message_queue = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if self.message_queue == {} or message not in self.message_queue:
            self.message_queue[message] = timestamp + 10
            return(True)
        if message in self.message_queue:
            if timestamp >= self.message_queue[message]:
                self.message_queue[message] = timestamp + 10
                return(True)
            else:
                return(False)

# Create test cases
logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))
print(logger.shouldPrintMessage(2, "bar"))
print(logger.shouldPrintMessage(3, "foo"))
print(logger.shouldPrintMessage(8, "bar"))
print(logger.shouldPrintMessage(10, "foo"))
print(logger.shouldPrintMessage(11, "foo"))

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

# Initial thoughts:
# It is important, for a moment, that we know when a message came in
# and when is the next time stamp which we can allow it to print
# Messages could be coming in for an infinite amount of time, so for a more
# realistic approach, we can't hold too much data in memory
# -- Perhaps we can pop messages which haven't been re-encountered and we
# are past it's "okay" timestamp
# -- Perhaps we can use a queue to determine the priority of messages which
# will their "holding period" will expire soon.

# Possible solution steps:
# Have a double-ended queue to use for the messages
# -- Each element in the queue is a tuple (message, "okay" timestamp)
# When a message gets passed in, we'll check if it's in the queue (O(n)) time
# If not, then insert the message to the back of queue (with next timestamp + 10)
# -- and return true
# Otherwise, check that we reached it's "okay" time period and return true or false
# Check the current timestamp passed in and see if it's >= the one at the front of
# the queue. If it is, pop that element. Whenever it's encountered again, the answer
# will be true. Continue to pop any messages that meets this constraint. O(n) time
