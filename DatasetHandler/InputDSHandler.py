import os
import shutil

import utils.generateAdjacencyMatrixFile as generator


INPUT_BASE_FOLDER = './InputDS/'
OUTPUT_BASE_FOLDER = './output/'
FILE_SEPARATOR = '/'


def validate_and_create_out_folders(graph_labels_enum, ds_name_str):
    if not os.path.exists(INPUT_BASE_FOLDER + ds_name_str):
        assert 'Error in reading file'
    if not os.path.exists(OUTPUT_BASE_FOLDER):
        os.mkdir(OUTPUT_BASE_FOLDER)
    out_folder = OUTPUT_BASE_FOLDER + ds_name_str
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    for label in graph_labels_enum:
        if os.path.exists(out_folder + '/Class_' + str(label)):
            shutil.rmtree(out_folder + '/Class_' + str(label))
        os.mkdir(out_folder + '/Class_' + str(label))


def generate_graph_adj_matrix_file(graph_label_file, graph_ind_file, graph_edge_file, output_folder):
    # read graph label file contents
    g_label_file = open(graph_label_file, 'r')
    g_labels = g_label_file.readlines()
    g_label_file.close()

    # read graph indicator file contents
    gi_file = open(graph_ind_file, 'r')
    lines = gi_file.readlines()
    gi_file.close()

    # read edge details
    ge_file = open(graph_edge_file, 'r')
    edge_details = ge_file.readlines()
    ge_file.close()

    graph_set = {}
    node_cnt = 0
    current_graph = 0
    start_pos = 0
    prev_graph_end_node_number = 0

    # loop through the line read in the graph indicator file
    # find the end of a particular graph when the number changes in the graph indicator file.
    for index in range(len(lines)):
        line = lines[index]
        if current_graph + 1 != int(line) or index == len(lines) - 1:
            class_label = g_labels[current_graph]
            output_label_folder = output_folder + '/Class_' + str(class_label).replace('\n', '')

            # increase the node count of the current graph and create a dictionary for the new node's edges
            # while reading the last line of the graph indicator file.
            if index == len(lines) - 1:
                node_cnt = node_cnt + 1
                graph_set[node_cnt] = {}

            start_pos = handle_file_creation(
                graph_set,
                edge_details,
                output_label_folder,
                start_pos,
                current_graph + 1,
                prev_graph_end_node_number
            )

            # as node numbers in graph indicator file is sequential (i.e the node number of the second graph will not
            # start from 1 but the immediate number after the last node number of the previous graph),
            # we need to store the node number of the last node in the previous graph in the following way
            prev_graph_end_node_number = prev_graph_end_node_number + len(graph_set.keys())

            node_cnt = 0                        # reset node count
            graph_set = {}                      # reset graph
            current_graph = current_graph + 1   # increment current graph count

        # increase the node count of the current graph and create a dictionary for the new node's edges
        node_cnt = node_cnt + 1
        graph_set[node_cnt] = {}

    # print(current_graph)


def handle_file_creation(graph, edge_det_file_cont, class_folder, start_pos=0,
                         current_graph=1, prev_graph_end_node_number=0):
    node_list = graph.keys()
    return_index = 0

    # read edge details
    for index in range(start_pos, len(edge_det_file_cont)):
        edge_det = edge_det_file_cont[index]
        edge_det = edge_det.replace(' ', '')
        edge_nodes = edge_det.split(sep=',')
        base_node = int(edge_nodes[0]) - prev_graph_end_node_number
        end_node = int(edge_nodes[1].replace('\n', '')) - prev_graph_end_node_number
        if not (base_node in node_list and end_node in node_list):
            return_index = index
            break
        edge_dic = {end_node: 1}
        graph[base_node].update(edge_dic)

    # write to .txt file
    print('Generating file for graph-no-' + str(current_graph))
    file = open(class_folder + '/' + str(current_graph) + '.txt', 'x')
    generator.write_matrix_in_file(graph, file)
    file.close()

    return return_index
