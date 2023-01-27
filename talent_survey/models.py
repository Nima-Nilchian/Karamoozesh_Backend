from django.db import models
from custom_lib.models import BaseModel


class TalentSurvey(BaseModel):
    test_name = models.CharField(max_length=250)
    survey_link = models.URLField()
    result = models.URLField()
