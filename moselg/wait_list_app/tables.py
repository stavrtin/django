import django_tables2 as tables
from .models import ReportBeds


class BedsTable(tables.Table):
    med_org = tables.Column(verbose_name='Med_org',
                          order_by=('med_org', '-med_org'))
    # m_employ = tables.Column(verbose_name='m_employ',
    #                        order_by=('m_employ', '-m_employ'))
    # f_employ = tables.Column(verbose_name='f_employ',
    #                                  order_by=('f_employ',
    #                                            '-f_employ'))
    # m_free = tables.Column(verbose_name='m_free',
    #                           order_by=('m_free', '-m_free'))
    # f_free = tables.Column(verbose_name='f_free',
    #                             order_by=('f_free', '-f_free'))
    # create_at = tables.Column(verbose_name='create_at',
    #                             order_by=('create_at', '-create_at'))

    class Meta:
        model = ReportBeds
        # template_name = 'search_man/beds_info.html'