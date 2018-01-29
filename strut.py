from struct import *

packedData= pack('iif',33,83,4.73)
print(packedData)

originalData = unpack('iif',packedData)
print(originalData)
