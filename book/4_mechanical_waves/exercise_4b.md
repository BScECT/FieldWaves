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

# Exercise 4b: Interpret velocities and depths from seismic wavefield from one shot

In this exercise you will interpret direct, refracted and reflected waves from a (synthetically generated) seismic wavefield recording. And will check the results via forward modelling, as you did in [Exercise 4a](./exercise_4a.md).

To this aim, use the same synthetically generated wave field that you used before:

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

Now you will read this wavefield data set, that includes the geometry of the data and data themselves. To that end:

- Run the next code, consider/analyze the source and receiver configuration again, and consider/analyze the wavefield data.
- In the code, the maximum amplitude (`maxAmplitude`) is set; adapt this maximum amplitude and look at the effect on the plot.

```{code-cell} ipython3
#%matplotlib qt
%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np

# Reading NPZ file
filename     = "shot_group_" + your_group_no
filename_npz = filename + ".npz"

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

# Plot geometry of shot gather
plt.figure( figsize = ( 12, 6 ) )
plt.plot(x_receivers,'o',color='b')
plt.plot(x_source,'x',color='r', markersize=10)
plt.legend(['x_receivers','x_source'])
plt.xlabel('index'); plt.ylabel('Distance (m)')
plt.title(' Distance of source and receivers versus index of array', fontsize=14 )
plt.show()

# Plot extracted shot gather
plt.figure( figsize = ( 16, 12 ) )
maxAmplitude = 0.04 * np.max( np.abs(Data) )
extent = [ np.min(x_receivers), np.max(x_receivers), np.max(timevector), np.min(timevector) ]
# Standard colormap:
# plt.imshow( Data, vmin=-maxAmplitude, vmax = maxAmplitude, extent = extent, aspect = 'auto' )
plt.imshow( Data, vmin=-maxAmplitude, vmax = maxAmplitude, extent = extent, aspect = 'auto', cmap='seismic' )
titleplot = filename + " : original"
plt.title(titleplot, fontsize=14 )
plt.colorbar()
plt.show()
```

## Identification of events

The figure of the wavefield data is a simulation of a seismic wavefield recording. On this wavefield recording, determine which event(s) can be interpreted as:

- Direct P-wave
- (Critically) refracted P-wave
- Direct surface wave
- P-wave reflections

You may have to play with `maxAmplitude` to see some events better.

## Estimation of wave velocity of events

Based on this identification, determine the velocity of the:

- Direct P-wave
- Head wave (Critically refracted P-wave)
- Direct surface wave

In order to estimate the velocity of a reflected wave, first consider the equation for a reflection-hyperbola, i.e.,

$$
T^2 = T_0^2 + \frac{X^2}{c^2},
$$

where $T_0$ is the time at the apex of the hyperbola, and $X$ is the horizontal distance from the apex, so the relative horizontal distance between the source and receiver. From this equation, the velocity can be made explicit:

$$
c = \frac{X}{\left( T^2 - T_0^2 \right)^{1/2}}.
$$

Based on this:

- Estimate the velocity from one of the reflections you picked above.

## Estimation of depth of refractor and reflector

Based on the above, depth estimates can be made. Let us first estimate the depth of the **refractor**, using the cross-over distance, the distance where the direct wave and the head-wave (critically refracted) cross each other. This is given by:

$$
Z_{\mathrm{refractor}} = \frac{X_{\mathrm{cross}}}{2}
      \left[ \frac{c_2-c_1}{c_2+c_1} \right]^{1/2},
$$

where $c_1$ is the velocity of the direct P-wave and $c_2$ the velocity of the (P-wave) refractor.

Based on this:

- Determine the depth of the refractor

Let us now consider the **reflection** you took. At a distance $X=0$, the reflection time becomes $T_0 = 2z/c_{\mathrm{refl}}$. That reflection time can be picked from the wavefield recording, and the velocity you estimated earlier. Then the depth can be determined via $z = c_{\mathrm{refl}} T_0 /2$.

Based on this:

- Determine the depth of the reflector

## Final check: forward model results via Exercise 4a

Based on the above, you have now determined all the velocities and depths for which you can model the travel times as you did in [Exercise 4a](./exercise_4a.md). So therefore:

- Run the travel-time code of Exercise 4a again, but now with the model parameters you estimated for your wavefield recording
- Check whether the travel times match the ones from your seismic wavefield recording above.

This should give you confidence in your physical interpretation of the wavefield recording.
