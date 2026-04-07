# You have a list of strings:
 
words = ["cat", "dog", "bird", "rat", "bat"]


# Question:  
# Count words longer than 3 characters using a simple loop.
count = 0
for word in words:
    if len(word) > 3:
        count += 1
print(count)
