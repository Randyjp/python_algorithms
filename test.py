s = '4H71NP35P2",""'
extra = 'something'
sp = s.split('"')

result = '{}","{}'.format(sp[0], extra)

print(result)