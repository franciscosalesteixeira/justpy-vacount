from src.utilities import *

class VA:

    def __init__(self, username):
        self.username = username
        self.total_va = {}
        self.sorted_va = {}
        self.info_va = {}
        self.finished = False

    def get_user(self):
        query = '''
                    query ($userName: String){
                        User(search:$userName){
                            name
                        }
                        MediaListCollection(userName: $userName, type: ANIME, status: COMPLETED) {
    						lists {
    							name
    							isCustomList
    							isSplitCompletedList
    							status
    							}
  						}
                    }
                '''
        variables = {
            "userName": self.username,
        }

        response = make_request(query, variables)

        return response

    def get_info(self):

        for page in range(20):

            if not self.finished:

                page += 1

                query = '''

                    query ($userName: String, $page: Int) {
                        MediaListCollection(userName: $userName, type: ANIME, status: COMPLETED) {
                            lists {
                                entries {
                                    media {
                                        id
                                        title {
                                            romaji
                                        }
                                        characters (page: $page){
                                            edges{
                                                node{
                                                    name {
                                                        full
                                                    }
                                                    siteUrl
                                                    image {
                                                  	  large
                                                  	}
                                                }
                                                voiceActors (language: JAPANESE){
                                                    name {
                                                        full
                                                    }
                                                    siteUrl
                                                    image {
                                                  	  large
                                                  	}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }

                    '''

                variables = {
                    "userName": self.username,
                    "page": page
                }

                response = make_request(query, variables)

                total_entries = len(
                    response['data']['MediaListCollection']['lists'][0]['entries'])

                for entry in range(total_entries):

                    title_id = [response['data']['MediaListCollection']['lists'][0]['entries'][entry]['media']['title']['romaji'],
                                response['data']['MediaListCollection']['lists'][0]['entries'][entry]['media']['id']]

                    total_info = response['data']['MediaListCollection']['lists'][
                        0]['entries'][entry]['media']['characters']['edges']

                    if total_info:

                        for set in total_info:

                            if set['node']:

                                char_info = [set['node']['name']
                                             ['full'], set['node']['siteUrl'], title_id, set['node']['image']['large']]

                                if set['voiceActors']:

                                    va_info = set['voiceActors'][0]['name']['full'], set['voiceActors'][0]['siteUrl'], set['voiceActors'][0]['image']['large']

                                    if va_info in self.total_va.keys():
                                        self.total_va[va_info].append(
                                            char_info)

                                    else:
                                        self.total_va[va_info] = [char_info]

                    else:
                        self.finished = True

            else:
                break

    def info_url(self):

        self.get_info()

        infoaux = []

        for k in self.total_va:

            for v in self.total_va[k]:

                va = (k[0], k[1], k[2])
                info = [v[0], v[1], v[3]]

                if v[0] not in infoaux:

                    infoaux.append(v[0])

                    if va in self.info_va.keys():
                        self.info_va[va].append(info)

                    else:
                        self.info_va[va] = [info]

        return sorted(self.info_va.items(),
                   key=lambda v: len(v[1]), reverse=True)

    def output(self):

        self.get_info()

        infoaux = []

        for k in self.total_va:

            for v in self.total_va[k]:

                va = k[0]
                info = [v[0], v[2][0]]

                if v[0] not in infoaux:

                    infoaux.append(v[0])

                    if va in self.sorted_va.keys():
                        self.sorted_va[va].append(info)

                    else:
                        self.sorted_va[va] = [info]

                else:

                    if va in self.sorted_va.keys():

                        for i, value in enumerate(self.sorted_va[va]):

                            if value[0] == info[0]:

                                value[1] = value[1] + " · " + info[1]
                                self.sorted_va[va][i] = [value[0], value[1]]

        write_file(sorted(self.sorted_va.items(),
                   key=lambda v: len(v[1]), reverse=True))
