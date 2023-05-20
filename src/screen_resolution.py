# 16:9
# (#1) 1920x1080
# (#2) 1536x864
# (#3) 1280x720

# 16:9*120 = 1920x1080    
# 16:9*96  = 1536x864  # NOTE: height % 16 == 0  # 96x54 tiles @ 16x16px
# 16:9*90  = 1440x810  # NOTE: max windowed resolution on laptop
# 16:9*80  = 1280x720  # NOTE: height % 16 == 0  # 80x45 tiles in map
# 16:9*60  = 960x540

def print_16_9_dimensions_scaled(n):
    width = 16 * n
    height = 9 * n
    info = '16:9 * ' + str(n) + ': ' + str(width) + 'x' + str(height)
    print(info)

for i in range(10, 150, 10):
    print_16_9_dimensions_scaled(i)
print()  # skip a line

for i in range(16, 150, 16):
    print_16_9_dimensions_scaled(i)
print()

print('864 / 16: ' + str(864 / 16))
print('810 / 16: ' + str(810 / 16))
print('720 / 16: ' + str(720 / 16))
print()

print('1536x864 / 16: ' +  str(1536//16) + 'x' + str(864//16))
print('1280x720 / 16: ' +  str(1280//16) + 'x' + str(720//16))
print()
