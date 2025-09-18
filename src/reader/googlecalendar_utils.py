from src.cricket_enums import FixtureType
from datetime import datetime, timezone, date

def clean_summary(summary):
    summary = summary.replace(',', '')
    summary = remove_summary_prefix(summary)
    summary = remove_summary_suffix(summary)
    return summary

def remove_summary_prefix(summary):
    if len(summary.split(': ')) > 1:
        return summary.split(': ')[1]
    else:
        return summary

def remove_summary_suffix(summary):
    if len(summary.split(' yards')) > 1:
        return summary.split(' yards')[0][:-4]
    return summary

def get_teams(summary):
    summary = rename_teams(summary)
    summary = summary.replace(' vs ', '~')
    summary = summary.replace(' v ', '~')
    if summary.count('~') != 1:
        summary = 'Not a WGCCC Team' + '~' + summary
    return summary.split('~')

def rename_teams(summary):
    summary = summary.replace('WGCCC 1st XI', 'Saturday 1st XI')
    summary = summary.replace('WGCCC 2nd XI', 'Saturday 2nd XI')
    summary = summary.replace('WGCCC 3rd XI', 'Saturday 3rd XI')
    summary = summary.replace('WGCCC U11A', 'WGCCC U11')
    summary = summary.replace('U13-U15 match', 'WGCCC Juniors')
    summary = summary.replace('WGCCC Juniors intersquad', 'WGCCC Juniors')
    summary = summary.replace('WGCCC U11 Summer vs Cokenach CC - Under 11', 'Cokenach CC - Under 11 vs WGCCC U11 Summer')
    summary = summary.replace('WGCCC U15 Summer vs Knebworth Park CC - Under 15', 'Knebworth Park CC - Under 15 vs WGCCC U15 Summer')
    summary = summary.replace('2nd XI vs London Colney 2nd XI', 'Saturday 2nd XI vs London Colney 2nd XI')
    return summary

def get_fixture_type_from_description(description):
    if description is None:
        return None
    description = remove_preformatted_tag(description)
    description = change2025description(description)
    match description.count('~'):
        case 0:
            return FixtureType.SENIOR
        case 1|2:
            return FixtureType[description.split('~')[1].upper()]

        case _:
            return FixtureType.SENIOR

def remove_preformatted_tag(html_snippet):
    return html_snippet.removeprefix('<br>').removeprefix('<pre>').removesuffix('</pre>')

def change2025description(description):
    description = description.replace('League:', 'xxx~League~')
    description = description.replace('Cup:', 'xxx~Cup~')
    description = description.replace('Friendly:', 'xxx~Friendly~')
    return description

def get_fixture_type_from_summary(summary):
    if ' yards)' in summary:
        return FixtureType.LEAGUE
    else:
        return FixtureType.SENIOR

def clean_fixture_date(calendar_date):
    if type(calendar_date) is date:
        return datetime(calendar_date.year,calendar_date.month,calendar_date.day, tzinfo=timezone.utc)
    return calendar_date


def is_fixture_this_year(fixture_date):
    start_date = datetime(2025, 4, 1, tzinfo=timezone.utc)
    return fixture_date > start_date
