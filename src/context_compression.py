# Context compression logic will be implemented here
def compress_context(course_list, max_items=3):
    """
    course_list: list of courses or topics
    max_items: how many important items to keep
    """

    if len(course_list) <= max_items:
        return course_list

    # Keep only most important items (simple compression)
    return course_list[:max_items]
