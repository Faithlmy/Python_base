from django.db import models

# Create your models here.


class TbCustomerPaper(models.Model):
    # mm = models.Manager
    ecn_no = models.CharField(db_column='ECN_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=255, blank=True, null=True)
    p_name = models.CharField(max_length=255, blank=True, null=True)
    st_site = models.CharField(db_column='ST_site', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drawing_type = models.CharField(max_length=255, blank=True, null=True)
    definer_name = models.CharField(max_length=255, blank=True, null=True)
    c_name = models.CharField(max_length=255, blank=True, null=True)
    c_type = models.CharField(max_length=255, blank=True, null=True)
    c_site = models.CharField(max_length=255, blank=True, null=True)
    uploader = models.CharField(max_length=255, blank=True, null=True)
    custters_spec = models.CharField(max_length=255, blank=True, null=True)
    case_name = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    alter_cause = models.TextField(blank=True, null=True)
    alter_front = models.TextField(blank=True, null=True)
    alter_later = models.TextField(blank=True, null=True)
    desc_file = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True)
    c_confirm = models.IntegerField(blank=True, null=True)
    copy_id = models.IntegerField(blank=True, null=True)
    drawingtype = models.IntegerField(blank=True, null=True)
    modify_draft = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    create_people = models.CharField(max_length=255, blank=True, null=True)
    current = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
