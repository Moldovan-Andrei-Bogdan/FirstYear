import copy

from Graph import Graph
from GraphExternalFunctions import GraphExternalFunctions
from UndirectedGraph import UndirectedGraph


class UI:
    def __init__(self):
        self.__list_of_graph_copies = []
        self.__list_of_connected_components = None
        self.__active_graph = None

    def __print_menu(self):
        print("0.Create Empty Graph")
        print("1.Read Graph from file")
        print("2.Get number of vertices")
        print("3.Parse the set of vertices")
        print("4.Parse the inbound edges of vertex")
        print("5.Parse the outbound edges of vertex")
        print("6.Check if edge exists")
        print("7.Get in degree and out degree of vertex")
        print("8.Add new vertex")
        print("9.Add new edge")
        print("10.Get edge info")
        print("11.Change edge info")
        print("12.Remove edge")
        print("13.Remove vertex")
        print("14.Make a copy of the graph")
        print("15.Select a copy of the graph")
        print("16.Remove a copy of the graph")
        print("17.Write graph to file")
        print("18.Create Random Graph")
        print("x.Exit")

    def __print_menu2(self):
        print("0.Create empty undirected graph")
        print("1.Read Undirected Graph from file")
        print("2.Get number of vertices")
        print("3.Parse the set of vertices")
        print("4.Parse the inbound edges of vertex")
        print("5.Parse the outbound edges of vertex")
        print("6.Check if edge exists")
        print("7.Add new vertex")
        print("8.Add new edge")
        print("9.Remove edge")
        print("10.Remove vertex")
        print("11.Make a copy of the graph")
        print("12.Select a copy of the graph")
        print("13.Remove a copy of the graph")
        print("14.Write graph to file")
        print("15.Create Random Undirected Graph")
        print("16.Get edge info")
        print("17.Get Connected Components")
        print("18.Display Connected Components")
        print("19.Select Connected Component")
        print("x.Exit")

    def run_console_u(self):
        while True:
            self.__print_menu2()
            option = input("Your option is:")
            if option == '0':
                self.__active_graph = UndirectedGraph()

            if option == '1':
                self.__active_graph = GraphExternalFunctions.read_graph_from_file("./in.txt", "u")

            if option == '2':
                if self.__active_graph is not None:
                    print(f"Number of vertices {self.__active_graph.number_of_vertices}")
                else:
                    print("No instance of a graph")
            if option == '3':
                if self.__active_graph is not None:
                    for vertex in self.__active_graph.parse_vertices():
                        print(f"A vertex is {vertex}")
                else:
                    print("No instance of a graph")
            if option == '4':
                if self.__active_graph is not None:
                    target_vertex = input("Vertex is:")
                    if self.__active_graph.check_if_vertex_exists(int(target_vertex)) is False:
                        print("This vertex does not exist")
                    else:
                        in_flag = False
                        for inbound in self.__active_graph.parse_inbound_of_vertex(int(target_vertex)):
                            print(f"{inbound},{target_vertex}")
                            in_flag = True
                        if in_flag is False:
                            print("No inbounds for this vertex")
                else:
                    print("No instance of a graph")

            if option == '5':
                if self.__active_graph is not None:
                    target_vertex = input("Vertex is:")
                    if self.__active_graph.check_if_vertex_exists(int(target_vertex)) is False:
                        print("This vertex does not exist")
                    else:
                        in_flag = False
                        for outbound in self.__active_graph.parse_outbound_of_vertex(int(target_vertex)):
                            print(f"{target_vertex},{outbound}")
                            in_flag = True
                        if in_flag is False:
                            print("No outbounds for this vertex")
                else:
                    print("No instance of a graph")

            if option == '6':
                if self.__active_graph is not None:
                    start_vertex = input("Start vertex is:")
                    end_vertex = input("End vertex is:")
                    if self.__active_graph.is_there_edge(int(start_vertex), int(end_vertex)) is True:
                        print("This edge exists")
                    else:
                        print("This edge does not exist")
                else:
                    print("No instance of a graph")

            if option == '7':
                if self.__active_graph is not None:
                    vertex_to_add = input("Vertex you want to add is:")
                    if self.__active_graph.add_vertex(int(vertex_to_add)) is False:
                        print("This vertex already exists")
                    else:
                        print("Vertex added")
                else:
                    print("No instance of a graph")

            if option == '8':
                if self.__active_graph is not None:
                    start_vertex = input("Start vertex is:")
                    end_vertex = input("End vertex is:")
                    result_of_adding_edge = self.__active_graph.add_edge(int(start_vertex), int(end_vertex))
                    if result_of_adding_edge is None:
                        print("One of the vertices given does not exist")
                    if result_of_adding_edge is False:
                        print("This edge already exists")
                    elif result_of_adding_edge is not False and result_of_adding_edge is not None:
                        print("Added the new edge")
                else:
                    print("No graph instance")

            if option == '9':
                if self.__active_graph is not None:
                    start_vertex = input("Start Vertex is:")
                    end_vertex = input("End vertex is:")
                    if self.__active_graph.remove_edge(int(start_vertex), int(end_vertex)) is False:
                        print("Edge given does not exist")
                    else:
                        print("Edge was removed")

            if option == '10':
                if self.__active_graph is not None:
                    vertex_to_remove = input("Vertex you want to remove is:")
                    if self.__active_graph.remove_vertex(int(vertex_to_remove)) is False:
                        print("Vertex given does not exist")
                    else:
                        print("Vertex was removed")

            if option == '11':
                if self.__active_graph is not None:
                    self.__list_of_graph_copies.append(copy.deepcopy(self.__active_graph))
                    print("A copy of the current graph was made")
                else:
                    print("No instance of a graph")

            if option == '12':
                if self.__active_graph is not None:
                    index_of_the_copy_in_list = input("Enter the index of the graph copy in the list of copies:")
                    index_of_the_copy_in_list = int(index_of_the_copy_in_list)
                    if index_of_the_copy_in_list not in range(0, len(self.__list_of_graph_copies)):
                        print("Index given is not inside(not valid)")
                    else:
                        self.__active_graph = copy.deepcopy(self.__list_of_graph_copies[index_of_the_copy_in_list])
                        print("The specified copy was set now as the active graph")
                else:
                    print("No instance of a graph")

            if option == '13':
                if self.__active_graph is not None:
                    index_of_the_copy_in_list = input("Enter the index of the graph copy in the list of copies:")
                    index_of_the_copy_in_list = int(index_of_the_copy_in_list)
                    if index_of_the_copy_in_list not in range(0, len(self.__list_of_graph_copies)):
                        print("Index given is not inside(not valid)")
                    else:
                        self.__list_of_graph_copies.pop(index_of_the_copy_in_list)
                        print("The specified copy was removed")
                else:
                    print("No instance of a graph")

            if option == "14":
                if self.__active_graph is not None:
                    GraphExternalFunctions.write_graph_to_file("./out.txt", self.__active_graph, "u")
                    print("The graph has been written to the file")
                else:
                    print("No instance of a graph")

            if option == '15':
                vertices_number = input("Number of vertices is:")
                edges_number = input("Number of edges is:")
                result_of_generation = GraphExternalFunctions.generate_random_graph(int(vertices_number),
                                                                                    int(edges_number), "u")
                if result_of_generation is not None:
                    self.__active_graph = result_of_generation
                    print("The graph was generated randomly and set as the active graph")
                else:
                    print("The edges are way to many compared to the vertices")

            if option == '16':
                if self.__active_graph is not None:
                    start_vertex = input("Start Vertex is:")
                    end_vertex = input("End Vertex is:")
                    result_of_getter = self.__active_graph.get_edge_info(int(start_vertex), int(end_vertex))
                    if result_of_getter is not None:
                        print(f"The cost of the specified edge is {result_of_getter}")
                    else:
                        print("This edge does not exist")
                else:
                    print("No instance of a graph")

            if option == '17':
                self.__list_of_connected_components = GraphExternalFunctions.find_connected_components(
                    self.__active_graph)
                print(len(self.__list_of_connected_components))

            if option == '18':
                if self.__list_of_connected_components is not None:
                    index = 0
                    for connected_component in self.__list_of_connected_components:
                        print(f"The connected component with index {index} is:")
                        for item in connected_component.parse_vertices():
                            print(f"A vertex is {item}")
                        index += 1
                else:
                    print("No connected components yet...try to search for some")
            if option == '19':
                index_of_cc = input("Please enter the index of the connected component you want to select:")
                if int(index_of_cc) not in range(0, len(self.__list_of_connected_components)):
                    print("Index out of range")
                else:
                    self.__active_graph = self.__list_of_connected_components[int(index_of_cc)]
                print("The selected connected component was set as the new active graph")
            if option == 'x':
                exit()

    def run_console_d(self):
        while True:
            self.__print_menu()
            option = input("Your option is:")
            if option == '0':
                self.__active_graph = Graph(0, 0)

            if option == '1':
                self.__active_graph = GraphExternalFunctions.read_graph_from_file("./in.txt", "d")

            if option == '2':
                if self.__active_graph is not None:
                    print(f"Number of vertices {self.__active_graph.number_of_vertices}")
                else:
                    print("No instance of a graph")

            if option == '3':
                if self.__active_graph is not None:
                    for vertex in self.__active_graph.parse_vertices():
                        print(f"A vertex is {vertex}")
                else:
                    print("No instance of a graph")

            if option == '4':
                if self.__active_graph is not None:
                    target_vertex = input("Vertex is:")
                    if self.__active_graph.check_if_vertex_exists(int(target_vertex)) is False:
                        print("This vertex does not exist")
                    else:
                        in_flag = False
                        for inbound in self.__active_graph.parse_inbound_of_vertex(int(target_vertex)):
                            print(f"{inbound},{target_vertex}")
                            in_flag = True
                        if in_flag is False:
                            print("No inbounds for this vertex")
                else:
                    print("No instance of a graph")

            if option == '5':
                if self.__active_graph is not None:
                    target_vertex = input("Vertex is:")
                    if self.__active_graph.check_if_vertex_exists(int(target_vertex)) is False:
                        print("This vertex does not exist")
                    else:
                        in_flag = False
                        for outbound in self.__active_graph.parse_outbound_of_vertex(int(target_vertex)):
                            print(f"{target_vertex},{outbound}")
                            in_flag = True
                        if in_flag is False:
                            print("No outbounds for this vertex")
                else:
                    print("No instance of a graph")

            if option == '6':
                if self.__active_graph is not None:
                    start_vertex = input("Start vertex is:")
                    end_vertex = input("End vertex is:")
                    if self.__active_graph.is_there_edge(int(start_vertex), int(end_vertex)) is True:
                        print("This edge exists")
                    else:
                        print("This edge does not exist")
                else:
                    print("No instance of a graph")

            if option == '7':
                if self.__active_graph is not None:
                    target_vertex = input("Vertex is:")
                    if self.__active_graph.check_if_vertex_exists(int(target_vertex)) is False:
                        print("This vertex does not exist")
                    else:
                        print(
                            f"Out degree, In degree is:{self.__active_graph.get_in_degree_and_out_degree_of_vertex(int(target_vertex))}")
                else:
                    print("No instance of a graph")

            if option == '8':
                if self.__active_graph is not None:
                    vertex_to_add = input("Vertex you want to add is:")
                    if self.__active_graph.add_vertex(int(vertex_to_add)) is False:
                        print("This vertex already exists")
                    else:
                        print("Vertex added")
                else:
                    print("No instance of a graph")

            if option == '9':
                if self.__active_graph is not None:
                    start_vertex = input("Start vertex is:")
                    end_vertex = input("End vertex is:")
                    cost = input("The cost is")
                    result_of_adding_edge = self.__active_graph.add_edge(int(start_vertex), int(end_vertex), int(cost))
                    if result_of_adding_edge is None:
                        print("One of the vertices given does not exist")
                    if result_of_adding_edge is False:
                        print("This edge already exists")
                    elif result_of_adding_edge is not False and result_of_adding_edge is not None:
                        print("Added the new edge")
                else:
                    print("No graph instance")

            if option == '10':
                if self.__active_graph is not None:
                    start_vertex = input("Start Vertex is:")
                    end_vertex = input("End Vertex is:")
                    result_of_getter = self.__active_graph.get_edge_info(int(start_vertex), int(end_vertex))
                    if result_of_getter is not None:
                        print(f"The cost of the specified edge is {result_of_getter}")
                    else:
                        print("This edge does not exist")
                else:
                    print("No instance of a graph")

            if option == '11':
                if self.__active_graph is not None:
                    start_vertex = input("Start Vertex is:")
                    end_vertex = input("End Vertex is:")
                    new_cost = input("New Cost is:")
                    result_of_setter = self.__active_graph.set_edge_info(int(start_vertex), int(end_vertex),
                                                                         int(new_cost))
                    if result_of_setter is False:
                        print("This edge does not exist")
                    else:
                        print("Cost was modified")
                else:
                    print("No instance of a graph")

            if option == '12':
                if self.__active_graph is not None:
                    start_vertex = input("Start Vertex is:")
                    end_vertex = input("End vertex is:")
                    if self.__active_graph.remove_edge(int(start_vertex), int(end_vertex)) is False:
                        print("Edge given does not exist")
                    else:
                        print("Edge was removed")

            if option == '13':
                if self.__active_graph is not None:
                    vertex_to_remove = input("Vertex you want to remove is:")
                    if self.__active_graph.remove_vertex(int(vertex_to_remove)) is False:
                        print("Vertex given does not exist")
                    else:
                        print("Vertex was removed")

            if option == '14':
                if self.__active_graph is not None:
                    self.__list_of_graph_copies.append(copy.deepcopy(self.__active_graph))
                    print("A copy of the current graph was made")
                else:
                    print("No instance of a graph")

            if option == '15':
                if self.__active_graph is not None:
                    index_of_the_copy_in_list = input("Enter the index of the graph copy in the list of copies:")
                    index_of_the_copy_in_list = int(index_of_the_copy_in_list)
                    if index_of_the_copy_in_list not in range(0, len(self.__list_of_graph_copies)):
                        print("Index given is not inside(not valid)")
                    else:
                        self.__active_graph = copy.deepcopy(self.__list_of_graph_copies[index_of_the_copy_in_list])
                        print("The specified copy was set now as the active graph")
                else:
                    print("No instance of a graph")

            if option == '16':
                if self.__active_graph is not None:
                    index_of_the_copy_in_list = input("Enter the index of the graph copy in the list of copies:")
                    index_of_the_copy_in_list = int(index_of_the_copy_in_list)
                    if index_of_the_copy_in_list not in range(0, len(self.__list_of_graph_copies)):
                        print("Index given is not inside(not valid)")
                    else:
                        self.__list_of_graph_copies.pop(index_of_the_copy_in_list)
                        print("The specified copy was removed")
                else:
                    print("No instance of a graph")

            if option == "17":
                if self.__active_graph is not None:
                    GraphExternalFunctions.write_graph_to_file("./out.txt", self.__active_graph, "d")
                    print("The graph has been written to the file")
                else:
                    print("No instance of a graph")

            if option == '18':
                vertices_number = input("Number of vertices is:")
                edges_number = input("Number of edges is:")
                result_of_generation = GraphExternalFunctions.generate_random_graph(int(vertices_number),
                                                                                    int(edges_number), "d")
                if result_of_generation is not None:
                    self.__active_graph = result_of_generation
                    print("The graph was generated randomly and set as the active graph")
                else:
                    print("The edges are way to many compared to the vertices")

            if option == 'x':
                exit()
