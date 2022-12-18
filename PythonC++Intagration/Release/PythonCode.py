import os
import json

raw_data_full_file_path = r'U:\cppPython\Release\CS210_Project_Three_Input_File.txt'
frequency_map_file_name = r'.\frequency.dat'

def generate_frequency(clean_list_of_items):
    frequency_map = {}
    for item in clean_list_of_items:
        if item in frequency_map.keys():
            frequency_map[item] += 1
        else:
            frequency_map[item] = 1
    return frequency_map

def read_input_file(path):
    with open(path, 'r') as f:
        return f.readlines()

def get_input_file_path():
    if os.path.exists(raw_data_full_file_path):
        return raw_data_full_file_path
    else:
        path = input("Please input the file path for the chrolological items purchases data: ")
        return path

def clean(input_list):
    clean_list = []
    for item in input_list:
        if item != '\n':
            clean_list.append(item.strip())
    return clean_list

def save_frequency_map(frequency_map, file_path):
    with open(file_path, 'w') as fp:
        json.dump(frequency_map, fp)
    
def retrieve_frequency_map(file_path):
    with open(file_path, 'r') as fp:
        return json.load(fp)

def process_data(output_path):
    input_path = get_input_file_path()
    raw_data = read_input_file(input_path)
    clean_list = clean(raw_data)
    frequency_map = generate_frequency(clean_list)
    save_frequency_map(frequency_map, output_path)
    return frequency_map
        
def get_frequency_map():
    if os.path.exists(frequency_map_file_name):
        if os.path.getsize(frequency_map_file_name)>0:
            return retrieve_frequency_map(frequency_map_file_name)
        else:
           return process_data(frequency_map_file_name) 
    else:
        return process_data(frequency_map_file_name)

def list_items():
    frequencies = get_frequency_map()
    for item in frequencies.keys():
        print(item, end=" ")
        print(frequencies[item])
    

def print_item(selected_item):
    frequencies = get_frequency_map()
    try:
        frequency = frequencies[selected_item]
        print(selected_item + " " + str(frequency))
        return True
    except:
        print("Did not find " + selected_item + " in our list of items.")
        return True
   
def print_with_buffer(string):
    print(string, end="")
    for i in range(len(string), 15):
        print(" ", end="")

def print_headder():
    print("ITEMS          FREQUENCY")
    print("------------------------")

def print_histogram():
    print_headder()
    frequencies = get_frequency_map()
    for item in frequencies.keys():
        print_with_buffer(item)
        for i in range(frequencies[item]):
            print("*", end="")
        print("")