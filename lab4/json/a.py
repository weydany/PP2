import json

with open('sample_data.json', 'r') as file:
    data = json.load(file)

print('Interface Status')
print('=======================================================================================')
print('DN                                                 Description           Speed   MTU   ')
print('-------------------------------------------------- --------------------  ------  ------')

for d in data['imdata']:
    dn = d['l1PhysIf']['attributes']['dn']
    print(dn, ' '*(50 - len(dn)), end='')

    desc = d['l1PhysIf']['attributes']['descr']
    print(desc, ' '*(20 - len(desc)), end=' ')

    speed = d['l1PhysIf']['attributes']['speed']
    print(speed, ' '*(6 - len(speed)), end=' ')

    mtu = d['l1PhysIf']['attributes']['mtu']
    print(mtu, ' '*(6 - len(mtu)))