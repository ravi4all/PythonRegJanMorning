def fileHandling():
    try:
        file = open('file_1.txt')
        data = file.read()
        print(data)

        x = {"data" : data}

        file_1 = open('file_2.txt', 'w')
        file_1.write(x)
        print("File written successfully")

    except (TypeError,FileNotFoundError) as error:
        # print(error)
        if TypeError:
            print("Only strings are allowed")
        elif FileNotFoundError:
            print("File not found")

    finally:
        print("File closed...")
        file.close()
        file_1.close()

fileHandling()