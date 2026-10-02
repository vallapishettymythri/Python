#netflix- enjoy the netflix- free and premium user
def premium(func):
    def wrapper(user):
        if user["plan"]=="premium":
            print("enjoy your netflix")
        else:
            print("upgrade your plan")
    return wrapper
@premium
def netflix_user(user):
    print("enjoy your netflix")

user1={"name":"abc","plan":"free"}
user2={"name":"pqr","plan":"premium"}
netflix_user(user1)