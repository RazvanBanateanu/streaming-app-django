from django.contrib import admin

from .models import TVShowProxy, TVShowSeasonProxy, Playlist, PlaylistItem

# Register your models here.

class SeasonEpisodeInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0

class TVShowSeasonProxyAdmin(admin.ModelAdmin):
    inlines = [SeasonEpisodeInline]
    fields = ['title', 'parent']
    class Meta:
        model = TVShowSeasonProxy
    
    def get_queryset(self, request):
        return TVShowProxy.objects.all()

admin.site.register(TVShowSeasonProxy, TVShowSeasonProxyAdmin)


class TVShowSeasonProxyInline(admin.TabularInline):
    model = TVShowSeasonProxy
    extra = 0
    fields = ['order', 'title', 'state']

class TVShowProxyAdmin(admin.ModelAdmin):
    inlines = [TVShowSeasonProxyInline]
    fields = ['title', 'decription', 'state', 'video', 'slug']
    class Meta:
        model = TVShowProxy

    def get_queryset(self, request):
        return TVShowProxy.objects.all()

admin.site.register(TVShowProxy, TVShowProxyAdmin)


class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0

class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistItemInline]
    class Meta:
        model = Playlist

admin.site.register(Playlist, PlaylistAdmin)
