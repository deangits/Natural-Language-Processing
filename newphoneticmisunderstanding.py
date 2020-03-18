import numpy as np

#Lists of the phonetic characters of the converted ATC sentences.
pstring1 = ["æ","l","t","ɪ","t","j","uː","d", "r","ɪ","s","t","r","ɪ","k","ʃ","ə","n","z","ɑː","k","æ","n","s","ə","l","d"]
pstring2 = ["s","ɜː","k","l","t","uː","r","ʌ","n","w","eɪ"]
pstring3 = ["h","æ","v","n","ʌ","m","b","ə","z"]
pstring4 = ["h","aʊ","d","uː", "j","uː", "h","ɪə","m","iː"]
pstring5 = ["m","eɪ","k","ʃ","ɔː","t","ə","p","r","əʊ","ʧ"]
pstring6 = ["m","eɪ","d","eɪ","m","eɪ","d","eɪ","m","eɪ","d","eɪ"]
pstring7 = ["m","ɪ","s","t","ə","p","r","əʊ","ʧ"]
pstring8 = ["n","ɛ","g","ə","t","ɪ","v","k","ɒ","n","t","æ","k","t"] 
pstring9 = ["r","iː","d","b","æ","k"]
pstring10 = ["r","ɪ","k","w","ɛ","s","t","f","ʊ","l","r","uː","t","k","ɪə","r","ə","n","s"]

#All sentences are combined in a single list.
pstrings= [pstring1,pstring2,pstring3,pstring4,pstring5,pstring6,pstring7,pstring8,pstring9,pstring10]

#A function that removes characters from a string that occur more than once.
def Remove(characterlist):
    new_string = []
    for character in characterlist:
        if character not in new_string:
            new_string.append(character)
    return new_string

#Every string consists of unique characters.
goodstring1 = Remove(pstring1)
goodstring2 = Remove(pstring2)
goodstring3 = Remove(pstring3)
goodstring4 = Remove(pstring4)
goodstring5 = Remove(pstring5)
goodstring6 = Remove(pstring6)
goodstring7 = Remove(pstring7)
goodstring8 = Remove(pstring8)
goodstring9 = Remove(pstring9)
goodstring10 = Remove(pstring10)

goodstrings = [goodstring1,goodstring2,goodstring3,goodstring4,goodstring5,goodstring6,goodstring7,goodstring8,goodstring9,goodstring10]

'''
All strings are compared to one another.
This is done by checking whether a character from one list occurs in the other string.
If this is the case, the similarity is counted and recorded in the comparison table.
'''
comparisontable = []
for goodstring in goodstrings:
    countertable = []
    for goodstringcomp in goodstrings:
        n = 0
        if goodstring != goodstringcomp:
            for letter in goodstring:
                if letter in goodstringcomp:
                    n += 1
        countertable.append(n)
    comparisontable.append(countertable)

#The number of similarities are divided by the length of the particular string and expressed in a percentage.
for comparisonlist in comparisontable:
    for i in range(len(comparisonlist)):
        comparisonlist[i] = round(100*comparisonlist[i]/len(pstrings[comparisontable.index(comparisonlist)]),2)
matrix = np.array(comparisontable)
print("The following table expresses the similarities between strings in a percentage.")
print("Each row corresponds to a string that is being compared to another string that is expressed by a column.\n")
print(matrix,"\n")

#For each string comparison their is a pair that includes their respective similarities.
pairs = []
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if row != column and row > column:
            a = matrix[row][column]
            b = matrix[column][row]
            pairs.append([a,b])


#For each pair the average is taken, since the highest average results in the most similarities.
averages = []
for pair in pairs:
    avg = (pair[0]+pair[1])/2
    averages.append(round(avg,2))

#The averages are sorted and the indices of the top 3 maximum averages are retrieved.
arr= np.array(averages)
indices = arr.argsort()[-3:][::-1].tolist()

#Each pair that is in the top 3 is found based on the indices.
maxpairs =[]
for index in indices:
    maxpairs.append(pairs[index])

#The position of the values of the pairs, which corresponds to the strings that were compared, are found in the matrix.
matrixposition = []
for pair in maxpairs:
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == pair[1] and matrix[column][row] == pair[0]:
                matrixposition.append([row+1,column+1])
print(matrixposition)

print("Therefore, the strings that are most prone to misunderstanding are: 2, 5 & 7.")




