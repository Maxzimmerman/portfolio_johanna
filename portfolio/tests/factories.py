import factory
import factory.fuzzy
from django.utils.text import slugify

from ..models import Service


class ServiceFactory(factory.django.DjangoModelFactory):
    image = factory.Faker("company")
    title = factory.Faker("sentence", nb_words=3)
    text = factory.fuzzy.FuzzyText(length=20)
    more_information = factory.fuzzy.FuzzyText(length=500)

    def slug(self):
        return slugify(self.title)

    class Meta:
        model = Service
