# 4.7) given a set of projects and dependencies find the build order

from enum import Enum
from trees_and_graphs.graph import Graph
from collections import deque


class State(Enum):
    BLANK = 0
    PARTIAL = 1
    COMPLETED = 2


class Project:
    __slots__ = 'name', 'state', 'children'

    def __init__(self, data):
        self.name = data
        self.state = State.BLANK
        self.children = []

    def get_children(self):
        if len(self.children) < 1:
            return []
        return self.children


def build_order(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return dfs_order(graph.nodes)


def build_graph(projects, dependecies):
    project_nodes = []
    # graph = Graph()

    for name in projects:
        new_node = Project(name)
        project_nodes.append(new_node)

    for dependency in dependecies:
        child = find_node(project_nodes, dependency[0])
        parent = find_node(project_nodes, dependency[1])
        parent.children.append(child)

    return Graph(project_nodes)


def find_node(nodes, name):
    for node in nodes:
        if node.name == name:
            return node


def dfs_order(projects):
    stack = deque()

    for project in projects:
        if project.state == State.BLANK:
            if not do_dfs(project, stack):
                return False  # return if there's a cycle
    return stack


def do_dfs(project, stack):
    # if we find a partial node, we have a cycle and no way to build the projects
    if project.state == State.PARTIAL:
        return False

    if project.state == State.BLANK:
        project.state = State.PARTIAL
        for child in project.get_children():
            if not do_dfs(child, stack):
                return False
        project.state = State.COMPLETED
        stack.append(project)

    return True


# test code
projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]

stack = build_order(projects, dependencies)
print(stack)