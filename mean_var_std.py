import numpy as np

def calculate(list):

  # Checks that list has 9 digits & raises ValueError if not
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    # Convert list into a 3x3 Numpy array
    array = np.array(list).reshape(3,3)

  # Calculations
  mean = [array.mean(axis = 0).tolist(), array.mean(axis = 1).tolist(), array.mean().tolist()]
  var = [array.var(axis = 0).tolist(), array.var(axis = 1).tolist(), array.var().tolist()]
  std = [array.std(axis = 0).tolist(), array.std(axis = 1).tolist(), array.std().tolist()]
  max = [array.max(axis = 0).tolist(), array.max(axis = 1).tolist(), array.max().tolist()]
  min = [array.min(axis = 0).tolist(), array.min(axis = 1).tolist(), array.min().tolist()]
  sum = [array.sum(axis = 0).tolist(), array.sum(axis = 1).tolist(), array.sum().tolist()]

  # Create dictionary for calculations
  calculations = {
      'mean': mean,
      'variance': var,
      'standard deviation': std,
      'max': max,
      'min': min,
      'sum': sum
  }

  return calculations