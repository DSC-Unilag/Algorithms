import requests
import json

url = "https://api.github.com/repos/DSC-Unilag/Algorithms/contents"
response = requests.get(url)
data = json.loads(response.text)

print("| Category         | Algorithm                                                                              | Sub Category |")
print("|------------------|----------------------------------------------------------------------------------------|------------------|")

current_folder = ""
algorithm_list = ""
sub_folder = ""

def get_sub_folder_data(sub_folder_url):
    sub_folder_response = requests.get(sub_folder_url)
    sub_folder_data = json.loads(sub_folder_response.text)
    sub_algorithm_list = ""
    for sub_file in sub_folder_data:
        sub_file_name = sub_file["name"].replace(".py","")
        sub_file_name = sub_file_name.replace("_", " ")
        sub_file_name = sub_file_name.title()
        sub_file_url = sub_file["html_url"]
        sub_algorithm_list += "[" + sub_file_name + "](" + sub_file_url + ")<br>"
    return sub_algorithm_list

for item in data:
    if item["type"] == "dir":
        sub_folder_url = item["url"]
        sub_folder_response = requests.get(sub_folder_url)
        sub_folder_data = json.loads(sub_folder_response.text)
        for sub_item in sub_folder_data:
            if sub_item["type"] == "dir":
                if current_folder != "":
                    print("| " + current_folder + " | " + algorithm_list + " | " + sub_folder + " |")
                    algorithm_list = ""
                current_folder = item["name"]
                sub_folder = sub_item["name"]
                sub_folder_url = sub_item["url"]
                algorithm_list = get_sub_folder_data(sub_folder_url)
            else:
                file_name = sub_item["name"].replace(".py","")
                file_name = file_name.replace("_", " ")
                file_name = file_name.title()
                file_url = sub_item["html_url"]
                algorithm_list += "[" + file_name + "](" + file_url + ")<br>"
    else:
        file_name = item["name"].replace(".py","")
        file_name = file_name.replace("_", " ")
        file_name = file_name.title()
        file_url = item["html_url"]
        if current_folder == "":
            current_folder = "N/A"
        algorithm_list += "[" + file_name + "](" + file_url + ")<br>"

if current_folder != "":
    print("| " + current_folder + " | " + algorithm_list + " | " + sub_folder + " |")
