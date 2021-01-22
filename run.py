


with open('data', 'r') as f:
    data = f.read()


lines = data.split('\n')

players = {}

for line in lines:
    split = line.split('\t')
    if len(split) <= 2:
        break
    name = split[1].split(',')[0].strip()
    
    opponent = split[2].split(' ')[0]
    
    date = split[0].strip()
    
    if name in players.keys():
        players[name][date] = opponent
    else:
        players[name] = {date: opponent}

count = 0

for player in players.keys():
    if len(players[player]) > 1:
        count += 1
        teams = players[player].values()
        
        if len(set(teams)) != len(teams):
            print('WINNER: {} {}'.format(player, teams))
        else:
            print('{} {}'.format(player, teams))

print('Total count: {}'.format(count))
