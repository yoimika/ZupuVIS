from typing import Self
from cn2an import cn2an

class Person:
    """ 表示族谱中的一个人，TA 应该具有以下属性：
    - 名字
    - 父辈名
    - csv 信息：dict 
        - 父辈名
        - 关系
        - 名
        - 世
        - 辈
        - 其他信息
    """
    def __init__(self, head: list[str], csv_info: list[str], id=0):
        assert len(head) == len(csv_info)
        self.csv_info: dict[str, str] = {key: value for key, value in zip(head, csv_info)}
        name = self.csv_info['名']
        self.name: str = name[:-1] if name[-1] == '公' else name
        father = self.csv_info['父辈名'] 
        self.father: str = father[:-1] if father[-1] == '公' else father
        self.id = id
    
    def get_name(self)->str:
        """ Get who am i
        """
        return self.name
    
    def get_name_with_id(self)->str:
        return self.name + f'{self.id}'
    
    def get_csv_info(self)->dict[str, str]:
        """ Get the csv info
        """
        return self.csv_info
    
    def get_father_name(self)->Self:
        return self.father
    
    def get_father_relation(self)->str:
        return self.csv_info['关系']
    
    def get_shi(self)->str:
        return self.csv_info['世']
    
    def get_bei(self)->str:
        return self.csv_info['辈']
    
    def get_info(self)->str:
        return self.csv_info['其他信息']

    def __repr__(self):
        return f"我是{self.name}, Man!"

    def is_father_beifen(self, other: Self) -> bool:
        """ 检查 other 是不是父辈的人
        """
        my_shi = self.csv_info['世'][1:-1]
        other_shi = other.csv_info['世'][1:-1]
        if cn2an(my_shi) - cn2an(other_shi) == 1:
            return True
        return False
