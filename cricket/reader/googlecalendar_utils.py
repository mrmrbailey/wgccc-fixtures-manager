from enum import StrEnum

from fixture_enums import FixtureType
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
    summary = summary.replace(' vs ', '~')
    summary = summary.replace(' v ', '~')
    if summary.count('~') != 1:
        summary = 'Not a WGCCC Team' + '~' + summary
    return summary.split('~')

def is_postponed(summary):
    return get_notes(summary) == Notes.POSTPONED

def get_notes(summary):
    if len(summary.split(': ')) > 1:
        return Notes.get_value(summary.split(': ')[0])
    else:
        return None

def get_fixture_type_from_description(description):
    if description is None:
        return None
    description = remove_preformatted_tag(description)
    match description.count('~'):
        case 0:
            return FixtureType.SENIOR
        case 1|2:
            return FixtureType[description.split('~')[1].upper()]
        case _:
            return FixtureType.SENIOR

def remove_preformatted_tag(html_snippet):
    return html_snippet.removeprefix('<br>').removeprefix('<pre>').removesuffix('</pre>')

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
    start_date = datetime(2026, 4, 1, tzinfo=timezone.utc)
    return fixture_date > start_date

class Notes(StrEnum):
    ASTRO = 'Astro'
    ASTRO_MAYBE = 'Astro?'
    CANCELLED = 'Cancelled'
    POSTPONED = 'Postponed'
    UNKNOWN = 'Unknown'

    @classmethod
    def get_value(cls, value):
        for k, v in cls.__members__.items():
            if v.value == value:
                return v
        else:
            return Notes.UNKNOWN
