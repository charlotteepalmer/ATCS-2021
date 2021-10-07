mountains = {'Mount Everest': 29029, 'Makalu': 27838, 'Annapurna': 26545}
for key in mountains.keys():
    print('Key %s' % key)
for value in mountains.values():
    print('Value: %s' % value)
for key, value in mountains.items():
    print(key, "is", value, "feet tall")