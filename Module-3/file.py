# .CSV - Comma Separated Value

# with open('message.txt','w') as file:
#      file.write('i love python!')

# with open('message.txt','a') as file:
#     file.write('i love python!')

with open('message.txt','r') as file:
    text = file.read()
    print(text)