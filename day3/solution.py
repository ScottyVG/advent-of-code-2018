# Python

with open('input.txt', 'r') as data:
# part 1
  all_lines = data.readlines()
  mat = [0 for i in range(1000 * 1000)]
  for string in all_lines:
    string = string.replace('x', ' ')
    string = string.replace(':', ' ')
    string = string.replace(',', ' ')
    split_string = string.split()
    _, _, x_corner, y_corner, x_dim, y_dim = string.split()
    for i in range(int(x_corner), int(x_corner) + int(x_dim)):
      for j in range(int(y_corner), int(y_corner) + int(y_dim)):
        mat[(i * 1000) + j] += 1
  over_claimed = 0
  for i in range(1000*1000):
    if mat[i] > 1:
      over_claimed += 1
  print(over_claimed)

# part 2
  for string in all_lines:
    string = string.replace('x', ' ')
    string = string.replace(':', ' ')
    string = string.replace(',', ' ')
    split_string = string.split()
    claim_num, _, x_corner, y_corner, x_dim, y_dim = string.split()
    max_claimed = 0
    for i in range(int(x_corner), int(x_corner) + int(x_dim)):
      for j in range(int(y_corner), int(y_corner) + int(y_dim)):
        max_claimed = max(max_claimed, mat[(i*1000) + j])
    if max_claimed == 1:
      print(claim_num)



