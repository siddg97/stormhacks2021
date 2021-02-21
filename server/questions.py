import string
from constants import sample

"""
General Question Pool:
- Tell me about yourself?
- What yo know about our company?
- What do you understand about the role?
- Why are you interested in working at our company?
- What motivates you in a job?

"""

technical_skill_list = [
    "PHP",
    "HTML",
    "CSS",
    "C++",
    "C",
    "Java",
    "SQL",
    "MongoDB",
    "React-native",
    "AWS",
    "Azure",
    "Docker",
    "Kubernetes",
    "JIRA",
    "Visual Studio",
    "GCP",
    "Vue.js",
    "VueJS",
    "Object-Oriented",
    "Git",
    "HTML5",
    "CSS3",
    "Sass",
    "Bootstrap",
    "jQuery",
    "JavaScript",
    "MVVM",
    "Angular",
    "React",
    "APIs",
    "MySQL",
    "PostgreSQL",
    "MariaDB",
    "Google Analytics",
    "Agile",
    "Laravel",
    "AWS",
    "Typescript",
    "Nodejs",
    "CI",
    "CD",
]

soft_skill_list = [
    "time management",
    "planning",
    "management",
    "organization",
    "troubleshooting",
    "team",
    "teamwork",
    "conflict resolution",
    "behavioural",
    "quick learning",
]

tech_question_templates = [
    "Tell me about a time you used *?",
    "Have you much time have you been using * for?"
]

soft_question_templates = [
    "Tell me about a time you demonstrated * skills?",
]

def match_skill(description):
    def match_keyword(kw):
        words = description.lower().split()
        table = str.maketrans('', '', string.punctuation)
        stripped_sample = [word.translate(table) for word in words]
        count = 0
        for word in stripped_sample:
            if kw.lower() == word:
                count += 1
        return {
            'count': count,
            'skill': kw,
        }
    return match_keyword

def process_tech_skills(text):
    match_technical = list(map(match_skill(text), technical_skill_list))
    sorted_match = sorted(match_technical, key=lambda k: -k['count'])
    return sorted_match

def process_soft_skill(text):
    match_soft = list(map(match_skill(text), soft_skill_list))
    sorted_match = sorted(match_soft, key=lambda k: -k['count'])
    return sorted_match

def gen_questions(matches, templates, limit=3):
    filtered = list(filter(lambda m: int(m['count']) > 0, matches))
    skills = list(map(lambda m: m['skill'], filtered))
    questions = []
    for i in range(len(skills)):
        for j in range(len(templates)):
            questions.append(templates[j].replace('*', skills[i]))
    return questions

