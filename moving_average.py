class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.window = []


    def next(self, val: int) -> float:
        """
        Method:
        - We will take in the input and push it to the window
        - We will check the window size to see if it's > 0 and <= 3
        -- If so, we will take the average of the elements and return
        -- Otherwise, pop the oldest element (0) and then determine the average
        """
        self.window.append(val)
        if len(self.window) > self.size:
            self.window.pop(0)
        if len(self.window) > 0:
            # return the sum of the elements divided by the size of the window,
            # the size should be greater than self.size
            return(float(sum(self.window)) / len(self.window))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Initial thoughts:
# - We consider the n most recent inputs, where n = size
# - We stay mindful of the input size, and so we can remove any old data from our window

# Questions?
# Can the inputs fit in memory? Will the average be able to fit in memory?
# Are we expecting floats or ints? Will the return type need to be a float or int?
# -> Answer provided by leetcode
# Can we get negative numbers?
# Will our size value be positive?
# Could someone set the size to 0? How would we handle that?
