# list of squares of only the odd numbers.
squares_of_odds = [i * i for i in range(1, 21) if i % 2 == 1]
print(squares_of_odds)

#list with each name capitalized.
names = ["alice", "bob", "carol"]
Capitalized_words=[]
for name in names:
  Capitalized_words.append(name.capitalize())
print(Capitalized_words)


#or

names = ["alice", "bob", "carol"]
capitalized = [name.capitalize() for name in names]
print(capitalized)

#Given a list with duplicates, [1, 2, 2, 3, 3, 3], get a list of unique values using a set.
nums = [1, 2, 2, 3, 3, 3]
unique_nums = list(set(nums))
print(unique_nums) 
