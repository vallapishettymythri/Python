#split()
dict={
     "subjects": "maths,english,physics"
}
lst=dict["subjects"].split(",")
new_dict={
    "subject1":lst[0],
    "subject2":lst[1],
    "subject3":lst[2]
}
print(new_dict)



#Clear()-
dict={
    0:1,
    1:2,
    2:3,
    3:4
}
dict.clear()
dict