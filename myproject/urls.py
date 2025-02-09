"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('abt/',aboutus),
    path('gallery',gallery),
    path('cnt/',contactus),
    path('preg/',Parents),
    path('creg/',Caretaker),
    path('login/',Logins),
    path('pdash/',pdash),
    path('lgout/',lgout),
    path('cdesn/',children),
    path('pedit/',pedit),
    path('emergency/',emergency),
    path('pviewchild/',pviewchild),
    path('childedit/<int:id>',childedit),
    path('pbookappoint/',pbookappoint),
    path('adash/',adash),
    path('adedit/',adedit),
    path('showmsg/',showmsg),
    path('delmsg/<int:id>',delmsg),
    path('adminviewappoint/',adminviewappoint),
    path('adviewchild/<int:id>',adviewchild),
    path('approveappt/<int:id>',approveappt),
    path('rejectappt/<int:id>',rejectappt),
    path('recruit/',recruitment),
    path('approvecr/<int:id>',approvecr),
    path('rejectcr/<int:id>',rejectcr),
    path('adminvcr/',adminviewcr),
    path('crdelete/<int:id>',crdelete),
    path('credit/<int:id>',credit),
    path('allotcr/',allotcr),
    path('caredes/',caredash),
    path('emrmsg',emrmsg),
    path('delem/<int:id>/',delemr),
    path('crviewchild/',crviewchild),
    path('sendreply/<email>',sendreply),
    path('cedit/',cedit)
    
]

