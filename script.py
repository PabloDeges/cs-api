import json
# meow :3
better_dict = {}

# with open("all_sorted_data.json") as f:
#     data = json.load(f)

#     for x in data:
#         name_unformat = x["name"]
#         name_format = name_unformat.replace(" | ", "_").replace(" ", "_")
#         better_dict[name_format] = x
with open("cs_data.json", "r") as f:
    data = json.load(f)
    weapon_arr = []
    for x in data:
        skin = data[x]
        if skin["weapon"] in better_dict.keys():
            better_dict[skin["weapon"]].append(skin)
            
        else:
            better_dict[skin["weapon"]] = []
        

        

        


with open("cs_weapon_data.json", "w") as c:
    json.dump(better_dict, c)



