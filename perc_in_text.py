def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

file = open("newfile.txt", "w")
file.write("""The field_name itself begins with an arg_name that is either a number or a keyword. 
If it’s a number, it refers to a positional argument, and if it’s a keyword, it refers to a named keyword argument. 
If the numerical arg_names in a format string are 0, 1, 2, … in sequence, they can all be omitted (not just some) 
and the numbers 0, 1, 2, … will be automatically inserted in that order. Because arg_name is not quote-delimited, 
it is not possible to specify arbitrary dictionary keys (e.g., the strings '10' or ':-]') within a format string. 
The arg_name can be followed by any number of index or attribute expressions. 
An expression of the form '.name' selects the named attribute using getattr(), 
while an expression of the form '[index]' does an index lookup using __getitem__().

""")
file.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxzy":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))