def temp_conv(c):
    return 9/5 * c + 32

cel = [33.4,35.5,32.1,36.5,37.8,34.7]

f = []

for temp in cel:
##    print(temp_conv(temp))
    f.append(temp_conv(temp))
    #print(f)

#map(function_name, iterable)
#f_list = list(map(temp_conv, cel))
#print(f_list)

f_list = list(map(lambda c: 9/5 *c + 32, [33.4,35.5,32.1,36.5,37.8,34.7]))
print(f_list)
