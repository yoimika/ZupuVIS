from graph.person import Person
from typing import Any, TypeVar, Self, Union

T_Var = TypeVar('T')

class Node:
    """ Person wrapper
    """
    def __init__(self, person: Person):
        self.person: Person = person
        self.father: Node = None
        self.sons: list[Node] = []
        self.is_father_special: bool = False
        self.is_son_special: bool = False
        self.potential_fathers: list[Node] = []
        self.potential_sons: list[Node] = []

    
    def get_sons(self, include_potential=False, only_potential=False)->list[str]:
        """ Get sons
        """
        return _get_attri(
            self.sons,
            self.potential_sons,
            self.is_son_special,
            include_potential,
            only_potential
        )
    
    def get_father(self, include_potential=False, only_potential=False)->Union[list[str], str]:
        if not include_potential and not only_potential:
            return self.father
        return _get_attri(
            [self.father],
            self.potential_fathers,
            self.is_father_special,
            include_potential,
            only_potential
        )
    
    def __get_hash_id__(self):
        return self.person.get_name_with_id()

    def __hash__(self):
        return hash(self.__get_hash_id__())
    
    def __eq__(self, other: Self):
        return self.__get_hash_id__() == other.__get_hash_id__()
        


class Graph:
    def __init__(self):
        self.roots: list[Node] = []
        self.nodes: list[Node] = []
    
    def bfs(self, verbose_son=False, include_potential=False, only_potential=False):
        """Generator bfs, verbose_son -> if searched before add it also.
        """
        yield from _bfs(
            self.roots,
            verbose_son=verbose_son,
            include_potential=include_potential,
            only_potential=only_potential
        ) 


def _bfs(
        roots: list[Node],
        verbose_son=False,
        include_potential=False,
        only_potential=False
    ):
        queue = roots
        mem = set(roots)
        while len(queue) != 0:
            loop_sons = []
            curr_node = queue.pop(0)
            sons = curr_node.get_sons(include_potential, only_potential)
            for son in sons:
                if son not in mem:
                    mem.add(son)
                    queue.append(son)
                    loop_sons.append(son)
                    continue
                if not verbose_son:
                    loop_sons.append(son)
            yield curr_node, loop_sons
    

def _get_attri(
        attri: list[T_Var],
        potential_attri: list[T_Var],
        is_special: bool,
        include_potential:bool=False, 
        only_potential:bool=False
    )->list[T_Var]:
    if is_special:
        if only_potential:
            return potential_attri
        if include_potential:
            return attri + potential_attri
    return attri