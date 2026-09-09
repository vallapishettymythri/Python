#WAP to return count of vowels and consonants
def count(string):
    vowel=0
    cons=0
    for i in string:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            vowel+=1
        else:
            cons+=1
    return vowel,cons
string="this is python"
count(string)