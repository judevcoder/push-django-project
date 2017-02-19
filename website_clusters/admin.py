from django.contrib import admin
from models import WebsiteCluster, Website, WebsiteIcon, WebsiteInvitation


class WebsiteAdmin(admin.ModelAdmin):
	list_display = ('website_url', 'account_key', 'cluster', 'created_at')
admin.site.register(Website, WebsiteAdmin)


admin.site.register(WebsiteCluster)
admin.site.register(WebsiteIcon)
admin.site.register(WebsiteInvitation)