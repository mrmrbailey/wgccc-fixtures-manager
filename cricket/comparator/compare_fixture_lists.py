from cricket_enums import FixtureType

def get_different_fixtures(source_list, target_list):
    different_fixtures = get_differences(source_list, target_list)
    different_fixtures += get_differences(target_list, source_list)
    return different_fixtures

def get_differences(source_list, target_list):
    differences = []
    for fixture in source_list:
        try:
            if fixture.fixture_type not in (FixtureType.FRIENDLY, FixtureType.SENIOR):
                if fixture == target_list[target_list.index(fixture)]:
                    pass
        except ValueError:
            differences.append(fixture)
    return differences
