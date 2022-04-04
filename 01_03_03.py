#for loop
sisters = ('onyi','nenye','chidinm','uche','nazo')

# for sister in sisters:
#     print(sister)

# for sister in sisters[0:4]:
#     print(sister)

for sister in sisters:
    if sister == 'onyi':
        print(f'{sister} - LOLM')
    elif sister == 'nenye':
        print(f'{sister} - dark slim sheddy')
        break    
    elif sister == 'chidinm':
        print(f'{sister} - First born')
    else:
        print(f'{sister} - younger than me')        