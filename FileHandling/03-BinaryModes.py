# image_1 = open('Football.png', 'rb')
image_2 = open('download_1.jpg','rb')

# data_1 = image_1.read()
data_2 = image_2.read()

# print(data)

result = open('image_1.jpg','ab')
# result.write(data_1)
result.write(data_2)

# image_1.close()
image_2.close()
result.close()