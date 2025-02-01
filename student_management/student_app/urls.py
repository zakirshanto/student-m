from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # মূল পৃষ্ঠা
    path('add/', views.student_create, name='student_create'),  # নতুন ছাত্র যোগ করার পৃষ্ঠা
    path('<int:pk>/', views.student_detail, name='student_detail'),  # ছাত্রের বিস্তারিত তথ্য দেখানোর পৃষ্ঠা
    path('<int:pk>/edit/', views.student_update, name='student_update'),  # ছাত্রের তথ্য আপডেট করার পৃষ্ঠা
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),  # ছাত্র মুছে ফেলার পৃষ্ঠা
]
