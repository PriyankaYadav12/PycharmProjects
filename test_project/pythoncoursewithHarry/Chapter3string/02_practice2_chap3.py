name = input("enter the name:")
date = input("enter the date:")
template = '''
Dear <|name|>,
you are selected
<|date|>

'''
print(template.replace('<|name|>', name).replace('<|date|>',date))
