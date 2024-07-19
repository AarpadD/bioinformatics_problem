with open('/Users/arpad/Downloads/dna.txt', 'r') as file:
    s = file.read().replace('\n', '')
count_a = s.count('A')
count_c = s.count('C')
count_g = s.count('G')
count_t = s.count('T')
print(count_a, count_t, count_c, count_g)
