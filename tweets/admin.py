from django.contrib import admin
from .models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'created_at')  # now valid
    fields = ('content', 'image', 'user')

    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        initial['user'] = request.user.pk  # preselect current admin
        return initial

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)
