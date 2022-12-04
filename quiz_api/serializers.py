from rest_framework import serializers

from .models import Topic, Test, Question, Option, TestsUsers


class OptionSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='question.id')

    class Meta:
        model = Option
        fields = [
            'id',
            'content',
            'is_right_option',
            'question_id'
        ]


class QuestionSerializer(serializers.ModelSerializer):
    right_options = serializers.SerializerMethodField()
    wrong_options = serializers.SerializerMethodField()
    test_id = serializers.IntegerField(source='test.id')

    class Meta:
        model = Question
        fields = [
            'id',
            'content',
            'right_options',
            'wrong_options',
            'test_id'
        ]

    def get_right_options(self, obj):
        return OptionSerializer(obj.options.filter(is_right_option=True), many=True).data

    def get_wrong_options(self, obj):
        return OptionSerializer(obj.options.filter(is_right_option=False), many=True).data


class TestsUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestsUsers
        fields = [
            'user_id',
            'result'
        ]


class TestSerializer(serializers.ModelSerializer):
    topic = serializers.CharField(max_length=255, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)
    max_right_options = serializers.SerializerMethodField(read_only=True)
    users = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Test
        fields = [
            'id',
            'topic',
            'questions',
            'max_right_options',
            'users'
        ]

    def get_max_right_options(self, obj):
        max_mark = 0
        data = QuestionSerializer(obj.questions, many=True).data
        for question in data:
            max_mark += len(question['right_options'])
        return max_mark

    def get_users(self, obj):
        return TestsUsersSerializer(obj.tests_users, many=True).data


class TopicSerializer(serializers.ModelSerializer):
    test = TestSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = [
            'id',
            'title',
            'content',
            'test'
        ]
