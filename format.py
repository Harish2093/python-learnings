'''
Format function
'''

users = ['i', 'vp', 'bw']
devices = ['and', 'ios', 'win']

for user, device in zip(users, devices):
    template = "user {} uses device {}".format(user, device)
    print(template)
print('-'*80)
for user, device in zip(users, devices):
    template = "user {1} uses device {0}".format(user, device)
    print(template)