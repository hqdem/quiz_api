from rest_framework.routers import DefaultRouter

from .viewsets import TopicViewset, TestViewset, QuestionViewset, OptionViewset

router = DefaultRouter()
router.register(r'topics', TopicViewset, basename='topic')
router.register(r'tests', TestViewset, basename='test')
router.register(r'questions', QuestionViewset, basename='question')
router.register(r'options', OptionViewset, basename='option')
urlpatterns = router.urls
