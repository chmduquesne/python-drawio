#!/usr/bin/env python3
import networkx


def max_degree(g):
    """
    Returns the maximum number of edges of any node in the graph
    """
    return max([g.degree[n] for n in g])



def edge_styles(g):
    """
    Returns the list of all possible edge styles
    """
    styles = set()
    for e in g.edges(data="style"):
        style = "-"
        if e[2] is not None:
            style = e[2]
        styles.add(style)
    return sorted(list(styles))



def write_header(g, f):
    """
    Creates a header for the csv file of the graph
    """
    n = max_degree(g)
    es = edge_styles(g)

    f.write("# identity: nodeid\n")
    f.write("# label: %label%\n")
    f.write("# style: %style%\n")
    f.write("# link: url\n")
    f.write("# width: @width\n")
    f.write("# height: @height\n")
    f.write("# layout: verticalflow\n")

    refs = [f"ref_{i}_{j}" for j in range(len(es)) for i in range(n)]
    labels = [f"label_{i}" for i in range(n)]

    f.write("# ignore: nodeid,style,height,width," + ",".join(refs +
        labels) + "\n" )

    # ref_i_j is connected to nodeid with label i and edge style j
    for j, s in enumerate(es):
        for i in range(n):
            f.write(
                f'# connect: {{"from": "ref_{i}_{j}", "to": "nodeid", '
                f'"fromlabel": "label_{i}", '
                f'"style": "{s}"}}\n')
    f.write(','.join(
        ["nodeid", "label", "tags", "style", "width", "height", "link"] +
        refs + labels
        ) + "\n" )



def write_graph(g, f):
    """
    Creates the content for the csv file of the graph
    """
    n = max_degree(g)
    es = edge_styles(g)

    for node in g.nodes:
        label = g.nodes[node].get("label", "-")
        tags = g.nodes[node].get("tags", "-")
        style = g.nodes[node].get("style", "-")
        link = g.nodes[node].get("link", "-")
        width = g.nodes[node].get("width", "auto")
        height = g.nodes[node].get("height", "auto")

        # ref_i_j is connected to nodeid with label i and edge style j
        refs = ["-"] * n * len(es)
        labels = ["-"] * n
        for i, e in enumerate(g.edges(node, data=True)):
            data = e[2]
            j = es.index(data.get("style", "-"))
            refs[j*n+i] = e[1]
            labels[i] = data.get("label", "-")

        f.write(','.join([node, label, tags, style, width, height, link] + refs + labels) + "\n")




def write(g, f):
    write_header(g, f)
    write_graph(g, f)
