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
    summary = summary.replace('WGCCC 1st XI', 'Saturday 1st XI')
    summary = summary.replace('WGCCC 2nd XI', 'Saturday 2nd XI')
    summary = summary.replace('WGCCC 3rd XI', 'Saturday 3rd XI')
    summary = summary.replace('WGCCC U11A', 'WGCCC U11')
    if summary.count('~') != 1:
        summary = 'Not a WGCCC Team' + '~' + summary
    return summary.split('~')

def get_fixture_type_from_description(description):
    if description is None:
        return 'Unknown'
    description = remove_preformatted_tag(description)
    description = change2025description(description)
    match description.count('~'):
        case 0:
            return 'Senior'
        case 1|2:
            return description.split('~')[1]
        case _:
            return 'Senior'

def remove_preformatted_tag(html_snippet):
    return html_snippet.removeprefix('<br>').removeprefix('<pre>').removesuffix('</pre>')

def change2025description(description):
    description = description.replace('League:', 'xxx~League~')
    description = description.replace('Cup:', 'xxx~Cup~')
    description = description.replace('Friendly:', 'xxx~Friendly~')
    return description

def get_fixture_type_from_summary(summary):
    if ' yards)' in summary:
        return 'League'
    else:
        return 'Senior'

def clean_fixture_date(calendar_date):
    if type(calendar_date) is date:
        return datetime(calendar_date.year,calendar_date.month,calendar_date.day, tzinfo=timezone.utc)
    return calendar_date


def is_fixture_this_year(fixture_date):
    start_date = datetime(2025, 4, 1, tzinfo=timezone.utc)
    return fixture_date > start_date
