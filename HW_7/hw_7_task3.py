# from pprint import pprint

catalog_name_ = 'catalog_task3'
res_file = 'result_task3.txt'


def read_file(file_name: str) -> tuple:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
        lines.insert(0, len(lines))
    return tuple(lines)


def get_data(catalog_name):
    import os
    base_path = os.getcwd()
    catalog_path = os.path.join(base_path, catalog_name)
    files_list = os.listdir(catalog_path)
    res = {f: read_file(os.path.join(catalog_path, f)) for f in files_list}
    sort_res = sorted(res.items(), key=lambda x: x[1][0], reverse=False)
    return dict(sort_res)


def write_data(catalog_name: str, file_name: str):
    with open(file_name, 'a', encoding='utf-8') as file:
        for k, v in get_data(catalog_name).items():
            file.write(f'{k}\n')
            for line in v:
                file.write(f'{line}\n')


# pprint(get_data(catalog_name_), width=120, sort_dicts=False)
write_data(catalog_name_, res_file)
