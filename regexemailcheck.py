#wap to emails checking
import re

def valid_emails(email):
    pattern = "[a-z0-9]+@[a-z]+\.[a-z]+"
    match = re.fullmatch(pattern, email)
    if match:
        return True
    else:
        return False

emails = ["abc123@gmail.com", "@abc@gmail.com", "abc345@gmail",
          "abc123@hotmail.com", "a@bc.com"]

result = []

for email in emails:
    r = valid_emails(email)
    result.append(r)

print(result)