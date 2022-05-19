#basic string methods
a = '  Vaibhav  '
b = 'blayer'

a.strip() #trims spaces-bothsides
a.lstrip() #trims spaces from left
a.rstrip() #trims spaces from right

b.title() #capitalize the first letter
b.upper() #capitalize whole string
b.lower() #decapitalize whole string

a.strip().upper() #trims then capitalizes

# join accepts a list of string
# and joins them in order
f_name = a.strip().title()
l_name = b.strip().title()
full_name = ''.join([f_name, ' ', l_name])
