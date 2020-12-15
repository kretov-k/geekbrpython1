from sys import argv

script_name, a, b, c = argv


def zar(a, b, c):
    z = a * b + c
    return z


a, b, c = int(a), int(b), int(c)
print("Your salary is:")
print(zar(a, b, c))

# can't type russian here. If any russian symbols appear - syntaxerror. The other strange thing is syntax error
# if I do print(f"some text {zar(a, b, c)}").
