# File handling
file_handler = open("SampleTestFile.txt", "r")
print(file_handler)
for i in file_handler:
    print(i)

# ----------------------------------------------------------------------------------------------------------------------

# other ways
file_handler = open("SampleTestFile.txt", "r")
read_file = file_handler.read()
print(read_file)
# Recommended to enclose open() function with try-except to contain "File not found exception"

# ----------------------------------------------------------------------------------------------------------------------

# Lists in python
sample_list = ['A', 'b', 'c', 'd', 'e', 'f', 'a']
for element in sample_list:
    print(element)

sample_list.sort()
print(sample_list)

date = "12/03/1996"
spe = date.split("/")
print(spe[1])

# ----------------------------------------------------------------------------------------------------------------------

# Sorting a tuple in terms of value.
my_dict = {
    "k1": 1,
    "k2": 10
}
my_dict["k3"] = 0
print(sorted(((k, v) for k, v in my_dict.items()), reverse=False))

# ---------------------------------------------End of Course 2----------------------------------------------------------
