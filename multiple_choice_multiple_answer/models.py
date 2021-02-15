from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from django.forms.widgets import CheckboxSelectMultiple
import re

author = 'Yaoni'

doc = """
Multiple choice, multiple answer fields.
"""


class Constants(BaseConstants):
    name_in_url = 'multiple_choice_multiple_answer'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    love_this = models.StringField(
        label="Easily choose multiple answers!",
        widget=CheckboxSelectMultiple(
            choices=(
                # answer 1 and 2 shall be the correct ones
                (1, "This is awesome!"),
                (2, "Great!"),
                (3, "Hm okay"),
                (4, "Don't like it (really?💣)"),
            )
        ),
    )

    def love_this_error_message(self, val):
        # remember that 1 and 2 are correct
        pattern = re.compile("^\[\'1\', \'2\'\]$")
        if pattern.search(value) == None:
            return "Sorry, wrong answers. Try the first two options."
