import json
import requests
from fastapi import HTTPException, status
from shortcut import object_as_dict
from model.sdk_counter import SdkCounter
from model.user_counter import UserCounter


def get_all_statistic_by_filter_type(filter_type, db):
    if filter_type == 'SDK':
        data = SdkCounter.get_all_sdk(db)
    elif filter_type == 'USER':
        data = UserCounter.get_all_user(db)
    else:
        raise HTTPException(
            detail="Filter type is not defined",
            status_code=status.HTTP_400_BAD_REQUEST)
    result_dict = [object_as_dict(obj) for obj in data]
    for data in result_dict:
        data.pop('id')
        data['fill_rate'] = int(data['ad_counter']) / int(data['imp_counter'])
    return json.dumps(result_dict)


def create_user_or_update_statistic(data, type, db):
    user, is_created = UserCounter\
        .get_or_create_user_by_username(data.username, db)
    if not is_created:
        UserCounter.add_user_ad_or_imp_counter(db, user, type)


def get_external_responce(url):
    return requests.get(url)
