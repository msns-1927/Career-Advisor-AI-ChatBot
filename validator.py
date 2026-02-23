def validate_response(response):
    """
    Validates structured JSON response format.
    """
    required_keys = [
        "career_guidance",
        "skills_to_develop",
        "recommended_actions",
        "step_by_step_plan"
    ]

    if not isinstance(response, dict):
        return False

    for key in required_keys:
        if key not in response:
            return False

    return True