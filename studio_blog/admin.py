from django.contrib import admin

from .models import StudioMovies, Gallery, DuringProduction

admin.site.register(StudioMovies)
admin.site.register(Gallery)
admin.site.register(DuringProduction)
