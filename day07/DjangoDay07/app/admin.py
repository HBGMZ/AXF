from django.contrib import admin
from app.models import Goods, Grade, Student


# 注册
class GoodsAdmin(admin.ModelAdmin):
    # 显示的字段
    list_display = ['pk', 'name', 'icon', 'price']

    # 分页
    list_per_page = 10

    # 过滤字段
    list_filter = ['name']

    # 搜索字段
    search_fields = ['name', 'pk']

    # 执行动作位置
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(Goods, GoodsAdmin)


class StudentInfo(admin.TabularInline):
    model = Student
    extra = 1

class GradeAdmin(admin.ModelAdmin):
    list_display =  ['pk', 'g_name']
    inlines = [StudentInfo]

class StudentAdmin(admin.ModelAdmin):
    list_filter = ['s_grade']
    list_display =  ['pk', 's_name', 's_score']


admin.site.register(Grade, GradeAdmin)
admin.site.register(Student, StudentAdmin)
