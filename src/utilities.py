import json
import requests

def make_request(query, variables):

    url = "https://graphql.anilist.co"

    response = requests.post(
        url, json={"query": query, "variables": variables})

    response = json.loads(response.text)

    return response

def write_list(set):

    with open("aux.txt", "a") as f: 
        f.write("%s: \n" % (set))

def write_file(set):

    with open("aux.txt", "w") as f: 

        list = ""
        
        for key, value in set: 

            f.write("%s: %s \n" % (key, len(value)))
            f.write("\n")
            
            for info in value:
                
                list = list + str(info[1])
                f.write("{:50} {}\n".format(info[0], list))
            
                list = ""

            f.write("\n")

    format("aux.txt")

def format(file):

    with open('aux.txt', 'r') as file :
        
        filedata = file.read()

        filedata = filedata.replace("'", "")
        filedata = filedata.replace("[", "")
        filedata = filedata.replace("]", "")
        filedata = filedata.replace(", ", "\t")

    with open('aux.txt', 'w') as file:
        file.write(filedata)