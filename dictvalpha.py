#String vowel and consonant list in dict
def strdict(str):
    result={
        "vowel":[],
        "consonant":[]
    }
    for i in str:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':       #if i in ["a","e","i","o","u"]:
            result["vowel"].append(i)
        else:
            result["consonant"].append(i)
    return result
str="jai shree mahakal"
strdict(str)