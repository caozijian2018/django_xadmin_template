import xadmin
from apps.organizations.models import Teacher, CourseOrg, City

class TeacherAdmin(object):
    pass

class CourseOrgAdmin(object):
    pass

class CityAdmin(object):
    list_display = ['id', 'name', 'desc']
    search_fields = ["name", "desc"]
    list_filter = ['name', 'desc', 'add_time']
    # pass

xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)
