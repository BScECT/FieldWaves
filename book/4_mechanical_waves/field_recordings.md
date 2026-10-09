# Seismic wavefield recordings from the field: physical interpretation using kinematic concepts

In this section, we will look at the physical interpretation of seismic wavefield data as recorded in the field, two recordings on land (one with rocky near-surface and one with loose-soil near-surface) and one recording at sea.

## Seismic wavefield recording on land: rocky near-surface

Let us first consider a seismic wave field recorded on land. In {numref}`fig-raw-shot-land` this wavefield record is shown. The first event we are considering is the "first arrival". It shows itself by giving a pulse after a quiet period. This arrival can be a *direct* arrival or a *refraction*, both of which we discussed earlier. When looking closely at the record, it can be seen that there is a slight change of dip, occurring at around an offset of 800 m. Therefore, the arrival until this distance is a direct arrival, while beyond that distance, it is the refraction. By drawing a straight line through the direct arrival, the velocity with which it propagates along the surface is: 2400 meters in 670 ms, so approximately 3600 m/s. This is a relatively high velocity, so there is probably some very hard rock at the surface. The velocity of the refracted arrival can also be determined by a straight line through that arrival; it amounts to 2400 meters in around 500 ms (note that the arrival does not go through the origin, so it is the difference between the time at $x=0$ m and at $x=2400$ m), so a velocity of 4800 m/s. Below the record in {numref}`fig-raw-shot-land`, a simple model is shown that explains this first arrival; the synthetic record belonging to this model is given on the top right of the figure.

The next events we consider are the strong events that cross 2400 meter at some 1.3 seconds. This event is interpreted as ground-roll or surface waves (they propagate along the surface). Calculating the velocity, we come to 1850 m/s. Again, the simple model below the record explains this ground roll; the synthetic record on the top right of the figure also shows this arrival.

```{figure} figures/Figure4_1.PNG
:name: fig-raw-shot-land
:width: 100%

Field seismic wavefield recording from land survey (top left), synthetic seismogram (top right) using model of near surface (middle) and model at larger depths (bottom).
```

Also in this field record, a "high-frequency" event can be observed, which goes through the 4-second mark at about 1300 meters distance. Calculating the velocity from this, we come to some 325 m/s. It may be clear that this is a wave that goes through the air. This event is also synthesized in the top right figure, using the model as given below it.

Last but not least, are "high-frequency" events which are slightly curved, e.g. the ones at 0.9 and 1.6 seconds. These events are interpreted as reflections from layer boundaries in the deep subsurface. Those are usually the events we are interested in when we want to obtain an image of the subsurface. Using a simple model as given at the bottom of the figure (which explains the deeper part of the earth), the synthetic record for these events is also shown in the top right of the figure.

In the above, we have interpreted five types of events, which can be captured in one combined model and are shown in one combined synthetic seismogram. These synthetics explain the most important events in the raw seismic record. Still, when looking at the resulting synthetic seismogram, we see that we are very over-simplifying the situation, since the synthetic and field record are only resembling in the arrival times of the most important events. When looking at the general characteristics, they are very different indeed.

## Seismic wavefield recording on land: loose-soil near-surface

The field record we discussed so far was recorded on some hard rocks where the velocities are relatively high. However, when shooting data on land with loose top soil, in this case sand on a beach, the characteristics are much different. In {numref}`fig-raw-shot-wassenaar`, a field record of this situation is given. Again, we can determine the main events in this record. Let us first consider the "first arrival", i.e. the arrival that is coming in first after a quiet period. As usual, this is interpreted as a refraction, as shown in the figure below the record. The velocity can be determined: we come to some 1600 m/s. This velocity is very close to the velocity of water, so this refraction may be due to the water table. In the figure on the right, the synthetic shows this arrival.

The next event is the most prominent one, namely the event that goes through the 1-second mark at some 180 m, so its velocity is around 180 m/s. This arrival is interpreted as "ground-roll"/surface waves, which travel along the surface. The model which explains this arrival is given again below the record, and its synthetic is shown on the top right.

The most important events for this wavefield recording are the "high-frequency" events that are the slightly curved arrivals, which can all be interpreted as reflections from deep layers. The number of reflections are too many; only a few are synthesized in the record on the top right, using the model as given at the bottom of the figure.

Again, when comparing the synthetic to the field seismogram, it is obvious that we have very over-simplified the earth; the positive side is that we have probably been able to understand most of the events in the field recording.

```{figure} figures/Figure4_2.PNG
:name: fig-raw-shot-wassenaar
:width: 100%

Field seismic wavefield recording from land survey with loose top soil (top left), synthetic seismogram (top right) using model of near surface (middle) and model at larger depths (bottom).
```

## Seismic wavefield recording at sea

{numref}`fig-raw-shot-marine` shows a seismic wavefield recording, made at sea. This record is much "cleaner" than the land record, as we measure in a water layer, which is a very homogeneous layer.

Let us analyze some separate events again. The first event in the marine record is the faint one, going nearly through the origin. It crosses the 500 meter at some 340 ms; this means a velocity of some 1470 m/s. It may be clear that this is the direct arrival from the source to the receivers through the water, as explained in the model below the record. This direct arrival is thus a body wave, since it travels with the velocity of water.

The next event is the first arrival at farther offsets; this arrival is interpreted as a refractive event. When analyzing the distance travelled over time, i.e. the apparent velocity, a velocity of roughly 2000 m/s is obtained. Using the equation for a refraction ({eq}`eq:trefract`), a depth of 300 meter is obtained. This is quantified in the model below the figure, and its associated synthetic seismogram in the figure on the top right.

The third event we analyze is the first strong event that looks hyperbolic: starting at some 0.4 seconds and bending down to some 2.2 seconds at 3200 m offset. Clearly, because of its hyperbolic behaviour, it is interpreted as a reflection. When looking at later times, we have some more strong hyperbolic events, such as at 0.8 seconds (bending downward toward some 2.3 seconds), and at 1.2 seconds (bending downward toward 2.4 seconds), and even more. These events are interpreted as so-called multiply reflected waves, i.e., waves that bounce up and down in the water layer. In fact almost all events we see below 0.8 seconds are due to multiply reflected waves, or short-hand: multiples. The times at which the multiply reflected waves arrive seem to be periodic; this is indeed the case.

Combining the interpretation of the refraction and the reflection, it must be noted that the refracted arrival does not converge to the first reflection but to a later reflection. This means that the refraction occurs at a deeper layer; the shallower layers are probably loosely consolidated, so that the velocity of sound has not changed much compared to the one from water.

A simple model explaining all these events is shown in the figure below the record, with a water layer of 300 meter. The refracted layer is estimated at a depth of 550 meter, where we assumed that the velocity was a constant of 1500 m/s above. The resulting synthetic seismogram is shown in the top right of the figure. It may be clear that the multiply reflected waves come from the same reflective boundary in the subsurface, namely, the sea bottom (and the sea surface, of course), and are therefore superfluous. They are considered as noise; the only one being "signal" is the one at around 0.4 seconds.

```{figure} figures/Figure4_3.PNG
:name: fig-raw-shot-marine
:width: 100%

Seismic wavefield recording from marine survey (top left), synthetic seismogram (top right) using model of water layer and sea-water bottom, where only the path of one multiple reflection is drawn (bottom).
```
