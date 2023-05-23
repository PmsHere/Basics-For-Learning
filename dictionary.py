# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']

states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

# user = ['Mattan', 70, 10.5, 'Brown', 'Brown']
user = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

If you try to access something that isn't in the dictionary, you'll get a key error. And if you ever get confused about what something is - a dictionary or a list - you can always use the type() function. 

You can search for things in dictionaries using .get(). It lets you look something up without returning a key error. 

You're also able to get all the keys in a given dictionary by printing .keys()
