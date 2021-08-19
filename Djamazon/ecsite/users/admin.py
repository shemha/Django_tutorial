# venv/lib/python3.8/site-packages/django/contrib/adminディレクトリ
from django.contrib import admin
# venv/lib/python3.8/site-packages/django/contrib/auth/admin.pyの'UserAdmin'クラス
from django.contrib.auth.admin import UserAdmin
# venv/lib/python3.8/site-packages/django/contrib/auth/forms.pyの'UserChangeForm'クラス, 'UserCreationForm'クラス
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# venv/lib/python3.8/site-packages/django/utils/tanslation/__init__.pyの'ugettext_lazy'クラス
from django.utils.translation import ugettext_lazy as _
# users/models.pyのUserクラス
from .models import User

# Register your models here.
class MyUserChangeForm(UserChangeForm):
    """User情報を変更するフォーム"""
    class Meta:
        model = User
        fields = '__all__' # 全ての情報を変更可能


class MyUserCreationForm(UserCreationForm):
    """Userを作成するフォーム"""
    class Meta:
        model = User
        fields = ('email',) # emailとパスワードが必要


class MyUserAdmin(UserAdmin):
    """カスタムユーザーモデルのAdmin"""
    fieldsets = (
        (None, {'fields': ('email', 'password', 'fav_products')}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, MyUserAdmin)