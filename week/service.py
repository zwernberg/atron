from atron import settings
from atron import espn_service


def fetchMatchups(leagues, matchupPeriodId = '', seasonId = settings.YEAR):
    data = {
        'leagues': [],
    }
    status_code = ''

    for league in leagues:
        params = {
            'leagueId': league.league_id,
            'seasonId': seasonId,
            'matchupPeriodId': matchupPeriodId
        }

        res = espn_service.fetch('scoreboard', league.league_id, extra_params = params)
        val = res.json()
        val['metadata']['division'] = league.division
        
        # for matchup in val['scoreboard']['matchups']:
        #     players = []
        #     for team in matchup['teams']:
        #         params = {
        #             'playerId': ",".join(str(v) for v in team['playerIDs']),
        #             'useCurrentPeriodProjectedStats': True,
        #             'useCurrentPeriodRealStats': True,
        #             'includeRankings': False,
        #             'includeProjectionText': False,
        #             'includeOwnPotentialTradeTransactions': False,
        #             'includeLatestNews': False,
        #             'matchupPeriodId': matchupPeriodId
        #         }
        #         team_result = fetch('playerInfo', league.league_id, extra_params= params)
        #         players = team_result.json()['playerInfo']['players']
        #         team['players'] = players

        status_code = res.status_code
        data['leagues'].append(val)

        return {
            'data': data,
            'status_code': status_code
        }