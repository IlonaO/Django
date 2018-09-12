from restless.dj import DjangoResource

from apps.blog.models import Post


class PostsResource(DjangoResource):
    def list(self):
        return [post.to_dict() for post in Post.objects.all()]

    def detail(self, pk):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return {'error': 'Post o podanym id nie istnieje'}
        return post.get_details()
