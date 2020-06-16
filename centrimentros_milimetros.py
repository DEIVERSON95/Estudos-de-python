medida = float(input('Digite uma medida: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
m = medida * 1
cm = medida * 100
mm = medida * 1000
print(' A medida de {:.0f} metros corresponde a {} em km \n A medida de {:.0f} metros corresponde a {} em hm \n A medida {:.0f} metros corresponde a {} em dam \n A medida {:.0f} metros corresponde a {} em dm \n A medida {:.0f} corresponde a {} em m \n A medida de {:.0f} metros corresponde a {} em centrimetros \n A medida de {:.0f} metros corresponde a {} em milimetros '.format(medida, km, medida, hm, medida, dam, medida, dm, medida, m, medida, cm, medida, mm))