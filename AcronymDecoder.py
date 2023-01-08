#gets tweet or text from user
tweet = input('Enter full tweet or text:\n')
intro = "Here are the acronyms in the tweet or text:"

if "LOL" in tweet:
  print(intro)
  print('LOL = laughing out loud')
elif "BFN" in tweet:
  print(intro)
  print('BFN = bye for now')
elif "IRL" in tweet:
  print(intro)
  print('IRL = in real life')
elif "IMO" in tweet:
  print(intro)
  print('IMO = in my opinion')
elif "AFK" in tweet:
  print(intro)
  print('AFK = away from keyboard')
elif "NFSW" in tweet:
  print(intro)
  print("NSFW = not safe for work')
else:
  print("There are no known accronyms in the tweet or text that you entered.")        
