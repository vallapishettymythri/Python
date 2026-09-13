#urls
import re
urls = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://youtu.be/abc123XYZ",
    "https://www.youtube.com/watch?v=K4TOrB7at0Y",
    "https://youtu.be/X7aK8l9mN2Q",
    "https://www.youtube.com/watch?v=Python123",
]
pattern="\w+"
result=[]
for i in urls:
    ans=re.findall(pattern,i)
    result.append(ans[-1])
result