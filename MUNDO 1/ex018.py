import math

ang = int(input('\033[1;30mDigite um ângulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('\033[1;30mO seno, cosseno e a tangente do angulo {}° é:'.format(ang))
print(' ')
print('\033[1;30m-' * 20)
print('\033[1;36mSen{}° é {:.2f}'.format(ang, sen))
print('\033[1;36mCos{}° é {:.2f}'.format(ang, cos))
print('\033[1;36mTan{}° é {:.2f}'.format(ang, tan))
print('\033[1;30m-' * 20)
