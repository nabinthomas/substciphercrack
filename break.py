""" 
Breaking Simple Susbtitution Cipher 

General Algorithm
1. Read Input String (Cipher Text)
2. Prepare the Frequency Map for each letter in the cipher text
3. Sort the map based on the frequency.
4. Map each letter to the corresponding letter from the Standard Frequency Map.
5. Print the decoded message
6. (Manually) try to read the message and fix errors.

"""

import operator
import collections
import sys


sampleCipherText = "PBFPVYFBQXZTYFPBFEQJHDXXQVAPTPQJKTOYQWIPBVWLXTOXBTFXQWAXBVCXQWAXFQJVWLEQNTOZQGGQLFXQWAKVWLXQWAEBIPBFXFQVXGTVJVWLBTPQWAEBFPBFHCVLXBQUFEVWLXGDPEQVPQGVPPBFTIXPFHXZHVFAGFOTHFEFBQUFTDHZBQPOTHXTYFTODXQHFTDPTOGHFQPBQWAQJJTODXQHFOQPWTBDHHIXQVAPBFZQHCFWPFHPBFIPBQWKFABVYYDZBOTHPBQPQJTQOTOGHFQAPBFEQJHDXXQVAVXEBQPEFZBVFOJIWFFACFCCFHQWAUVWFLQHGFXVAFXQHFUFHILTTAVWAFFAWTEVOITDHFHFQAITIXPFHXAFQHEFZQWGFLVWPTOFFA";
debugEnabled = True;

def debugPrint (*args):
    if (debugEnabled == True):
        print (args);

def prepareStandardFrequencyMap():
    standardFrequencyOrder = "etaoinshrdlcumwfgypbvkjxqz".upper();
    numLetters = len(standardFrequencyOrder);
    if (numLetters != 26):
        print ("Something is off. Not all letters are in ", standardFrequencyOrder);
        exit(-1);
    
    debugPrint ("Using Frequency Ordering : ", standardFrequencyOrder);

    standardFrequencyMap = standardFrequencyOrder;
    return standardFrequencyMap;

def prepareFrequencyMap(cipherText):
    frequencyMap = dict();
    
    for index in range (0, 26):
        frequencyMap[chr(ord('A') + index)] = 0;
    
    for index in range(0, len(cipherText)):
        char = cipherText[index];
        frequencyMap[char] = frequencyMap[char] + 1;
    
    debugPrint (frequencyMap)
    return frequencyMap;

def sortFrequencyMap(frequencyMap):
    sortedMap = collections.OrderedDict(sorted(frequencyMap.items(), key=operator.itemgetter(1), reverse=True))
    debugPrint (sortedMap);
    return sortedMap;

def createDecryptionMap(sortedFrequencyMap, standardFrequencyMap):
    for letter, frequency in sortedFrequencyMap.items():
        print(letter, " ==> ", frequency);

    # Mapping
    index = 0;
    decryptionMap = dict();
    for letter, frequency in sortedFrequencyMap.items():
        decryptionMap[letter] = standardFrequencyMap [index];
        print(letter, standardFrequencyMap [index])
        index = index + 1;
    
    return decryptionMap;
    
def doDecrypt(decryptionMap, cipherText):
    for char in cipherText:
        print (char, end='');
    print("\n");
    for char in cipherText:
        print (decryptionMap[char], end='');
    print ("\n");
    
def runDecrypt(cipherText):
    standardFrequencyMap = prepareStandardFrequencyMap();
    frequencyMap = prepareFrequencyMap(cipherText);
    sortedFrequencyMap = sortFrequencyMap(frequencyMap);
    decryptionMap = createDecryptionMap(sortedFrequencyMap, standardFrequencyMap);
    doDecrypt(decryptionMap, cipherText);

if __name__ == '__main__':
    runDecrypt(sampleCipherText);
    if (len (sys.argv) > 1):
        runDecrypt(sys.argv[1]);