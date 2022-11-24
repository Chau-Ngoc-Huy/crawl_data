import json

f = open("crawl/list_artist/artist_1.txt", "r")
artists = f.read().split('\n')
f.close()

size = "medium"

common_config = {
            "keywords": "",
            "limit": 100,
            "print_urls": "true",
            "size": size,
            "type": "face",
            "time": "past-year",
            "language": "English",
            "output_directory": "data/crawl_data/" + size
        }
f.close()

config = {
    "Records": []
}

for name in artists:
    print(config)
    if (name != ""):
        artist_config = common_config.copy()
        artist_config['keywords'] = name + " live stage"

        config["Records"].append(artist_config)


print(config)
json_object = json.dumps(config, indent=4)
with open("./crawl/config.json", "w") as outfile:
    outfile.write(json_object)
