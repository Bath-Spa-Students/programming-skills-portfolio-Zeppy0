glossary = {
    'variable': 'set point for value',
    'string': 'character',
    'list': 'Collection of primary sequence',
    'tuple': 'Immutable Character',
    'Dictionary': 'Collection of key-value pairs',
}
for key,value in glossary.items(): 
    print("{key.title()}: {value}")

glossary['loop'] = 'A method to iterate through collections'
glossary['function'] = 'A piece of code that performs a specific function'
glossary['class'] = 'Creative design'
glossary['module'] = 'File containing Python code'
glossary['package'] = 'Package module' 
print(glossary)