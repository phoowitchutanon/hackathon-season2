import re
import os
from datetime import datetime , timedelta
from typing import List


def xml_to_list(xml_file: str) -> None:
    """
    create csv file from datalist
    input: datalist
    output: None
    """
    props = ["EMPID", "PASSPORT", "FIRSTNAME", "LASTNAME", "GENDER", "BIRTHDAY",
             "NATIONALITY", "HIRED", "DEPT", "POSITION", "STATUS", "REGION"]
    with open(xml_file) as f:
        datafile = f.read()
    datalist = []
    for prop in props:
        data_prop = re.findall(rf"<{prop}>(.*?)</{prop}>", datafile)
        if prop in ["HIRED", "BIRTHDAY"]:
            data_prop = [datetime.strptime(
                datestring, '%d-%m-%Y').strftime('%Y-%m-%d') for datestring in data_prop]
        datalist.append(data_prop)
    return list(zip(*datalist))


def datalist_to_csv(datalist: List[tuple], csv_file: str) -> None:
    """
    create csv file from datalist
    input: datalist
    output: None
    """
    props = ["EMPID", "PASSPORT", "FIRSTNAME", "LASTNAME", "GENDER", "BIRTHDAY",
             "NATIONALITY", "HIRED", "DEPT", "POSITION", "STATUS", "REGION"]
    with open(csv_file, 'a') as f:
        f.truncate(0)
        f.write(','.join(props) + '\n')
        for data in datalist:
            f.write(','.join(data) + '\n')
    print("done !")


def delete_anomaly_status(datalist: List[tuple]) -> List[tuple]:
    """Delete anomaly status from datalist
    input: datalist
    output: datalist
    """
    filtered_data = list(filter(lambda x: x[10] != '0', datalist))
    return filtered_data


def filter_positions(datalist: List[tuple], positions: List[str]) -> List[tuple]:
    filtered_data = list(filter(lambda x: x[9] in positions, datalist))
    return filtered_data


def filter_hire_time(year: int, datalist: List[tuple]) -> List[tuple]:
    """
    filter hire time by year
    input: year, datalist
    output: datalist
    """
    current_time = datetime.now()
    base_time = current_time - timedelta(days=365*year)
    filtered_data = list(filter(lambda x: datetime.strptime(
        x[7], '%Y-%m-%d') < base_time, datalist))
    return filtered_data


def _find_duplicate_employee_id(datalist: List[tuple]) -> List[tuple]:
    """
    find duplicate employee id
    input: datalist
    output: index of duplicate employee id
    """
    seen_data = set()
    unique_data = list()
    duplicate_data = set()
    duplicate_index = list()
    for index, data in enumerate(datalist):
        employee_data = data[0]
        if employee_data not in seen_data:
            seen_data.add(employee_data)
            unique_data.append(index)
        else:
            duplicate_data.add(employee_data)
            duplicate_index.append(index)

    return duplicate_index


def _find_duplicate_passport(datalist: List[tuple]) -> List[tuple]:
    """
    find duplicate passport
    input: datalist
    output: datalist
    """
    seen_data = set()
    unique_data = list()
    duplicate_data = set()
    duplicate_index = list()
    for index, data in enumerate(datalist):
        passport_data = data[1]
        if passport_data not in seen_data:
            seen_data.add(passport_data)
            unique_data.append(index)
        else:
            duplicate_data.add(passport_data)
            duplicate_index.append(index)

    return duplicate_index


def remove_duplicate_employee_id(datalist: List[tuple]) -> List[tuple]:
    """
    remove duplicate passport data
    input: datalist
    output: datalist
    """
    try :
        filtered_datalist = datalist.copy()
        for index in sorted(_find_duplicate_employee_id(datalist), reverse=True):
            del filtered_datalist[index]
        return filtered_datalist
    except :
        pass


def remove_duplicate_passport(datalist: List[tuple]) -> List[tuple]:
    """
    remove duplicate passport data
    input: datalist
    output: datalist
    """
    try :
        filtered_datalist = datalist.copy()
        for index in sorted(_find_duplicate_passport(datalist), reverse=True):
            del filtered_datalist[index]
        return filtered_datalist
    except :
        pass


def Clean_data(datalist: List[tuple]) -> List[tuple]:
    """
    clean data
    input: datalist
    output: datalist
    """
    filtered_data = delete_anomaly_status(datalist)
    filtered_data = filter_positions(filtered_data, ['Airhostess', 'Pilot', 'Steward'])
    filtered_data = filter_hire_time(3, filtered_data)
    filtered_data = remove_duplicate_employee_id(filtered_data)
    filtered_data = remove_duplicate_passport(filtered_data)
    return filtered_data


def _unique(input_list) -> list:
    unique_list = []
    for x in input_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def country_seperate_to_csv(datalist: List[tuple], save_dir) -> None:
    """
    create csv file seperate by country
    input: datalist, country
    output: None
    """
    props = ["EMPID", "PASSPORT", "FIRSTNAME", "LASTNAME", "GENDER", "BIRTHDAY",
             "NATIONALITY", "HIRED", "DEPT", "POSITION", "STATUS", "REGION"]

    country_list = _unique([x[6] for x in datalist])
    for country in country_list:
        data_list_filter = list(filter(lambda x: x[6] == country, datalist))
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        with open(f'{save_dir}/result_{country}.csv', 'a') as f:
            f.truncate(0)
            f.write(','.join(props) + '\n')
            for i in data_list_filter:
                f.write(','.join(i) + '\n')