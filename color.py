import cv2
from collections import Counter

#convert (r,g,b) tuples to color code  (for eg:-FF5733)
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

#create a lists of color code from image
def create_list_of_colors(path):
  img = cv2.imread(path)
  rows = img.shape[0]
  columns = img.shape[1]
  l=[]
  x1=[]
  x2=[]
  y1=[]
  y2=[]
  for i in range(rows):
    for j in range(columns):
      s_a = img[i][j].tolist()
      s_a = tuple(s_a[::-1])
      code = rgb_to_hex(s_a)
      l.append(code)
      if i==0:
        x1.append(code)
      elif i==rows-1:
        x2.append(code)
      if j==0:
        y1.append(code)
      elif j==columns-1:
        y2.append(code)
  return l,x1,x2,y1,y2


#finding dominant color from list l
def get_dominant_color(l):
  test_list = Counter(l)
  res = test_list.most_common(1)[0][0]
  return '#'+res

#creating list "border"
def create_border_color_list(x1,x2,y1,y2):
  border=[]
  border.extend(x1)
  border.extend(x2)
  border.extend(y1)
  border.extend(y2)
  return border

#getting border color from list "border"
def get_dominant_border(border):
  test_border = Counter(border)
  ans = test_border.most_common(1)[0][0]
  return '#'+ans


#main function to run with image path as argument.
def run_for_results(path):
  result={}
  l,x1,x2,y1,y2 = create_list_of_colors(path)
  ans1 = get_dominant_color(l)
  result['dominant_color'] = ans1
  border = create_border_color_list(x1, x2, y1, y2)
  ans2 = get_dominant_border(border)
  result['logo_border'] = ans2
  print(result)
  return result

