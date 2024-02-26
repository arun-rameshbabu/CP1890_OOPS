from dataclasses import dataclass
import csv

if __name__ == "__main__":
    FILENAME = "all_sales.csv"

sales_list = [[2021, 2, 15, 3245.0]]


def write_list(sales_list):
    with open("all_sales.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sales_list)


def read_list(FILENAME):
    sales_list = []
    with open(str(FILENAME), newline='') as file_handler:
        reader = csv.reader(file_handler)
        for row in reader:
            sales_list.append([int(row[0]), int(row[1]), int(row[2]), float(row[3])])
        return sales_list


def write_txt(new_data):
    with open("imported_data.txt",'a') as outfile_handle:
        outfile_handle.write(f"{new_data}\n")


def read_txt():
    with open("imported_data.txt",'r') as file:
        sales_log = []
        for name in file:
            name = name.replace('\n', "")
            sales_log.append(name)
        return sales_log

@dataclass
class Region:
    pass


@dataclass
class File:
    region: Region
    filename: str = "all_sales.csv"
