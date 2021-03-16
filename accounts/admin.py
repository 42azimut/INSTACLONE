from django.contrib import admin
from .models import Profile, Follow

# Register your models here.


class FollowInline(admin.TabularInline): #팔로우 내용을 표 양식으로 보는 옵션
    model = Follow
    fk_name = 'from_user'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'user']
    list_display_links =['nickname', 'user']
    search_fields = ['nickname']
    inlines = [FollowInline,]

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'created_at']
    list_display_links = ['from_user', 'to_user', 'created_at']
