def get_transactions(user_id: str):
    return [
        {"amount": 100, "country": "AR"},
        {"amount": 200, "country": "AR"},
    ]


def get_user_profile(user_id: str):
    return {
        "user_id": user_id,
        "name": "Test User",
    }