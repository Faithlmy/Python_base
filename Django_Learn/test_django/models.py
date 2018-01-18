from django.db import models

# Create your models here.

class TbCustomInfo(models.Model):
    c_name = models.CharField(max_length=255, blank=True, null=True)
    c_name_short = models.CharField(max_length=255, blank=True, null=True)
    c_num = models.CharField(max_length=255, blank=True, null=True)
    c_type = models.CharField(max_length=255, blank=True, null=True)
    c_site = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    delete_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_custom_info'


class TbCustomerPaper(models.Model):
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
    customer_info = models.ForeignKey('TbCustomInfo', on_delete=models.DO_NOTHING, db_column='customer_info', blank=True, null=True)
    copy_id = models.IntegerField(blank=True, null=True)
    drawingtype = models.IntegerField(blank=True, null=True)
    modify_draft = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    create_people = models.CharField(max_length=255, blank=True, null=True)
    current = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_customer_paper'


class TbDrawingFile(models.Model):
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    uploader = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey('TbCustomerPaper', on_delete=models.DO_NOTHING, blank=True, null=True)
    file_type = models.IntegerField(blank=True, null=True)
    # project = models.ForeignKey('TbProjectPaper', on_delete=models.DO_NOTHING, blank=True, null=True)
    # drawing_type = models.ForeignKey('TbDrawing', on_delete=models.DO_NOTHING, blank=True, null=True)
    cus = models.IntegerField(blank=True, null=True)
    drawing_type_name = models.CharField(max_length=255, blank=True, null=True)
    dev_type = models.CharField(max_length=255, blank=True, null=True)
    # id_dev_type = models.ForeignKey('TbTypeDevice', on_delete=models.DO_NOTHING, db_column='id_dev_type', blank=True, null=True)
    b_all = models.IntegerField(blank=True, null=True)
    sign_filepath = models.CharField(max_length=255, blank=True, null=True)
    seal_filepath = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_drawing_file'
