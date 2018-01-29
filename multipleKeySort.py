from operator import itemgetter

users = [
{'fname': 'Ashmin', 'lname': 'Kharel'},
{'fname': 'Erika', 'lname': 'Perfect'},
{'fname': 'Rebecca', 'lname': 'Cutie'},
{'fname': 'Emma', 'lname': 'Whore'},
]

for x in sorted(users, key =itemgetter)