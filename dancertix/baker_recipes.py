import faker

from django.contrib.auth import get_user_model
from model_bakery.recipe import Recipe

from .models import Dancer, Reservation, Performance

User = get_user_model()

FAKE = faker.Faker()


guardian = Recipe(User, username=FAKE.user_name, email=FAKE.safe_email)


dancer = Recipe(
	Dancer,
	display_name=FAKE.name,
	first_name=FAKE.first_name,
	last_name=FAKE.last_name,
)