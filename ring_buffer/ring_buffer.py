class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
      if self.current == self.capacity:
        # self.current = 0
        # self.storage[self.current] = item
        # self.current += 1
        self.storage[0] = item

        print('full', self.storage)
      else:
        self.storage[self.current] = item
        self.current += 1


  def get(self):
      print('storage not full',self.storage[: self.current])
      return self.storage[: self.current]
    # if self.storage[self.current] == None:
    #   print('storage not full',self.storage[: self.current])
    #   return self.storage[: self.current]
    # else:
    #   print('storage full', self.storage[: self.capacity])
    #   # return self.storage[: self.capacity]
