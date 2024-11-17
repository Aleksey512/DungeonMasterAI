import re

EMAIL_MASK = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
PASS_MASK = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[a-zA-Z\d!@#$%^&*()_+]+$"
)

# JWT TOKEN EXPIRY
FIVE_MINUTES = 60 * 5
TEN_DAYS = 60 * 60 * 24 * 10

# EVENT NAMES
USER_CREATED_EVENT_NAME = "user.created"
