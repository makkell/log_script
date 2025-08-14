import json
from tabulate import tabulate
from datetime import datetime
import argparse

def unpack(data):
    return [[endpoint, values['count'], values['response_time']] for endpoint, values in data.items()]


def print_table(table, headers):
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


def read_log(file_paths, date=None):
    files = file_paths.split()
    data_dict = {}

    date = date.split('-') if date else None
    start_date = datetime.strptime(f"{date[0]}.2025", '%d.%m.%Y') if date else None
    end_date = datetime.strptime(f"{date[1]}.2025", '%d.%m.%Y') if date and len(date) > 1 else None
    for file in files:
        with open(file) as log_file:
            for line in log_file:
                if not line:
                    continue
                try:
                    data_log = json.loads(line)
                    ts = datetime.fromisoformat(data_log['@timestamp']).replace(tzinfo=None)
                    if date and end_date:
                        if not (start_date <= ts <= end_date):
                            continue
                    elif date:
                        if not (start_date.day == ts.day):
                            continue
                    url = data_log['url']
                    if url not in data_dict:
                        data_dict[url] = {'count': 0, 'response_time': 0}
                    data_dict[url]['count'] += 1
                    data_dict[url]['response_time'] += data_log['response_time']
                except Exception as e:
                    print(f'Ошибка {e}')
            for url in data_dict:
                if data_dict[url]['count'] != 0:
                    data_dict[url]['response_time'] = data_dict[url]['response_time'] / float(data_dict[url]['count'])
    return data_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Анализ логов")
    parser.add_argument('--files', help="Файлы логов через пробел", type=str)
    parser.add_argument('--date', help="Дата в формате dd.mm или диапазон dd.mm-dd.mm", type=str)
    args = parser.parse_args()

    headers = ['url', 'total', 'avg_response_time']
    data = unpack(read_log(args.files, date=args.date))
    print_table(data, headers)