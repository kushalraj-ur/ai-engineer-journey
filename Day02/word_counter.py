sentence = input("Enter The sentence : ")
split_sentence=sentence.lower().split()

counts = {}
for i in split_sentence:
  counts[i]=counts.get(i,0)+1
sorted_items = sorted(counts.items(),key=lambda item:item[1],reverse=True)

print('Word Frequencies:')
for i,count in sorted_items:
  print(f'{i}:{count}')

unique_words = set(split_sentence)
print(f'Total Unique Words : {len(unique_words)}')
  
    