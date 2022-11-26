from .data import flags

data = {}
reverse_data = {}

for flag in flags:
    data[flag['code']] = flag['emoji']
    reverse_data[str(flag['emoji'])] = flag['code']

def lookup(country_code):
    if country_code in data:
        return data[country_code]
    return None

def reverse_lookup(emoji):
    if emoji in reverse_data:
        return reverse_data[emoji]
    return None

