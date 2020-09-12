anagram_control = {} 

diff_a = 0
diff_b = 0

a = input("a: ")
b = input("b: ")

# Count number of letters in a string
for char in a:
    if char not in anagram_control:
        anagram_control[char] = 0
    anagram_control[char] += 1

# Count and check number of letters in b string
for char in b:
    if char not in anagram_control:
        anagram_control[char] = 0
    anagram_control[char] -= 1

# Count number of different letters for each string
for char in anagram_control:
    if 0 < anagram_control[char]:
        diff_a += anagram_control[char]
    else:
        diff_b -= anagram_control[char]

# Show result
if 0 < (diff_a + diff_b):
    print(f"remove {diff_a} characters from '{a}' and {diff_b} characters from '{b}'")
else:
    print("they are anagrams")