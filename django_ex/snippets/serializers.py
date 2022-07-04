from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = (
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'created',
            'updated',
        )
        ordering = ('-created_at', "-updated_at")
