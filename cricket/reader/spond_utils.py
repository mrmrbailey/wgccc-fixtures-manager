def get_teams(matchup):
    matchup = matchup.replace(' (H) - ', '~').replace(' (A)', '')
    if matchup.count('~') != 1:
        matchup = 'Not a WGCCC Team' + '~' + matchup
    return matchup.split('~')
