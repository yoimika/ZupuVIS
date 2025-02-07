from graph.graph import Graph, Node
from graph.person import Person
from configs.config import graph_config
from typing import Callable
import re

def default_set_father_and_son(
        new_nodes:list[Node],
        name2idx:dict[str, int],
        person:Person,
        person_idx: int
    ):
    father_idx = name2idx.get(person.get_father_name(), None)
    if father_idx is not None:
        # Set father
        new_nodes[person_idx].father = new_nodes[father_idx]

        # Set sons
        new_nodes[father_idx].sons.append(new_nodes[person_idx])

def qing_example_exception_father_and_son(
        new_nodes:list[Node],
        name2idx:dict[str, int],
        person:Person,
        person_idx: int,
    ):
    """ 用来处理 国某 的这个数据
    """
    father_regex = r"^国.$"
    new_nodes[person_idx].is_father_special = True
    for key, value_idx in name2idx.items():
        if re.match(father_regex, key):
            if person.is_father_beifen(new_nodes[value_idx].person):
                # Set potential father
                new_nodes[person_idx].potential_fathers.append(new_nodes[value_idx])
                # Set Son
                new_nodes[value_idx].potential_sons.append(new_nodes[person_idx])
                new_nodes[value_idx].is_son_special = True

def construct_graph_from_nodes(
        all_person: list[Person],
        exception_name: dict[str, Callable[[list[Node], dict[str, int], Person, int], None]]
    )->Graph:
    """构造Graph对象
    """
    N = len(all_person)
    g = Graph()

    name2idx = {person.get_name(): idx for idx, person in enumerate(all_person)}

    new_nodes = [Node(None) for _ in range(N)]
    for idx in range(N):
        # Set person
        person = all_person[idx]
        new_nodes[idx].person = person

    for idx in range(N):
        person = all_person[idx]
        # Set father and son
        father_name = person.get_father_name()
        if father_name not in exception_name.keys():
            default_set_father_and_son(
                new_nodes=new_nodes,
                name2idx=name2idx,
                person=person,
                person_idx=idx
            )
        else:
            exception_name[father_name](
                new_nodes=new_nodes,
                name2idx=name2idx,
                person=person,
                person_idx=idx,
            )
    
    # Set name2nodes
    setattr(g, 'nodes', new_nodes)
    # Get root
    for node in new_nodes:
        if node.father is None:
            if not node.is_son_special and not node.is_father_special:
                g.roots.append(node)
    return g


