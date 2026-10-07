---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
mystnb:
  # The cells are to be filled in and run by the reader, so the page must not be
  # executed at build time.
  execution_mode: 'off'
---

# Exercise 4a: Model traveltimes for seismic wavefield from one shot

In this exercise you will model the traveltimes of a seismic wavefield for a direct, refracted and reflected wave. The model contains only one boundary, giving rise to a reflection and a head wave (a critically refracted wave) when the wave speed of the second medium is higher than the wave speed of the first medium.

To this aim, we will use a synthetically generated wave field for one shot position. Sixteen (0-15) wave-field recordings are present:

- Take the first character of your first name, take the number of this character in the alphabet and if it is larger than 15, subtract 15.
- Make this your group number as a string variable.

```{code-cell} ipython3
your_group_no = ""
```

```{code-cell} ipython3
# Housekeeping, no physics. Running this page in the browser, the next lines fetch
# your own shot gather from the book. Running the notebook on your own machine, with
# the .npz file already beside it, they do nothing.
import os
import pathlib

filename_npz = "shot_group_" + your_group_no + ".npz"

if not pathlib.Path(filename_npz).exists():
    from pyodide.http import pyfetch
    # Live Code runs Python in a worker, which would resolve a plain "data/..."
    # against itself and not against this page. The working directory mirrors the
    # folder this page sits in on the server, so it gives the address to ask for.
    url = os.getcwd().split("/home/pyodide/book")[-1] + "/data/" + filename_npz
    response = await pyfetch(url)
    if response.status != 200:
        raise FileNotFoundError(
            url + " -> HTTP " + str(response.status)
            + ". Is your_group_no a number from 0 to 15?")
    pathlib.Path(filename_npz).write_bytes(await response.bytes())
    print("fetched", filename_npz)
```

Now you will read this wavefield data set, that includes the geometry of the data, so the positions of the source and receivers. To that end:

- Run the next code, and consider/analyze the source and receiver configuration.
- Where is the source positioned compared to the receiver positions (beginning, end, or somewhere else)?

```{code-cell} ipython3
#%matplotlib qt
%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np

# Reading NPZ file
filename_npz = "shot_group_" + your_group_no + ".npz"

with open(filename_npz, "rb") as f:
    npzfile     = np.load(f)                   ; print(npzfile.files)
    Data        = npzfile['Data']
    timevector  = npzfile['tt']
    x_receivers = npzfile['x_receivers']
    x_source    = npzfile['x_source']

# Check:
#print(Data[1,1])
#print(timevector[1])
#print(x_receivers[1])
#print(x_source)

plt.figure( figsize = ( 12, 6 ) )
plt.plot(x_receivers,'o',color='b')
plt.plot(x_source,'x',color='r', markersize=10)
plt.legend(['x_receivers','x_source'])
plt.xlabel('index'); plt.ylabel('Distance (m)')
plt.title(' Distance of source and receivers versus index of array', fontsize=14 )
plt.show()
```

Next, you need to generate the travel-time curves for that geometry. But, of course, you need to specify the parameters of the model, i.e., the velocities of the different waves and the depth of the boundary. The depth of the boundary may be different for the refractor and the reflector, but initially you can keep those depths the same. So to that end, using the variable names as set in the next code:

- Specify the P-wave velocities of the first and second medium, and the surface-wave velocity (of the first medium)
- Specify the depths of the refractor and reflector (initially, take them the same)
- Play with the velocities and depths such that you can see the different events in the travel-time curves, in particular that you can see both a reflection and a head wave (critically refracted wave)

```{code-cell} ipython3
# Specify velocities and depths
c_directP     =
c_directSurf  =
c_refract     =
depth_refract =
depth_reflect =
```

```{code-cell} ipython3
tt_directP    = np.zeros_like(x_receivers)
tt_directSurf = np.zeros_like(x_receivers)
tt_refract    = np.zeros_like(x_receivers)
tt_reflect    = np.zeros_like(x_receivers)

# direct P-wave:
tt_directP[:]    = abs(x_receivers[:]-x_source)/c_directP                         ; print('tt_directP    = ',tt_directP[0:3])

# direct Surface wave:
tt_directSurf[:] = abs(x_receivers[:]-x_source)/c_directSurf                      ; print('tt_directSurf = ',tt_directSurf[0:3])

# refracted P-wave:
sin_crit      = c_directP/c_refract
cos_crit      = np.sqrt(1-sin_crit*sin_crit)
tt_refract[:] = abs(x_receivers[:]-x_source)/c_refract + 2.0*depth_refract*cos_crit/c_directP ; print('tt_refract    = ',tt_refract[0:3])

# find limiting indices of array when distance < x_crit (then no critical refraction):
x_crit        = 2.0 * depth_refract * sin_crit/cos_crit    ; print('x_crit = ',x_crit,' m')
# left end:
i1     = 0
ii_end = len(x_receivers)      #; print('iiend  = ',ii_end)
for ii in range (0,len(x_receivers)):
    if abs(x_receivers[ii]-x_source) < x_crit:
        break
    else:
        i1 = ii
#print('i1 =',i1,';  x_receivers[i1] = ',x_receivers[i1])
#print('abs(x_receivers[i1]-x_source) = ',abs(x_receivers[i1]-x_source))

# right end:
i2     = len(x_receivers)
for ii in range (ii_end-1,0,-1):
    if abs(x_receivers[ii]-x_source) < x_crit:
        break
    else:
        i2 = ii
#print('i2 =',i2,';  x_receivers[i2] = ',x_receivers[i2])
#print('abs(x_receivers[i2]-x_source) = ',abs(x_receivers[i2]-x_source))


# reflected P-wave:
t0            = 2*depth_reflect/c_directP
tt_reflect[:] = np.sqrt(t0*t0 + (x_receivers[:]-x_source)*(x_receivers[:]-x_source)/(c_directP*c_directP))
print('tt_reflect     = ',tt_reflect[0:3])

plt.figure( figsize = ( 16, 12 ) )
plt.plot(x_receivers, tt_directP, 'x',color='b')
plt.plot(x_receivers, tt_directSurf, 'x',color='c')
plt.plot(x_receivers[0:i1], tt_refract[0:i1], 'x',color='g')
plt.plot(x_receivers[i2:-1], tt_refract[i2:-1], 'x',color='g')
plt.plot(x_receivers, tt_reflect, 'x',color='r')
plt.axis( [np.min(x_receivers), np.max(x_receivers), np.min(timevector), np.max(timevector)] )
plt.gca().invert_yaxis()
plt.legend(['directP','directSurf','refraction','','reflection'])
plt.show()
```
