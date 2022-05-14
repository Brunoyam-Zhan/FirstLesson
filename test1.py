
import json

# from pizzahub import menu
# f = open('test1.json', "w")
# a = json.dump(menu, f)

f = open('test1.json', "r")
a = json.load(f)
print(a)
print(type(a))
f.close()






# f = open('text.txt', 'w')
# f.write('New string')
# f.close()

# f = open('text.txt', 'r')
# print(f.readlines())
# f.close()


# f = open('text.txt', 'a')
# f.write('string')
# f.close()

# f = open('text.txt', 'w+t')
# f.write('New string')
# f.close()


