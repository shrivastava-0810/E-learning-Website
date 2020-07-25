from django.contrib import admin
from django.urls import path, include
from course import views as course_views
from aboutus import views as aboutus_views
from becomeinstructor import views as becomeinstructor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', course_views.home, name='home'),
    path('home.html', course_views.home, name='home'),
    path('courses.html', course_views.courses, name='courses'),
    path('about.html', aboutus_views.about, name='about'),
    path('contact.html', aboutus_views.contact, name='contact'),
    path('accounts/', include('accounts.urls')),
    path('becomeinstructor.html', becomeinstructor_views.becomeinstructor, name='becomeinstructor'),

]
