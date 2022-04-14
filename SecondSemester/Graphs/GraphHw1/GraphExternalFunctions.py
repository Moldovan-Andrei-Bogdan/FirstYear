import random
from queue import Queue

from Graph import Graph
from UndirectedGraph import UndirectedGraph


class GraphExternalFunctions:
    @staticmethod
    def read_graph_from_file(file_name, type_of_graph):
        if type_of_graph == 'd':
            open_file = open(file_name, "r")
            lines = open_file.readlines()
            first_line = lines[0].strip().split(" ")
            graph = Graph(int(first_line[0]), int(first_line[1]))
            for line_index in range(1, len(lines)):
                line = lines[line_index].strip()
                line_items = line.split(" ")
                if len(line_items) == 1:
                    graph.add_vertex(int(line_items[0]))
                else:
                    graph.add_to_in_dict(int(line_items[1]), int(line_items[0]))
                    graph.add_to_out_dict(int(line_items[0]), int(line_items[1]))
                    graph.add_to_cost(int(line_items[0]), int(line_items[1]), int(line_items[2]))
            open_file.close()
            return graph
        else:
            open_file = open(file_name, "r")
            lines = open_file.readlines()
            first_line = lines[0].strip().split(" ")
            graph = UndirectedGraph(int(first_line[0]), int(first_line[1]))
            graph.initialize_dictionaries()
            for line_index in range(1, len(lines)):
                line = lines[line_index].strip()
                line_items = line.split(" ")
                if len(line_items) == 1:
                    graph.add_vertex(int(line_items[0]))
                else:
                    if graph.check_if_vertex_exists(int(line_items[0])) is False:
                        graph.add_vertex(int(line_items[0]))
                    if graph.check_if_vertex_exists(int(line_items[1])) is False:
                        graph.add_vertex(int(line_items[1]))
                    graph.add_edge(int(line_items[0]), int(line_items[1]), int(line_items[2]))
            open_file.close()
            return graph

    @staticmethod
    def write_graph_to_file(file_name, graph_instance, type_of_graph):
        if type_of_graph == 'd':
            open_file = open(file_name, "w")
            number_of_vertices = graph_instance.number_of_vertices
            number_of_edges = graph_instance.get_number_of_edges()
            open_file.write(f"{number_of_vertices} {number_of_edges}\n")
            edges_data = graph_instance.get_all_edges_plus_costs()
            for key in edges_data:
                open_file.write(f"{key[0]} {key[1]} {edges_data[key]}\n")
            open_file.close()
        else:
            open_file = open(file_name, "w")
            out_dict = graph_instance.get_copy_of_out_dictionary()
            duplicate_list = []
            open_file.write(f"{graph_instance.number_of_vertices} {graph_instance.number_of_edges}\n")
            for vertex in out_dict:
                for aux in out_dict[vertex]:
                    if (aux, vertex) not in duplicate_list and (vertex, aux) not in duplicate_list:
                        open_file.write(f"{vertex} {aux} {graph_instance.get_edge_info(vertex, aux)}\n")
                        duplicate_list.append((vertex, aux))
            open_file.close()

    @staticmethod
    def generate_random_graph(number_of_vertices, number_of_edges, type_of_graph):
        if type_of_graph == 'd' and number_of_edges > number_of_vertices * number_of_vertices:
            return None
        if type_of_graph == 'u' and number_of_edges > int((number_of_vertices * (number_of_vertices - 1)) / 2):
            return None
        else:
            if type_of_graph == 'd':
                graph = Graph(number_of_vertices, 0)
                valid_edge_counter = 0
                while valid_edge_counter < number_of_edges:
                    start_index = random.randint(0, number_of_vertices - 1)
                    end_index = random.randint(0, number_of_vertices - 1)
                    cost = random.randint(0, 350)
                    if graph.add_edge(start_index, end_index, cost) is not False:
                        valid_edge_counter += 1
                return graph
            else:
                graph = UndirectedGraph(0, 0)
                valid_edge_counter = 0
                for index in range(1, number_of_vertices + 1):
                    graph.add_vertex(index)
                while valid_edge_counter < int(number_of_edges / 2):
                    start_index = random.randint(1, number_of_vertices)
                    end_index = random.randint(1, number_of_vertices)
                    cost = random.randint(0, 350)
                    if start_index != end_index and graph.add_edge(start_index, end_index, cost) is not False:
                        valid_edge_counter += 1
                return graph

    @staticmethod
    def find_connected_components(source_graph):
        out_dict_of_source_graph = source_graph.get_copy_of_out_dictionary()
        keys_of_out_dict = list(out_dict_of_source_graph.keys())
        list_of_visited_vertices = []
        list_of_connected_components = []
        for vertex in keys_of_out_dict:
            if vertex not in list_of_visited_vertices:
                undirected_graph_of_cc = UndirectedGraph(0, 0)
                undirected_graph_of_cc.add_vertex(vertex)
                queue_of_bfs = Queue()
                queue_of_bfs.put(vertex)
                list_of_visited_vertices.append(vertex)
                while not queue_of_bfs.empty():
                    aux_vertex = queue_of_bfs.get()
                    for item in out_dict_of_source_graph[aux_vertex]:
                        if item not in list_of_visited_vertices:
                            queue_of_bfs.put(item)
                            list_of_visited_vertices.append(item)
                            if undirected_graph_of_cc.check_if_vertex_exists(aux_vertex) is False:
                                undirected_graph_of_cc.add_vertex(aux_vertex)
                            if undirected_graph_of_cc.check_if_vertex_exists(item) is False:
                                undirected_graph_of_cc.add_vertex(item)
                            undirected_graph_of_cc.add_edge(aux_vertex, item,
                                                            source_graph.get_edge_info(aux_vertex, item))
                        elif source_graph.is_there_edge(aux_vertex, item) is True:
                            undirected_graph_of_cc.add_edge(aux_vertex, item,
                                                            source_graph.get_edge_info(aux_vertex, item))
                list_of_connected_components.append(undirected_graph_of_cc)

        return list_of_connected_components
