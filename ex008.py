medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida * (1/1000)
print('A media de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))
print('e em {}km '.format(km))