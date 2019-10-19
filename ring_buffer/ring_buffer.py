
class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity # initialize storage

  def append(self, item):
    self.storage[self.current] = item # put the item into storage
    if self.current < self.capacity - 1: # if the current is less than max capacity
      self.current += 1 # increment current
    else:
      self.current = 0 # if max capacity reset to 0

  def get(self):
    return [item for item in self.storage if item != None]