CODE_TABLE = [['А', 'Б', 'В', 'Г', 'Д', '', ''], ['0', '00', '1', '11', '000', '', '']
              ]


code_line = '00110101'
text_line = ''
it_coding = True
i = 0
t = ''
while i < len(code_line):
    t += code_line[i]
    if t in CODE_TABLE[1]:
        text_line += CODE_TABLE[0][CODE_TABLE[1].index(t)]
    else:
        i += 1
print(text_line)


