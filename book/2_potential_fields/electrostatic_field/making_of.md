# Making Of

The figures collected here support the preceding conceptual development while keeping the main chapter focused on the physics and mathematics.

## Computed field figures

The Python script {download}`plot_electrostatic_fields.py` generates both {numref}`electric-dipole-field` and {numref}`cloud-ground-field`. It evaluates the potentials and fields from the point-charge expressions, then draws equipotential contours and streamlines. The common multiplicative factor $1/(4\pi\epsilon_0)$ is omitted because it changes the numerical scale but not the geometry.

Run the script from this directory with

```bash
python plot_electrostatic_fields.py
```

## Editable conceptual figures

The following SVG files are deliberately constructed from simple labelled shapes and paths so that they can be adjusted in Inkscape or another vector editor:

- {download}`figures/gravity_electric_flux_comparison.svg`
- {download}`figures/source_and_test_charge.svg`
- {download}`figures/conductor_redistribution.svg`

Their captions and surrounding text contain the physical interpretation; the diagrams are kept visually economical so their geometry remains easy to modify.
