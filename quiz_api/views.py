from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from rest_framework.views import APIView

from .models import Test, Option, TestsUsers
from .serializers import TestSerializer


class AnswerOnTestProcedureAPIView(APIView):
    def post(self, request):
        test_id = request.data['test_id']
        user = request.user
        if TestsUsers.objects.filter(user=user, test__id=test_id).exists():
            return Response({
                'detail': 'You can pass the test only once!'
            }, status=HTTP_403_FORBIDDEN)
        id_of_options_2d = [request.data['answers'][id_q] for id_q in request.data['answers']]
        id_of_options_1d = []
        for item in id_of_options_2d:
            id_of_options_1d.extend(item)

        test = get_object_or_404(Test, pk=test_id)
        test_data = TestSerializer(test).data

        count_right_questions = Option.objects.filter(pk__in=id_of_options_1d, is_right_option=True).count()
        max_mark = test_data['max_right_options']

        user_mark = round((count_right_questions / max_mark) * 10)

        TestsUsers.objects.create(user=user, test=test, result=user_mark)

        return Response({
            'mark': user_mark,
        })

    permission_classes = [IsAuthenticated]
