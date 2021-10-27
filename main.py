import DatasetHandler.AIDSHandler as aids_handler
import DatasetHandler.COLLABHandler as collab_handler
import DatasetHandler.ENZYMESHandler as enzymes_handler
import DatasetHandler.IMDB_BINARY_Handler as imdb_bin_handler
import DatasetHandler.MSRC_9_Handler as msrc_9_handler
import DatasetHandler.MSRC_21C_Handler as msrc_21_handler
import DatasetHandler.MUTAGHandler as mutag_handler
import DatasetHandler.PROTEINSHandler as proteins_handler
import DatasetHandler.SYNTHETICHandler as synthetic_handler
import DatasetHandler.SynthieHandler as synthei_handler
import DatasetHandler.REDDIT_MULTI_5K_Handler as reddit_multi_5k_handler

if __name__ == '__main__':
    # graph_set = {0: {1: 10, 2: 20}, 1: {0: 1}, 2: {0: 5, 1: 2}}

    aids_handler.generate_graph_adj_matrix_file()
    collab_handler.generate_graph_adj_matrix_file()
    enzymes_handler.generate_graph_adj_matrix_file()
    imdb_bin_handler.generate_graph_adj_matrix_file()
    msrc_9_handler.generate_graph_adj_matrix_file()
    msrc_21_handler.generate_graph_adj_matrix_file()
    mutag_handler.generate_graph_adj_matrix_file()
    proteins_handler.generate_graph_adj_matrix_file()
    synthetic_handler.generate_graph_adj_matrix_file()
    synthei_handler.generate_graph_adj_matrix_file()
    reddit_multi_5k_handler.generate_graph_adj_matrix_file()
