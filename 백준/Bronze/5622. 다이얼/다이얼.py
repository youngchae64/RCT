from collections import Counter

word = input()
char_counts = Counter(word)

total_count_3 = char_counts['A'] + char_counts['B'] + char_counts['C']
total_count_4 = char_counts['D'] + char_counts['E'] + char_counts['F']
total_count_5 = char_counts['G'] + char_counts['H'] + char_counts['I']
total_count_6 = char_counts['J'] + char_counts['K'] + char_counts['L']
total_count_7 = char_counts['M'] + char_counts['N'] + char_counts['O']
total_count_8 = char_counts['P'] + char_counts['Q'] + char_counts['R'] + char_counts['S'] 
total_count_9 = char_counts['T'] + char_counts['U'] + char_counts['V']
total_count_10 = char_counts['W'] + char_counts['X'] + char_counts['Y'] + char_counts['Z'] 
total = total_count_3*3 + total_count_4*4 + total_count_5*5 + total_count_6*6 + total_count_7*7 + total_count_8*8 +total_count_9*9 + total_count_10*10 
print(total)