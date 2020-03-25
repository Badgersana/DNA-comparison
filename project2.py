#adds missing number of indels to end so both sequences are even in length #this works
def pad_with_indels(sequence, num):
    sequence = sequence + (num * '-')

    return sequence

#adds an indel at index, must change it from a position(1) to index (0) #this works
def insert_indel(sequence, index):
    if (index) == len(sequence) + 1:
        sequence = sequence + '-'
    else:
        sequence = sequence[:(index)] + '-' + sequence[index:]


    return sequence

#counts number of matches, ignores indels #this doesnt apparently
#changes matching chars to lowercase and calculates the percentage of matching characters
def count_matches(sequence1, sequence2):
    matches = 0
    mismatches = 0
    newSequence1 = ''
    newSequence2 = ''
    
    for i in range(len(sequence1)):
        if sequence1[i] == sequence2[i] and sequence1[i] != '-' and sequence2[i] != '-':
            matches += 1
            newSequence1 += sequence1[i].lower()
            newSequence2 += sequence2[i].lower()
            
        elif sequence1[i] != sequence2[i] or (sequence1[i] == '-' and sequence2[i] == '-'):
            newSequence1 += sequence1[i]
            newSequence2 += sequence2[i]
            mismatches += 1

    return newSequence1, newSequence2, matches, mismatches;
            
if __name__ == '__main__':

    sequence1 = input('Please enter DNA Sequence 1: ')
    sequence2 = input('\nPlease enter DNA Sequence 2: ')
    sequence2Spare = sequence2
    sequence1Spare = sequence1

    if len(sequence1) < len(sequence2):
        num = len(sequence2) - len(sequence1)
        sequence1 = pad_with_indels(sequence1, num)
        
    elif len(sequence2) < len(sequence1):
        num = len(sequence1) - len(sequence2)
        sequence2 = pad_with_indels(sequence2, num)
    

    sequence1, sequence2, matches, mismatches = count_matches(sequence1, sequence2)

    matchRate = (matches / (matches + mismatches)) * 100
    
    print(f'\nSequence 1: {sequence1}')
    print(f'\nSequence 2: {sequence2}')
    print(f'\nSimilarity: {matches} matches, {mismatches} mismatches. {matchRate:.1f}% match rate.')

    index = int(input('Please enter an indel location for Sequence 1: ')) - 1

    sequence1Spare = insert_indel(sequence1Spare, index)

    if len(sequence1Spare) < len(sequence2Spare):
        num = len(sequence2Spare) - len(sequence1Spare)
        sequence1Spare = pad_with_indels(sequence1Spare, num)
        
    elif len(sequence2Spare) < len(sequence1Spare):
        num = len(sequence1Spare) - len(sequence2Spare)
        sequence2Spare = pad_with_indels(sequence2Spare, num)

    sequence1Spare, sequence2Spare, matches, mismatches = count_matches(sequence1Spare, sequence2Spare)
    matchRate = (matches / (matches + mismatches)) * 100
    
    print(f'\nSequence 1: {sequence1Spare}')
    print(f'\nSequence 2: {sequence2Spare}')
    print(f'\nSimilarity: {matches} matches, {mismatches} mismatches. {matchRate:.1f}% match rate.')
