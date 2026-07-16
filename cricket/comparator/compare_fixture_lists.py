from comparator.compare_fixture import CompareFixture
from fixture_enums import Ground
from printer.fixture_utils import get_junior_fixtures

def get_different_fixtures(source_list, target_list):
    junior_source_fixtures = get_junior_fixtures(source_list)
    junior_target_fixtures = get_junior_fixtures(target_list)
    different_fixtures = get_differences(junior_source_fixtures, junior_target_fixtures)
    different_fixtures += get_differences(junior_target_fixtures, junior_source_fixtures)
    return different_fixtures

def get_spond_different_fixtures(source_list, spond_list):
    return get_different_fixtures(get_spond_comparator(source_list), get_spond_comparator(spond_list))

def get_wpf_different_fixtures(source_list, wpf_list):
    return get_different_fixtures(get_wpf_fixtures(source_list), get_wpf_fixtures(wpf_list))

def get_spond_comparator(list_of_fixtures):
    comparator_fixtures = []
    for fixture in list_of_fixtures:
        comparator_fixture = CompareFixture(fixture)
        if comparator_fixture.is_valid():
            comparator_fixtures.append(comparator_fixture)
    return comparator_fixtures

def get_differences(source_list, target_list):
    return [f for f in source_list if f not in target_list]

def get_wpf_fixtures(fixture_list):
    wpf_fixtures = []
    for fixture in fixture_list:
        if fixture.ground == Ground.WPF:
            wpf_fixtures.append(fixture)
    return wpf_fixtures