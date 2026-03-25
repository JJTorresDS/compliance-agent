import sqlite3


def get_transactions(user_id: str):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT amount, country, date FROM transactions WHERE user_id = ?",
        (user_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {"amount": r[0], "country": r[1], "date": r[2]}
        for r in rows
    ]


def get_user_profile(user_id: str):
    # Still mocked (fine for MVP)
    return {
        "user_id": user_id,
        "name": "John Doe",
    }