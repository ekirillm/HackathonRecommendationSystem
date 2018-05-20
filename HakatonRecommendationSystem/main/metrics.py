import numpy as np


def skills_similarity(skills_team1, skills_team2):
    return len(set(skills_team1).intersection(skills_team2)) / len(set().union(skills_team1, skills_team2))


def hakaton_experience(exp_team1, exp_team2):
    return exp_team1 or exp_team2


def ideas_metrics(count_ideas_team1, count_ideas_team2):
    return np.tanh(count_ideas_team1 + count_ideas_team2)


def programmer_ratio(p1, n1, p2, n2):
    if p1 + p2 == 0:
        return 0
    else:
        return 1 - 1 / (1 + np.exp(-(((n1 + n1) / (p1 + p2)) - 1 / 3)))
