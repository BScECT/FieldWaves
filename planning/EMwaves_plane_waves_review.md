# Plane-wave draft — joint review

First draft: 2026-11-08. Book source: `book/5_electromagnetic_waves/plane_waves_1d.md`.

## Review in small passes

1. **Opening through “Follow a feature, not a fixed position”.** Is the chain-rule calculation at the right level? Does the constant argument explain motion clearly enough? Ask the reviewer to explain why the minus sign means forward propagation before moving on.
2. **H, field directions and finite travel time.** Does the full Cartesian curl help retrieve earlier knowledge, or need more guidance? Decide whether the central coupled equations should remain inside the expandable check or be visible immediately afterwards. Check the balance between physical explanation and calculation.
3. **Spatial frequency and complex fields.** Is the analogy between ω and k convincing? Is the distinction between complex full fields and phasors clear without tildes? Ask the reviewer to explain one delay-to-phase conversion.
4. **Telegrapher’s equations.** Is the parallel-plate derivation a manageable ending, or should part be optional? It is deliberately a bridge, not a second circuit course.

Begin with pass 1 rather than asking for general approval of the whole section.

## Figures and Python

Three reproducible figures: a travelling pulse, time versus spatial frequency, and a parallel-plate cross-section. Generator: `book/5_electromagnetic_waves/scripts/plot_plane_waves.py`.

The two activities are embedded directly in the chapter at the relevant prompts. They follow the existing potential-fields pattern: Python generates self-contained HTML/JavaScript displays, and the controls run in the reader’s browser on the static book host. There is no notebook download, local-Jupyter step, external plotting service or live kernel requirement. Regenerate with `python book/5_electromagnetic_waves/scripts/build_plane_wave_interactives.py`.

The activities track a marked pulse feature versus a fixed sensor, and link temporal/spatial frequency with fixed axes. Both start with predictions. The asymmetric pulse makes the spatial/time-profile reversal visible. The raw HTML fragments embed the complete activity through sandboxed iframe srcdoc, so the book build does not depend on separate HTML asset deployment.

A later, optional activity could show radar range versus complex round-trip phase. Keep target scattering fixed and distinguish unwrapped phase from its value modulo 2π.

## Validation

The chapter builds successfully. Both embedded activities were inspected in the actual book page in a browser: changing time and sensor position updates the pulse plots and constant-argument readout; changing frequency and phase updates the harmonic plots, wavelength and wavenumber. The browser readout at 200 MHz gives λ=1.50 m and k=4.189 rad/m. A screenshot of the embedded pulse activity is saved with the chat outputs. The earlier notebook implementation was archived in the chat work directory and removed from the book. The analytical checks for propagation signs, waveform reversal and frequency/wavelength relations remain applicable.

## Preserve review edits

The chat review copy is independently editable. If Paco edits that copy, merge those changes deliberately into the book source. Do not regenerate or overwrite the review copy from the book. Back up both before merging. The initial matching source and review snapshot are kept in this chat’s work directory.
