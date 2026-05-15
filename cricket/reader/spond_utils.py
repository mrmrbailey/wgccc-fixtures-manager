import re

availability_regex = re.compile('.*\(H\).*\(A\)')

def get_teams(matchup):

    if re.search(availability_regex, matchup):
        matchup = matchup.replace(' (H) - ', '~').replace(' (A)', '')
    else:
        matchup = matchup.replace(' – ', '~')
    if matchup.count('~') != 1:
        matchup = 'Not a WGCCC Team' + '~' + matchup
    return matchup.split('~')
