class BaseConfig:
    def __init__(self):
        self.Unknown_token = "<Unknown>"
        self._default_csv_fp = './data/zupu.csv'
        self._default_txt_fp = './data/info.txt'
        self.csv_encoding = 'gbk'
        self.delimiter = ';'
        self.newline = ""


class Txt2csvConfig(BaseConfig):
    def __init__(self):
        super().__init__()
        self.save_fp = self._default_csv_fp
        self.txt_fp  = self._default_txt_fp


class GraphConfig(BaseConfig):
    def __init__(self):
        super().__init__()


class VisConfig(BaseConfig):
    def __init__(self):
        super().__init__()
        self.csv_fp = self._default_csv_fp


txt2csv_config = Txt2csvConfig()
graph_config = GraphConfig()
vis_config = VisConfig()