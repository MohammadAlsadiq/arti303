"""TODO: describe what this module is for."""
# giving grade for gpa


def letter_grade(gpa):
    """TODO: describe what this function does."""
    # TODO: your if/elif chain here
    if gpa>=4.5:
        return "A"
    elif gpa>=3.5:
        return "B"
    elif gpa>=2.5:
        return "C"
    elif gpa>=1.5:
        return "D"
    else:
        return "F"   
    pass
