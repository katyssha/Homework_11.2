import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        original = json.load(file)
    return original


def get_candidate(candidate_id: int):
    text = load_candidates_from_json()
    for candidate in text:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    candidates = []
    text = load_candidates_from_json()
    for candidate in text:
        if candidate["name"] == candidate_name:
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill_name):
    candidates = []
    text = load_candidates_from_json()
    for candidate in text:
        if skill_name.lower() in candidate['skills'].lower():
            candidates.append(candidate)
    return candidates
