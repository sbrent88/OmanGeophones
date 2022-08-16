import itertools
from datetime import datetime

start = datetime.now()


def elapsed_time():
    return datetime.now() - start



def make_geophone_data_paths(geo_id, julian_day):
    """
    its annoying to make the paths, this makes it easier
    """
    paths = ['/media/sbrent/Oman3/PASSCAL/Main_deployment/DAYS/{geo_id}}/{geo_id}}.7F..GDZ.2020.{julian_day}']
    return [p.format(geo_id=geo_id, julian_day=julian_day) for p in paths]




if __name__=='__main__':
    print('Nothing to see here. You may go about our business.')
    #geo_list = [ 'A19' ,'A04']
    #make_geophone_data_paths(geo_list,10)