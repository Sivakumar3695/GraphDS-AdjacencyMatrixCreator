# GraphDS-AdjacencyMatrixCreator

We chose the following datasets as the top 11 among the long list of Graph Datasets listed in the below link:
https://ls11-www.cs.tu-dortmund.de/staff/morris/graphkerneldatasets

Our list of datasets:

![image](https://user-images.githubusercontent.com/29046579/139038982-91ece68f-25c2-4060-853c-2ed8ca2800e3.png)

The users of this project need to place the datasets (download from the above link and extract) in the folder "InputDS". On running the main.py, the program will read essential files in the dataset folders and create corresponding adjacency matrices.

--------------------------------------------------------------------------
The program will generate the output folder in the following structure:

![Screenshot from 2021-10-27 15-09-18](https://user-images.githubusercontent.com/29046579/139040942-b58e673e-9119-4c19-85ed-cf3507783cdc.png)
              
---------------------------------------------------------------------------
In the above structure, class_0, class_1 and class_2 are provided just for the explanation. In real-time, folder names may vary depending on the list of graph labels available for a given dataset.
For example, it can be [class_0, class_1 ,...] or [class_1, class_2, ...] or [class_-1, class_1] or any other format depending upon the list of dataset's graph labels.

In turn, the individual folders (for example, consider class_0 folder) will contain the adjacency matrices of the graphs which fall under the category 0 (graph label for those graphs will be 0).
