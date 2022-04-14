import copy


class UndirectedGraph:
    def __init__(self, nv,ne):
        self.__in_dictionary = {}
        self.__out_dictionary = {}
        self.__cost_dictionary = {}
        self.__vertices = nv
        self.__edges = 0

    def initialize_dictionaries(self):
        for index in range(0, self.__vertices):
            self.__in_dictionary[index] = []
            self.__out_dictionary[index] = []

    @property
    def number_of_vertices(self):
        return self.__vertices

    @number_of_vertices.setter
    def number_of_vertices(self, value):
        pass

    @property
    def number_of_edges(self):
        return self.__edges

    @number_of_edges.setter
    def number_of_edges(self, value):
        pass

    def parse_vertices(self):
        vertices_list = list(dict.fromkeys(list(self.__out_dictionary.keys()) + list(self.__in_dictionary.keys())))
        for vertex in vertices_list:
            # if len(self.__in_dict[vertex]) != 0 or len(self.__out_dict[vertex]) != 0:
            #     yield vertex
            yield vertex

    def add_edge(self, start_vertex, end_vertex, cost):
        if self.check_if_vertex_exists(start_vertex) is False or self.check_if_vertex_exists(end_vertex) is False:
            return None

        if self.is_there_edge(start_vertex, end_vertex) is True:
            return False
        else:
            self.__in_dictionary[end_vertex].append(start_vertex)
            self.__in_dictionary[start_vertex].append(end_vertex)
            self.__out_dictionary[start_vertex].append(end_vertex)
            self.__out_dictionary[end_vertex].append(start_vertex)
            self.__cost_dictionary[(start_vertex, end_vertex)] = cost
            self.__cost_dictionary[(end_vertex, start_vertex)] = cost
            self.__edges += 1
            return True

    def check_if_vertex_exists(self, vertex_to_find):
        if vertex_to_find not in self.__in_dictionary and vertex_to_find not in self.__out_dictionary:
            return False
        else:
            return True

    def parse_inbound_of_vertex(self, given_vertex):
        for inbound_neighbour in self.__in_dictionary[given_vertex]:
            yield inbound_neighbour

    def parse_outbound_of_vertex(self, given_vertex):
        for outbound_neighbour in self.__out_dictionary[given_vertex]:
            yield outbound_neighbour

    def is_there_edge(self, start_vertex, end_vertex):
        if (start_vertex not in self.__out_dictionary and start_vertex not in self.__in_dictionary) or (
                end_vertex not in self.__in_dictionary and end_vertex not in self.__out_dictionary):
            return False
        if end_vertex not in self.__out_dictionary[start_vertex] and start_vertex not in self.__out_dictionary[
            end_vertex] and start_vertex not in self.__in_dictionary[end_vertex] and end_vertex not in \
                self.__in_dictionary[start_vertex]:
            return False
        return True

    # def get_in_degree_and_out_degree_of_vertex(self, given_vertex):
    #     is_vertex_inside_in_dict = given_vertex in self.__in_dictionary
    #     is_vertex_inside_out_dict = given_vertex in self.__out_dictionary
    #     if is_vertex_inside_out_dict is False and is_vertex_inside_in_dict is False:
    #         return False
    #     else:
    #         in_degree = 0
    #         out_degree = 0
    #         if is_vertex_inside_in_dict is True:
    #             in_degree = len(self.__in_dictionary[given_vertex])
    #         if is_vertex_inside_out_dict is True:
    #             out_degree = len(self.__out_dictionary[given_vertex])
    #         return out_degree, in_degree

    def add_vertex(self, vertex_to_add):
        if self.check_if_vertex_exists(vertex_to_add) is True:
            return False
        else:
            self.__in_dictionary[vertex_to_add] = []
            self.__out_dictionary[vertex_to_add] = []
            self.__vertices += 1
            return True

    def remove_edge(self, start_vertex, end_vertex):
        if self.is_there_edge(start_vertex, end_vertex) is False:
            return False
        else:
            self.__in_dictionary[end_vertex].remove(start_vertex)
            self.__in_dictionary[start_vertex].remove(end_vertex)
            self.__out_dictionary[start_vertex].remove(end_vertex)
            self.__out_dictionary[end_vertex].remove(start_vertex)
            self.__cost_dictionary.pop((start_vertex, end_vertex), None)
            self.__edges -= 1
            return True

    def remove_vertex(self, vertex_to_remove):
        if self.check_if_vertex_exists(vertex_to_remove) is False:
            return False
        else:
            for edge in self.__out_dictionary[vertex_to_remove]:
                self.remove_edge(vertex_to_remove, edge)
            for edge in self.__in_dictionary[vertex_to_remove]:
                self.remove_edge(vertex_to_remove, edge)
            if vertex_to_remove in self.__in_dictionary:
                self.__in_dictionary.pop(vertex_to_remove, None)
            if vertex_to_remove in self.__out_dictionary:
                self.__out_dictionary.pop(vertex_to_remove, None)

            self.__vertices -= 1

    def get_edge_info(self, start_vertex, end_vertex):
        if self.is_there_edge(start_vertex, end_vertex) is False:
            return False
        else:
            return self.__cost_dictionary[(start_vertex, end_vertex)]

    def get_copy_of_out_dictionary(self):
        return copy.deepcopy(self.__out_dictionary)
