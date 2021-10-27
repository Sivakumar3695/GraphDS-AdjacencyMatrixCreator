

def write_matrix_in_file(graph_set, file):
    for node in graph_set:
        for edge in range(1, len(graph_set)+1):
            if not graph_set[node].get(edge):
                # print(0, end=' ')
                file.write('0 ')
                continue
            edge_details = graph_set[node].get(edge)
            # print(edge_details, end=' ')
            file.write(str(edge_details) + ' ')
        # print("\n", end='')
        file.write('\n')
    # print(graph_set)
