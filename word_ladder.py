import re


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

def file_checker():
  filecheck = False
  while filecheck == False:  ##Error checking for File name input
    try:                      ##Try to open file if fail Print error and start again
      fname = input("Enter dictionary name: ")
      file = open(fname)
      filecheck = True
    except:
      print("Incorrect File name")
  global lines
  lines = file.readlines()

def start_input(start):             # Check if the Starting word input is blank, contains letters or special characters
  if start == "" or not start.isalnum():
    return False
  if any(char.isdigit() for char in start):
    return False
  else:
    return True

def target_input(target, start):      # Check if the target word input is blank, contains letters or special characters and is same length as the start word
  if target == "" or not target.isalnum() or len (target)!=len(start):
    return False
  if any(char.isdigit() for char in target):
    return False
  else:
    return True

def main():

  file_checker()   ##Call for function to check filename exists

  while True:
    start = input("Enter start word:").replace(" ","") #Remove any spaces form input
    while start_input(start) == False:                  #Calls the Start input check
      print("Start word cannot be blank, contain numbers or special characters")
      start = input("Enter start word:").replace(" ", "")

    words = []
    for line in lines:
      word = line.rstrip()
      if len(word) == len(start):
        words.append(word)

    target = input("Enter target word:").replace(" ","") #Remove any spaces form input
    while target_input(target, start) == False:         #Calls the target input check
      print("Target word cannot be blank, contain numbers or special characters and must be same length as start word")
      target = input("Enter start word:").replace(" ", "")
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


  path = [start]
  seen = {start : True}


  if find(start, wordsRemoved, seen, target, path):
    path.append(target)
    print(len(path) - 1, path)
  else:
    print("No path found")

if __name__ == '__main__':
  main()