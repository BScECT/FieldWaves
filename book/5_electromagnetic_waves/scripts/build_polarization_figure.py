"""Annotate the copied PPEO plane-boundary drawing for this book's axes.

The original SVG and annotated PNG remain unchanged in figures/.
Run this script, then use Inkscape's CLI to preview the resulting SVG.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

FIGURES = Path(__file__).resolve().parents[1] / 'figures'
SVG = 'http://www.w3.org/2000/svg'
INKSCAPE = 'http://www.inkscape.org/namespaces/inkscape'
ET.register_namespace('', SVG)
ET.register_namespace('inkscape', INKSCAPE)
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')


def node(parent, tag, **attributes):
    return ET.SubElement(parent, f'{{{SVG}}}{tag}', attributes)


root = ET.parse(FIGURES / 'PlaneBoundary.svg').getroot()
root.set('viewBox', '12 -5 208 242')
root.set('width', '832')
root.set('height', '968')
node(root, 'title').text = 'Horizontal and vertical electric polarization at a plane boundary'
node(root, 'desc').text = (
    'The red plane of incidence intersects a blue horizontal interface. '
    'H polarization is perpendicular to the red plane; V polarization lies '
    'in it and is perpendicular to the incident ray. Positive z points into medium 2.'
)
background = ET.Element(f'{{{SVG}}}rect', {
    'x': '12', 'y': '-5', 'width': '208', 'height': '242', 'fill': 'white',
})
root.insert(0, background)

# Replace the old coordinate triad rather than carrying over the PPEO axes.
for child in list(root):
    if child.get('id') == 'layer1':
        root.remove(child)

labels = node(root, 'g', id='book-annotations', **{
    f'{{{INKSCAPE}}}groupmode': 'layer',
    f'{{{INKSCAPE}}}label': 'Book labels (xz incidence plane, z into medium)',
    'font-family': 'Arial, Helvetica, sans-serif', 'font-size': '4.4',
    'fill': '#243743',
})


def text(x, y, content, **attributes):
    element = node(labels, 'text', x=str(x), y=str(y), **attributes)
    element.text = content
    return element


def subscript(x, y, base, suffix, **attributes):
    element = text(x, y, base, **attributes)
    node(element, 'tspan', **{'baseline-shift': 'sub', 'font-size': '3.1'}).text = suffix
    return element


text(90, 28, 'Plane of incidence (xz)', transform='rotate(30 90 28)',
     fill='#9c2831', **{'font-size': '4.8'})
text(34, 88, 'Medium 1')
text(34, 153, 'Medium 2')
text(164, 163, 'Interface z = 0', transform='rotate(-30 164 163)',
     **{'font-size': '4'})
subscript(73, 43, 'k', 'i')
subscript(151, 69, 'k', 'r')
subscript(125, 153, 'k', 't')
subscript(104, 93, 'θ', 'i', **{'text-anchor': 'end'})
subscript(111, 134, 'θ', 't', **{'text-anchor': 'end'})
subscript(83, 116, 'E', 'H', fill='#007fa8', **{'font-weight': 'bold'})
subscript(137, 107, 'E', 'V', fill='#bd641d', **{'font-weight': 'bold'})

# Retain the original electric-field directions, but distinguish H and V.
for element in root.iter():
    colour = {'path1612': '#007fa8', 'path2255': '#bd641d'}.get(element.get('id'))
    if colour:
        element.set('style', f'fill:none;stroke:{colour};stroke-width:0.7;marker-end:url(#Arrow1Lend)')

# A separate, right-handed triad avoids covering the field arrows at the origin.
for endpoint, position, name in [
    ('200,29', (202, 32), 'x'),
    ('168,29', (163, 32), 'y'),
    ('184,43', (182, 49), 'z'),
]:
    node(labels, 'path', d=f'M184,20 L{endpoint}', fill='none',
         stroke='#243743', **{'stroke-width': '0.4', 'marker-end': 'url(#Arrow1Lend)'})
    text(*position, name, **{'font-style': 'italic'})

text(116, 222, 'H: E perpendicular to the plane of incidence',
     **{'text-anchor': 'middle', 'font-size': '4.2', 'fill': '#007fa8'})
text(116, 230, 'V: E in the plane of incidence, perpendicular to kᵢ',
     **{'text-anchor': 'middle', 'font-size': '4.2', 'fill': '#bd641d'})

output = FIGURES / 'interface_hv_polarization.svg'
ET.ElementTree(root).write(output, encoding='utf-8', xml_declaration=True)
print(output)
