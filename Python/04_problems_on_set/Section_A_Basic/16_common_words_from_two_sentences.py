sentence1 = "python is easy and powerful"
sentence2 = "python is popular and useful"

words1 = set(sentence1.split())
words2 = set(sentence2.split())

print("Common words =", words1 & words2)
