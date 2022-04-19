from django.contrib import admin
from .models import Profile, NeighbourHood, Comments, Post, Business

# Register your models here.
admin.site.register(Profile)
admin.site.register(NeighbourHood)
admin.site.register(Comments)
admin.site.register(Post)
admin.site.register(Business)