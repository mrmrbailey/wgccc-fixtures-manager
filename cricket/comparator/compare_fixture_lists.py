from comparator.compare_fixture import CompareFixture
from cricket_enums import FixtureType

def get_different_fixtures(source_list, target_list):
    different_fixtures = get_differences(source_list, target_list)
    different_fixtures += get_differences(target_list, source_list)
    return different_fixtures

def get_spond_different_fixtures(source_list, spond_list):
    return get_different_fixtures(get_spond_comparator(source_list), get_spond_comparator(spond_list))

def get_spond_comparator(list_of_fixtures):
    comparator_fixtures = []
    for fixture in list_of_fixtures:
        comparator_fixture = CompareFixture(fixture)
        if comparator_fixture.is_valid():
            comparator_fixtures.append(comparator_fixture)
    return comparator_fixtures

def get_differences(source_list, target_list):
    differences = []
    for fixture in source_list:
        try:
            if fixture == target_list[target_list.index(fixture)]:
                pass
        except ValueError:
            differences.append(fixture)
    return differences
