import os

import pandas as pd
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE


class ExcelExtractor(object):
    def __init__(self, path: str, name: str):
        self.file_path = f"{path}/{name}.xlsx"
        self.header = []

        if not os.path.exists(path):
            os.makedirs(path)

    def flatten(self, data: list[dict]) -> list[dict]:
        res = []
        for data_dic in data:
            flat_dic = {}
            for key, val in data_dic.items():
                if isinstance(val, dict):
                    for inner_key, inner_val in val.items():
                        flat_dic[inner_key] = inner_val
                elif isinstance(val, list):
                    if val and isinstance(val[0], dict):
                        # 정규화 필요한 데이터는 우선 개수만 저장
                        flat_dic[key] = len(val)
                    else:
                        flat_dic[key] = ",".join(val)
                elif isinstance(val, str):
                    flat_dic[key] = ILLEGAL_CHARACTERS_RE.sub(r"", val)
                else:
                    flat_dic[key] = val
            res.append(flat_dic)
        return res

    def _set_header(self, data: dict):
        header = []
        for key, val in data.items():
            if isinstance(val, dict):
                for key in val.keys():
                    header.append(key)
            else:
                header.append(key)
        self.header = header

    def save_as_excel(self, data: list[dict]):
        self._set_header(data[0])
        rows = self.flatten(data=[dic for dic in data if dic])

        try:
            df = pd.read_excel(self.file_path)
        except FileNotFoundError:
            df = pd.DataFrame(columns=self.header)

        new_rows = pd.DataFrame(rows)
        df = pd.concat([df, new_rows], ignore_index=True)

        df.to_excel(self.file_path, index=False, engine="openpyxl")
