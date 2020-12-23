# -*- coding: utf-8 -*-
"""
This module compiles the defined test case model into an FMU using the
overwrite block parser.

The following libraries must be on the MODELICAPATH:

- Modelica IBPSA
- Modelica Buildings

"""
# import numerical package
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
# import fmu package
from pyfmi import load_fmu
from pymodelica import compile_fmu
# import buildingspy
#from buildingspy.io.outputfile import Reader
#import fncs

# load pickle to save results - cannot be picked FMU2ME object
# import pickle
import os


# simulate setup
startTime = 0
dt = 60.

## load fmu - cs
library='example.mo'
model = 'example'
name = compile_fmu(model,[library], jvm_args='-Xmx1g', target='cs', version='2.0', compile_to='example.fmu')
fmu = load_fmu(name)
options = fmu.simulate_options()
options['ncp'] = 500

# initialize output
x = []
tim = []

# input: None

# simulate fmu
#res = fmu.simulate(start_time=startTime, final_time=endTime,input = input_object, options=options)

# simulate fmu using do_step to see if states are stored in fmu
initialize = True
a_ove_activate = False

for i in range(3):
    ts = i*dt
    options['initialize'] = initialize    
    # set time varying parameters
    a_ove = i+1
    fmu.set(['a_ove','a_ove_activate'], [a_ove, a_ove_activate])

    # has to use 3600. instead of 3600, because the former will produce a float number to avoid integrator errors in jmodelica. 
    res_step = fmu.simulate(start_time=ts, final_time=ts+dt, options=options)
    initialize = False
    a_ove_activate = True

    print(len(res_step['eqn.x']))
    print(res_step['eqn.x'])
    print(res_step['time'])

    x.extend(res_step['eqn.x'])
    tim.extend(res_step['time'])


print('Finish simulation')

# post-process
# plot 
fig = plt.figure()
fig.add_subplot(111)
plt.plot(np.array(tim),np.array(x))
plt.savefig('result.pdf')
plt.close()	



