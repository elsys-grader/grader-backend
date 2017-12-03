from rest_framework import serializers
from submissions.models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    task = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Submission
        fields = ('task', 'user')
