# Recommendation logic will be implemented here
def recommend_learning_path(current_skills, target_skill):
    """
    current_skills: list of skills user already has
    target_skill: skill user wants to learn
    """

    skill_map = {
        "Python": ["Basics", "Data Types", "Loops", "Functions"],
        "Data Science": ["Python", "NumPy", "Pandas", "Visualization"],
        "Web Development": ["HTML", "CSS", "JavaScript"]
    }

    if target_skill not in skill_map:
        return "Target skill not found"

    path = []
    for skill in skill_map[target_skill]:
        if skill not in current_skills:
            path.append(skill)

    return path

