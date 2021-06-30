from django.contrib import admin
from django.contrib.admin.decorators import register
from . models import feed
from . models import subscriber
from . models import signup
from . models import usercreatesurvey
from . models import usereditsurvey
from . models import uquest
from . models import uchp
from . models import adminsignup
from . models import edituser
from . models import addsurvey
from . models import edit_testimonials
from . models import add_testimonials
from . models import achp




# Register your models here.
admin.site.register(feed)
admin.site.register(subscriber)
admin.site.register(signup)
admin.site.register(usercreatesurvey)
admin.site.register(usereditsurvey)
admin.site.register(uquest)
admin.site.register(uchp)
admin.site.register(adminsignup)
admin.site.register(edituser)
admin.site.register(addsurvey)
admin.site.register(edit_testimonials)
admin.site.register(add_testimonials)
admin.site.register(achp)


