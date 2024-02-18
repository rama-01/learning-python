# counter = 0
# a = 0
# b = 1
# while True:
#     print(b)
#     counter += 1
#     a, b = b, b + a
#     if counter >= 20:
#         break

# refactor code
count = 0
a, b = 0, 1
while count < 20:
    print(b)
    a, b = b, a + b
    count += 1
