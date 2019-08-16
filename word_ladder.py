import re

file = ""
filecheck = False

def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def find(word, words, seen, target, path):
  bad_letter = ["z"]
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list], reverse = True)   ##List now returns in reverse Does lead to gold
  for (match, item) in list:                                            ##in 3 steps now but hide and seek still too long
    for i in bad_letter:              #removed inefficient paths that use the letter z hide and seek now in 6 steps
      if i in item:
        list.remove((match, item))
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

while filecheck == False:               ##Error checking for File name input
  try:
    fname = input("Enter dictionary name: ")
    file = open(fname)
    filecheck = True
  except:
    print("Incorrect File name")

lines = file.readlines()


while True:
  start = input("Enter start word:")
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
  target = input("Enter target word:")
  break

#########
##This section removes selected words from the words list by comparing the words list to a list of selected
##Bad words, the revised list is then passed into the find function call.
remove_words = []
end = False
while end == False:
  badword = input("Please add any words you do not want used in the path, Or leave blank to continue:")
  if badword != "":
    remove_words.append(badword)
  else:
    break

wordsRemoved = [i for i in words if i not in remove_words]
##End Remove selected words section
#########

count = 0
path = [start]
seen = {start : True}


if find(start, wordsRemoved, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

