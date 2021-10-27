import DatasetHandler.InputDSHandler as ds_handler

GRAPH_LABEL_ENUM = [1, 2, 3]

DATASET_NAME = "COLLAB"
INPUT_FOLDER = ds_handler.INPUT_BASE_FOLDER + DATASET_NAME + ds_handler.FILE_SEPARATOR
OUTPUT_FOLDER = ds_handler.OUTPUT_BASE_FOLDER + DATASET_NAME
GRAPH_IND_FILE = 'COLLAB_graph_indicator.txt'
GRAPH_LABEL_FILE = 'COLLAB_graph_labels.txt'
GRAPH_EDGE_FILE = 'COLLAB_A.txt'


def generate_graph_adj_matrix_file():
    ds_handler.validate_and_create_out_folders(GRAPH_LABEL_ENUM, DATASET_NAME)
    ds_handler.generate_graph_adj_matrix_file(
        graph_label_file=INPUT_FOLDER + GRAPH_LABEL_FILE,
        graph_ind_file=INPUT_FOLDER + GRAPH_IND_FILE,
        graph_edge_file=INPUT_FOLDER + GRAPH_EDGE_FILE,
        output_folder=OUTPUT_FOLDER
    )
