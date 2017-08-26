#blog/ admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post
from .models import Comment
from .models import Tag



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','tag_list','content_size', 'status','created_at', 'updated_at']
    actions= ['make_draft', 'make_published']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')

    def tag_list(request, post):
        return  ', '.join(tag.name for tag in post.tag_set.all()) #list comprehension

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

    def make_draft(self, request, queryset):
        updated_count =  queryset.update(status='d')
        self.message_user(request, '{} 건의 포스팅을 Draft 상태로 변경'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 Draft 상태로 변경'

    def make_published(self, request, queryset):
        updated_count =  queryset.update(status='p')
        self.message_user(request, '{} 건의 포스팅을 Published 상태로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Published 상태로 변경'

    
#admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class Commentdmin(admin.ModelAdmin):
    list_display= ['id','author', 'post_content_len']
    #방법 1 list_select_related = ['post']  

    def post_content_len(self, comment):
        return '{}글자'.format(comment.post.content)
    #방법 2
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('post')



@admin.register(Tag)
class Tagdmin(admin.ModelAdmin):
    list_play=['name']
