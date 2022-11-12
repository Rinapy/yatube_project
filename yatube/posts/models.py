from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    """Объект поста, содержит поля (text, pub_date, author)"""

    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='posts'
    )

    class Meta:
        ordering = ['-pub_date']


class Group(models.Model):
    """Объект группы, содержит поля (title, slug, description)"""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return f'Посты группы "{self.title}"'
