#PROBLEM -> Counting DNA Nucleotides
#An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T')
# is "ATGCTTCAGAAAGGTCTTACG."
#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times
# that the symbols 'A', 'C', 'G', and 'T' occur in s.


with open('/Users/arpad/Downloads/dna.txt', 'r') as file:
    s = file.read().replace('\n', '')
count_a = s.count('A')
count_c = s.count('C')
count_g = s.count('G')
count_t = s.count('T')
print(count_a, count_t, count_c, count_g)
