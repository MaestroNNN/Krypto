# input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# output = 'DEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABC'
# smeshenie = 0
# itog = ''

# def analyz():
#     global itog
#     for i in input:
#         mesto = input.find(i)
#         new_mesto = mesto + smeshenie
#         itog += input[new_mesto]
#     print(itog) 

# while itog != output:
#     analyz()
#     if itog == output:
#         print("Ключ равен", smeshenie)
#     else:
#         smeshenie += 1
#         itog = ''


smeshenie = 0
itog = ''

def analyz(input_text):
    global itog
    for i in input_text:
        mesto = input_text.find(i)
        new_mesto = (mesto + smeshenie) % len(input_text) 
        itog += input_text[new_mesto]
    # print(itog) 

with open('input.txt', 'r') as input_file:
    input_text = input_file.read()

with open('output.txt', 'r') as output_file:
    output_text = output_file.read()

while itog != output_text:
    analyz(input_text)
    if itog == output_text:
        print("Ключ равен", smeshenie)
    else:
        smeshenie += 1
        itog = ''
