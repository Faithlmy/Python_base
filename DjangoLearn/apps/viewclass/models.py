from django.db import models

# Create your models here.


class TbCustomerPaper(models.Model):
    ecn_no = models.CharField(db_column='ECN_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=255, blank=True, null=True)
    p_name = models.CharField(max_length=255, blank=True, null=True)
    st_site = models.CharField(db_column='ST_site', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alter_cause = models.TextField(blank=True, null=True)
    alter_front = models.TextField(blank=True, null=True)
    create_people = models.CharField(max_length=255, blank=True, null=True)
    current = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_customer_paper'

