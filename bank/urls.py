from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('branches', views.BankViewSet)
router.register('branch_details', views.BranchViewSet)

urlpatterns = router.urls