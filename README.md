# drawio
A library to draw networkx graphs with diagrams.net

# Documentation

This library generates graphs using the [csv
API](https://drawio-app.com/import-from-csv-to-drawio/).

## Usage

```python
import networkx as nx
import drawio
import sys

g = nx.gn_graph(10)
drawio.write(g, sys.stdout)
```

This will print

```csv
# identity: nodeid
# label: %label%
# style: %style%
# link: url
# width: @width
# height: @height
# layout: verticalflow
# ignore: nodeid,style,height,width,ref_0_0,ref_1_0,ref_2_0,ref_3_0,ref_4_0,label_0,label_1,label_2,label_3,label_4
# connect: {"from": "ref_0_0", "to": "nodeid", "fromlabel": "label_0", "style": "-"}
# connect: {"from": "ref_1_0", "to": "nodeid", "fromlabel": "label_1", "style": "-"}
# connect: {"from": "ref_2_0", "to": "nodeid", "fromlabel": "label_2", "style": "-"}
# connect: {"from": "ref_3_0", "to": "nodeid", "fromlabel": "label_3", "style": "-"}
# connect: {"from": "ref_4_0", "to": "nodeid", "fromlabel": "label_4", "style": "-"}
nodeid,label,tags,style,width,height,link,ref_0_0,ref_1_0,ref_2_0,ref_3_0,ref_4_0,label_0,label_1,label_2,label_3,label_4
0,-,-,-,auto,auto,-,-,-,-,-,-,-,-,-,-,-
1,-,-,-,auto,auto,-,0,-,-,-,-,-,-,-,-,-
2,-,-,-,auto,auto,-,1,-,-,-,-,-,-,-,-,-
3,-,-,-,auto,auto,-,1,-,-,-,-,-,-,-,-,-
4,-,-,-,auto,auto,-,0,-,-,-,-,-,-,-,-,-
5,-,-,-,auto,auto,-,4,-,-,-,-,-,-,-,-,-
6,-,-,-,auto,auto,-,0,-,-,-,-,-,-,-,-,-
7,-,-,-,auto,auto,-,0,-,-,-,-,-,-,-,-,-
8,-,-,-,auto,auto,-,0,-,-,-,-,-,-,-,-,-
9,-,-,-,auto,auto,-,5,-,-,-,-,-,-,-,-,-
```
