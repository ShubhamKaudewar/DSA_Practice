
if __name__ == '__main__':
    import requests
    import json

    team = 'Barcelona'
    year = 2011
    goals = 0

    for tm in ['team1', 'team2']:
        print("team:", tm)
        url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&tm=' + team + '&page=1'
        response = requests.request('GET', url, headers={}, data={})
        total_pages = json.loads(response.text.encode('utf8'))['total_pages']

        for i in range(1, total_pages + 1):
            print("i: ", i, "/", total_pages)
            url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&tm=' + team + '&page=' + str(i)
            response = requests.request('GET', url, headers={}, data={})
            r = json.loads(response.text.encode('utf8'))
            r_data = r['data']

            for record in r_data:
                goals += int(record[tm + 'goals'])

    print(goals)


