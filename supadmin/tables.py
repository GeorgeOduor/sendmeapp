import django_tables2 as tables
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django_tables2 import A
from driver.models import Vehicle, CompanyProfile, Profile, Journey


class Company_Table(tables.Table):
    class Meta:
        model = CompanyProfile
        template_name = "django_tables2/bootstrap.html"

        buttons = tables.LinkColumn("company_detail", text=lambda record: record.name, args=[A("pk")])
        fields = ('id', 'company_logo', 'registration_number', 'registration_name', 'buttons')


class SimpleTable(tables.Table):
    edit_link = tables.LinkColumn('bug_edit',
                                  verbose_name='Edit', accessor='pk', attrs={'class': 'edit_link'})
    # delete_link = tables.LinkColumn('bug_delete', args=[A('pk')],
    #                                 verbose_name='Delete Bug', accessor='pk', attrs={'class': 'delete_link'})

    class Meta:
        attrs = {'class': 'paleblue'}
        model = CompanyProfile
