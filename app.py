import utils
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def original_inf():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>')
def about_candidate(candidate_id):
    candidate = utils.get_candidate(candidate_id)
    if not candidate:
        return 'Кандидат не найден'
    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def coincidence(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skill/<skill_name>')
def collect_skills(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', skill=skill_name, candidates=candidates)


app.run(host='0.0.0.0', port=8000)
