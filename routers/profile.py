from fastapi import APIRouter
from models.programmer_profile import Programmer_Profiles

router = APIRouter()

programmer_profiles = [
    {
        "id": 1,
        "username": "torvalds",
        "language_1": "C",
        "language_2": "C++",
        "language_3": "",
        "Repository_Most_Metged_Pull_Requests_1": "linux",
        "Repository_Most_Metged_Pull_Requests_2": "uemacs",
        "Repository_Most_Metged_Pull_Requests_3": "libdc-for-dirk",
    },
    {
        "id": 2,
        "username": "mojombo",
        "language_1": "Ruby",
        "language_2": "JavaScript",
        "language_3": "CSS",
        "Repository_Most_Metged_Pull_Requests_1": "god",
        "Repository_Most_Metged_Pull_Requests_2": "Chronic",
        "Repository_Most_Metged_Pull_Requests_3": "mustache.erl",
    },
    {
        "id": 3,
        "username": "dhh",
        "language_1": "Ruby",
        "language_2": "CSS",
        "language_3": "",
        "Repository_Most_Metged_Pull_Requests_1": "textmate-rails-bundle",
        "Repository_Most_Metged_Pull_Requests_2": "ia_typora",
        "Repository_Most_Metged_Pull_Requests_3": "conductor",
    },
        {
        "id": 4,
        "username": "tenderlove",
        "language_1": "Ruby",
        "language_2": "Vim Script",
        "language_3": "C",
        "Repository_Most_Metged_Pull_Requests_1": "tenderjit",
        "Repository_Most_Metged_Pull_Requests_2": "rails_autolink",
        "Repository_Most_Metged_Pull_Requests_3": "tinygql",
    }
]

@router.get('/user-insights')
def get_username():
    return programmer_profiles

@router.get('/user-insights/:{username}')
def get_username(username: str):
    return list(filter(lambda item: item['username'] == username, programmer_profiles))

@router.post('/user-insights')
def add_profile(programmer_profile: Programmer_Profiles):
    programmer_profiles.append(programmer_profile)
    return programmer_profiles

@router.put('/user-insights/:{username}')
def update_profile(username: str, programmer_profile: Programmer_Profiles):
    for index, item in enumerate(programmer_profiles):
        if item['username'] == username:
            programmer_profiles[index]["language_1"] = programmer_profile.language_1
            programmer_profiles[index]["language_2"] = programmer_profile.language_2
            programmer_profiles[index]["language_3"] = programmer_profile.language_3
            programmer_profiles[index]["Repository_Most_Metged_Pull_Requests_1"] = programmer_profile.Repository_Most_Metged_Pull_Requests_1
            programmer_profiles[index]["Repository_Most_Metged_Pull_Requests_2"] = programmer_profile.Repository_Most_Metged_Pull_Requests_2
            programmer_profiles[index]["Repository_Most_Metged_Pull_Requests_3"] = programmer_profile.Repository_Most_Metged_Pull_Requests_3
    return programmer_profiles

@router.delete('/user-insights/:{username}')
def delete_profile(username: str):
    for item in programmer_profiles:
        if item['username'] == username:
            programmer_profiles.remove(item)
    return programmer_profiles