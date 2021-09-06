n = float(input('\033[1;36mDigite uma distancia em METROS:'))
km = n*(10**(-3))
hm = n*(10**(-2))
dam = n*(10**(-1))
dm = n*(10**1)
cm = n*(10**2)
mm = n*(10**3)
print('\033[1;30mA medida de {} metros corresponde a:'
      '\n\033[4;30m{}km\n{}hm\n{:.1f}dam\n{}dm\n{}cm\n{}mm.'.format(n, km, hm, dam, dm, cm, mm))
