from django.db import models


CATEGORY_CHOICES = (
    ('A', 'ACTION'),
    ('D', 'DRAMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),
)

LANGUAGE = (
    ('EN', 'ENGLISH'),
    ('TA', 'TAGALOG')
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED')
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="movies")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    laguage = models.CharField(choices=LANGUAGE, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_production = models.DateField()
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

"""
--Movie
    -title
    -description
    -tags
    -views
    -image
    -category
    -language
    -year
    -status
    -download links
    -watch links
    
    -related movies
--search

"""