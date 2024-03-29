# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jK-HzmO6vYacFNh210SofByov5L5QsgY
"""

!pip install zenrows
from zenrows import ZenRowsClient
import json
import csv

client = ZenRowsClient("e159af9d7c4711e69fff5a6df159ec3f7de4393c")

def get_url(place_code):
    url_prefix = "https://www.tripadvisor.in/Attractions-"
    url_suffix = ".html"
    current_url = f"{url_prefix}{place_code}{url_suffix}"
    return current_url

def get_item_details(client, current_url):
    params = {"js_render": "true", "premium_proxy": "true", "autoparse": "true"}
    response = client.get(current_url, params=params)

    try:
        response.raise_for_status()
        json_data = response.json()
        item_list = json_data[2]
        item_details = [
            {
                "position": item.get("position", ""),
                "name": item.get("name", ""),
                "url": item.get("url", "")
            }
            for item in item_list.get("itemListElement", [])
        ]
        return item_details
    except Exception as e:
        print(f"Error retrieving item details: {e}")
        return None

def write_to_csv(item_details, user_input_place):
    csv_prefix = "top_Attractions_"
    csv_file = f"{csv_prefix}{user_input_place}.csv"

    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ["Position", "Name", "URL"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for details in item_details:
            writer.writerow({"Position": details['position'], "Name": details['name'], "URL": details['url']})

places = {
    "Varanasi": "g297685-Activities-oa0-Varanasi_Varanasi_District_Uttar_Pradesh",
    "Srinagar": "g297623-Activities-oa0-Srinagar_Srinagar_District_Kashmir_Jammu_and_Kashmir",
    "Udaipur": "g297672-Activities-oa0-Udaipur_Udaipur_District_Rajasthan",
    "Thanjavur": "g424926-Activities-oa0-Thanjavur_Thanjavur_District_Tamil_Nadu",
    "Shimla": "g304552-Activities-oa0-Shimla_Shimla_District_Himachal_Pradesh"
}

user_input_place = input("Enter the place to visit:/n1.Varanasi/n2.Srinagar/n3.Udaipur/n4.Thanjavur/n5.Shimla/n ")
place_code = places[user_input_place]
current_url = get_url(place_code)
item_details=get_item_details(client,current_url)
write_to_csv(item_details,user_input_place)