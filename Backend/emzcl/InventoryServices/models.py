from django.db import models
from UserServices.models import Users
# Create your models here.
class Warehouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True,null=True)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255 )
    pincode = models.CharField(max_length=255)
    warehouse_manager = models.ForeignKey(Users,on_delete=models.CASCADE, blank=True, null=True,related_name='warehouse_manager')
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=[('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE')], default='ACTIVE')
    size = models.CharField(max_length=255,choices=[('SMALL','SMALL'),('MEDIUM','MEDIUM'),('LARGE','LARGE')],default='SMALL')
    capacity = models.CharField(max_length=255,choices=[('LOW','LOW'),('MEDIUM','MEDIUM'),('HIGH','HIGH')],default='LOW')
    warehouse_type = models.CharField(max_length=255,choices=[('OWNED','OWNED'),('LEASED','LEASED')],default='OWNED')
    additional_details = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE,  blank=True, null=True, related_name='domain_user_id')
    added_by_user_id =  models.ForeignKey(Users, on_delete=models.CASCADE,  blank=True, null=True, related_name='added_by_user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)