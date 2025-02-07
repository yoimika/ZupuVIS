import typing
import csv
import re
import random

def clean_string(input: str)->str:
    trimmed_str = input.strip()
    cleaned_str = ' '.join(trimmed_str.split())
    return cleaned_str

def random_get_list(input: list[typing.Any])->typing.Any:
    assert isinstance(input, list)
    idx = random.randint(0, len(input)-1)
    return input[idx]

def raw_extract_list(input: list[str])->list[list[str]]:
    extracted_list = []
    beifen = ''
    xxshi = ''
    for item in input:
        match_result = re.search("第.*世", item)
        if match_result:
            xxshi = match_result.group()
            beifen = re.findall("“.”字辈", item)[0]
        else:
            splited_item = item.split()
            try:
                content = [
                    splited_item[0],
                    splited_item[1],
                    xxshi,
                    beifen,
                    ' '.join(splited_item[2:])
                ]
                extracted_list.append(content)
            except IndexError as e:
                print(f"Error: {e}")
                print(splited_item)
    return extracted_list

def filter_father_name(input_str: str)->list[str, str]:
    """把比如“xx长子”这个变为[“xx”,“长子”],第二个可能为 None
    """
    regex_pattern = r"[大长次一二三四五六抚]?[子女]$"

    father_name, diwei = None, None
    result = re.findall(regex_pattern, input_str)
    assert len(result) <= 1
    if len(result) == 1:
        diwei = result[0]
        father_name = input_str[:-len(diwei)]
    else:
        father_name = input_str
    return father_name, diwei

def filter_father_name_list(input_list: list[list[str]])->list[list[str]]:
    """ 将没有处理的父亲名字处理好
    """
    ret_list = []
    for list_item in input_list:
        father_name, diwei = filter_father_name(list_item[0])
        ret_list.append( [father_name, diwei] + list_item[1:] )
    return ret_list

def csv_save(
        fp: str,
        head: list[str],
        content: list[list[str]],
        delimiter=',',
        newline="",
        encoding='utf-8'
    ):
    with open(fp, mode='w', newline=newline, encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows([head] + content)

def extract_csv(
        fp: str,
        encoding: str='utf-8',
        delimiter: str=';',
        newline: str='',
    )->tuple[list[str], list[list[str]]]:
    """ Extract info from csv 
    return head and content
    """
    with open(fp, encoding=encoding, newline=newline) as file:
        reader = csv.reader(file, delimiter=delimiter)
        head = next(reader)
        content = [row for row in reader]
    return head, content


if __name__ == '__main__':
    test_str = ' aldsjf  lkaldsf    lkadsfl \n'
    print(f"-->{clean_string(test_str)}<--")