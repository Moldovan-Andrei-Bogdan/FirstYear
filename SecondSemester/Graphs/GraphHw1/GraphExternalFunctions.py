import random

from Graph import Graph


class GraphExternalFunctions:
    @staticmethod
    def read_graph_from_file(file_name):
        open_file = open(file_name, "r")
        lines = open_file.readlines()
        first_line = lines[0].strip().split(" ")
        graph = Graph(int(first_line[0]), int(first_line[1]))
        for line_index in range(1, len(lines)):
            line = lines[line_index].strip()
            line_items = line.split(" ")
            if len(line_items) == 0:
                graph.add_vertex(int(line_items[0]))
            else:
                graph.add_to_in_dict(int(line_items[1]), int(line_items[0]))
                graph.add_to_out_dict(int(line_items[0]), int(line_items[1]))
                graph.add_to_cost(int(line_items[0]), int(line_items[1]), int(line_items[2]))
        open_file.close()
        return graph

    @staticmethod
    def write_graph_to_file(file_name, graph_instance):
        open_file = open(file_name, "w")
        number_of_vertices = graph_instance.number_of_vertices
        number_of_edges = graph_instance.get_number_of_edges()
        open_file.write(f"{number_of_vertices} {number_of_edges}\n")
        edges_data = graph_instance.get_all_edges_plus_costs()
        for key in edges_data:
            open_file.write(f"{key[0]} {key[1]} {edges_data[key]}\n")
        open_file.close()

    @staticmethod
    def generate_random_graph(number_of_vertices, number_of_edges):
        if number_of_edges > number_of_vertices * number_of_vertices:
            return None
        else:
            graph = Graph(number_of_vertices, 0)
            valid_edge_counter = 0
            while valid_edge_counter < number_of_edges:
                start_index = random.randint(0, number_of_vertices - 1)
                end_index = random.randint(0, number_of_vertices - 1)
                cost = random.randint(0, 350)
                if graph.add_edge(start_index, end_index, cost) is not False:
                    valid_edge_counter += 1
            return graph
