favorite_languages = {
    'sarah': 'c',
    'jim' : 'c#',
    'brian' : 'python'
}

# language = favorite_languages['brian'].title()
# print(f'Brians fav language is {language}.')
"""A for loop for extracting the key value pairs of the dictionary and formatting into a print statement"""
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}!")
"""Loops through just the key's values and not the value pair"""
for name in favorite_languages.keys():
    print(name.title())

