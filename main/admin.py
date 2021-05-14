from django.contrib import admin


from .models import *

admin.site.register(TypesApartments)
admin.site.register(Cities)
admin.site.register(Typesale)
admin.site.register(Condition)
admin.site.register(Typehouse)
admin.site.register(Typesmaterial)
admin.site.register(Leaseterms)



admin.site.unregister(TypesApartments)
admin.site.unregister(Cities)
admin.site.unregister(Typesale)
admin.site.unregister(Condition)
admin.site.unregister(Typehouse)
admin.site.unregister(Typesmaterial)
admin.site.unregister(Leaseterms)




admin.site.register(Plots)
admin.site.register(Houses)
admin.site.register(Apartments)
admin.site.register(Commerce)

admin.site.register(Reviews)






class ProjectImageAdmin(admin.ModelAdmin):
  pass

class ProjectImageInline(admin.StackedInline):
  model = ProjectImage
  max_num=10
  extra=0

class ProjectAdmin(admin.ModelAdmin):
  inlines = [ProjectImageInline,]

admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(Announcement, ProjectAdmin)
