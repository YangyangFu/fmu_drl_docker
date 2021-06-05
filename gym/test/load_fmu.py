from pyfmi import load_fmu

fmu = load_fmu('ModelicaGym_CartPole.fmu')
print(fmu)

fmu.set('f',1)
res=fmu.simulate(0., 1.0)
print(res['f'])
print(res['time'])