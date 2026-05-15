from os import path

def get_data_path():
    return path.dirname(__file__) + '/../../data/'

def get_google_calendar_path():
    return get_data_path() + 'google-calendar/'

def get_play_cricket_path():
    return get_data_path() + 'play-cricket/'

def get_spond_path():
    return get_data_path() + 'spond/'

def get_wpf_path():
    return get_data_path() + 'wpf/'