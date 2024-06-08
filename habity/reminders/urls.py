from rest_framework.routers import SimpleRouter

from habity.reminders.views import ReminderViewSet

router = SimpleRouter()
router.register("reminders", ReminderViewSet)
urlpatterns = router.urls
