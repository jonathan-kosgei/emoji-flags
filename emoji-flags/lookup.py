from .data import flags

data = {}
for flag in flags:
    data[flag['code']] = flag['emoji']

def lookup(country_code):
    if country_code in data:
        return data[country_code]
    return None
