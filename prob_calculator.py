import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

    #print("contents =", self.contents)

  def draw(self, no_balls_to_draw):
    if no_balls_to_draw > len(self.contents):
      return self.contents
    else:
      balls_drawn = []
      for i in range(no_balls_to_draw):
        item = self.contents.pop(random.randrange(len(self.contents)))
        balls_drawn.append(item)
      return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  balls = []
  M = 0
  for key, value in expected_balls.items():
    for i in range(value):
      balls.append(key)

  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    total = 0
    for i in balls:
      idx = 0
      while True:
        try:
          idx = balls_drawn.index(i)
          total += 1
          del balls_drawn[idx]
          break
        except ValueError:
            break
      if total == len(balls):
        M+=1
  return M/num_experiments