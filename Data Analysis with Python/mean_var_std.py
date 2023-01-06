import numpy as np 

def calculate(n_list):
  if len(n_list)!=9:
    raise ValueError("n_list must contain nine numbers.")
  calculations = dict()
  ZList = []
  List_reshaped = np.reshape(n_list, (3,3)).tolist()
  functions = {'mean': np.mean, 'variance':np.var, 'standard deviation': np.std, 'max': np.max, 'min': np.min, 'sum': np.sum}
  for key in functions:
    ZList.append(functions[key](List_reshaped, axis=0).tolist())
    ZList.append(functions[key](List_reshaped, axis=1).tolist())
    ZList.append(functions[key](n_list).tolist())
    calculations[key] = ZList
    ZList = []
  return calculations


res = calculate([0,1,2,3,4,5,6,7,8])
print(res)
