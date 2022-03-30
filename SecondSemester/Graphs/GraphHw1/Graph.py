import copy


class Graph:
    def __init__(self, given_number_of_vertices, given_number_of_edges):
        self.__in_dict = {}
        self.__out_dict = {}
        self.__cost_dict = {}
        self.__number_of_vertices = given_number_of_vertices
        self.__number_of_edges = given_number_of_edges
        self.__initialize_dictionaries()

    def __initialize_dictionaries(self):
        for index in range(0, self.__number_of_vertices):
            self.__in_dict[index] = []
            self.__out_dict[index] = []

    def check_if_vertex_exists(self, vertex_to_check):
        if vertex_to_check in self.__in_dict or vertex_to_check in self.__out_dict:
            return True
        else:
            return False

    @property
    def number_of_vertices(self):
        return self.__number_of_vertices

    def get_number_of_edges(self):
        return self.__number_of_edges

    @number_of_vertices.setter
    def number_of_vertices(self, value):
        pass

    def get_edge_info(self, start_vertex, end_vertex):
        if self.is_there_edge(start_vertex, end_vertex) is False:
            return None
        else:
            return self.__cost_dict[(start_vertex, end_vertex)]

    def set_edge_info(self, start_vertex, end_vertex, new_cost):
        if self.is_there_edge(start_vertex, end_vertex) is False:
            return False
        else:
            self.__cost_dict[(start_vertex, end_vertex)] = new_cost
            return True

    def parse_vertices(self):
        vertices_list = list(dict.fromkeys(list(self.__out_dict.keys()) + list(self.__in_dict.keys())))
        for vertex in vertices_list:
            # if len(self.__in_dict[vertex]) != 0 or len(self.__out_dict[vertex]) != 0:
            #     yield vertex
            yield vertex

    def parse_inbound_of_vertex(self, given_vertex):
        for inbound_neighbour in self.__in_dict[given_vertex]:
            yield inbound_neighbour

    def parse_outbound_of_vertex(self, given_vertex):
        for outbound_neighbour in self.__out_dict[given_vertex]:
            yield outbound_neighbour

    def is_there_edge(self, start_vertex, destination_vertex):
        if (start_vertex, destination_vertex) not in self.__cost_dict:
            return False
        else:
            return True

    def get_in_degree_and_out_degree_of_vertex(self, given_vertex):
        is_vertex_inside_in_dict = given_vertex in self.__in_dict
        is_vertex_inside_out_dict = given_vertex in self.__out_dict
        if is_vertex_inside_out_dict is False and is_vertex_inside_in_dict is False:
            return False
        else:
            in_degree = 0
            out_degree = 0
            if is_vertex_inside_in_dict is True:
                in_degree = len(self.__in_dict[given_vertex])
            if is_vertex_inside_out_dict is True:
                out_degree = len(self.__out_dict[given_vertex])
            return out_degree, in_degree

    def add_vertex(self, vertex_to_add):
        if self.check_if_vertex_exists(vertex_to_add):
            return False
        else:
            self.__in_dict[vertex_to_add] = []
            self.__out_dict[vertex_to_add] = []
            self.__number_of_vertices += 1
            return True

    def add_to_in_dict(self, source_vertex, destination_vertex):
        self.__in_dict[source_vertex].append(destination_vertex)

    def add_to_out_dict(self, source_vertex, destination_vertex):
        self.__out_dict[source_vertex].append(destination_vertex)

    def add_to_cost(self, source_vertex, destination_vertex, cost):
        self.__cost_dict[(source_vertex, destination_vertex)] = cost

    def add_edge(self, start_vertex, end_vertex, cost):
        if self.check_if_vertex_exists(start_vertex) is False or self.check_if_vertex_exists(end_vertex) is False:
            return None
        else:
            if self.is_there_edge(start_vertex, end_vertex) is not False:
                return False
            else:
                self.add_to_cost(start_vertex, end_vertex, cost)
                self.add_to_in_dict(end_vertex, start_vertex)
                self.add_to_out_dict(start_vertex, end_vertex)
                self.__number_of_edges += 1
                return True

    def remove_edge(self, start_vertex, end_vertex):
        if self.is_there_edge(start_vertex, end_vertex) is False:
            return False
        else:
            self.__in_dict[end_vertex].remove(start_vertex)
            self.__out_dict[start_vertex].remove(end_vertex)
            self.__cost_dict.pop((start_vertex, end_vertex), None)
            self.__number_of_edges -= 1
            return True

    def __remove_vertex_from_neighbours(self, target_vertex):
        for vertex in self.__out_dict:
            if target_vertex in self.__out_dict[vertex]:
                self.__out_dict[vertex].remove(target_vertex)

        for vertex in self.__in_dict:
            if target_vertex in self.__in_dict[vertex]:
                self.__in_dict[vertex].remove(target_vertex)

    def remove_vertex(self, target_vertex):
        if self.check_if_vertex_exists(target_vertex) is False:
            return False
        else:
            self.__remove_vertex_from_neighbours(target_vertex)
            if target_vertex in self.__in_dict:
                self.__in_dict.pop(target_vertex, None)
            if target_vertex in self.__out_dict:
                self.__out_dict.pop(target_vertex, None)

            list_of_edges = list(self.__cost_dict.keys())
            for edge_pair in list_of_edges:
                if edge_pair[0] == target_vertex or edge_pair[1] == target_vertex:
                    self.__cost_dict.pop(edge_pair, None)
                    self.__number_of_edges -= 1
            self.__number_of_vertices -= 1
            return True

    def get_all_edges_plus_costs(self):
        return copy.deepcopy(self.__cost_dict)
