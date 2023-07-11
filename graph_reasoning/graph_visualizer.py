import matplotlib.pyplot as plt
import numpy as np


def visualize_nxgraph(graph, image_name):
    nodes_data = graph.get_attributes_of_all_nodes()
    plt.figure(image_name)
    for node_data in nodes_data:
        if node_data[1]["viz_type"] == "Point":
            plt.plot(node_data[1]["viz_data"][0], node_data[1]["viz_data"][1], node_data[1]["viz_feat"])

        elif node_data[1]["viz_type"] == "Line":
            viz_data = np.array(node_data[1]["viz_data"])
            plt.plot(viz_data[:,0], viz_data[:,1], node_data[1]["viz_feat"], linewidth=1.5)

    edges_data = graph.get_attributes_of_all_edges()
    for edge_data in edges_data:
        points = np.array([nodes_data[edge_data[0]]["center"], nodes_data[edge_data[1]]["center"]])
        viz_feat = edge_data[2]["viz_feat"] if "viz_feat" in edge_data[2].keys() else ""

        plt.plot(points[:,0], points[:,1], viz_feat)

    # plt.xlim([-3, 23])
    # plt.ylim([-3, 23])

    plt.draw()
    # plt.show()