from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Users(AbstractUser):
    name = models.CharField(max_length=100, blank=True,null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True, choices=(('VN', 'Vietnam'),
    ('US', 'United States'),
    ('UK', 'United Kingdom'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('JP', 'Japan'),
    ('KR', 'South Korea'),
    ('CN', 'China'),
    ('RU', 'Russia'),
    ('BR', 'Brazil'),
    ('VN','Viet Nam')))
    profile_pic= models.ImageField(upload_to='profile_pic./', blank=True, null=True)
    account_status = models.CharField(max_length=50, blank=True, null=True, choices=(('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Blocked', 'Blocked')))
    role = models.CharField(max_length=50, blank=True, null=True, choices=(('Admin', 'Admin'),
        ('User', 'User'),
        ('Supplier', 'Supplier'),
        ('Staff', 'Staff'),
        ('Manager', 'Manager')))
    dob = models.DateField( blank=True, null=True)

    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    social_media_links = models.JSONField( blank=True, null=True)
    addition_details = models.JSONField( blank=True, null=True)
    language = models.CharField(max_length=50,  blank=True, null=True, choices=( ('en', 'English'),
        ('vi', 'Vietnamese'),
        ('Us','English')
        ('fr', 'French'),
        ('es', 'Spanish'),
        ('de', 'German'),
        ('zh', 'Chinese'),
        ('ja', 'Japanese'),
        ('ko', 'Korean')))
    departMent = models.CharField(max_length=50, blank=True, null=True, choices=(('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('FIN', 'Finance'),
        ('MKT', 'Marketing'),
        ('SALES', 'Sales'),
        ('ENG', 'Engineering'),
        ('SUP', 'Support')))
    designation = models.CharField(max_length=50, blank=True, null=True, choices=(('HR', 'Human Resources'),
        ('CEO', 'CEO'),
        ('CSO', 'CSO'),
        ('CTO', 'CTO'),
        ('CMO', 'CMO'),
        ('COD', 'COD'),
        ('CIO', 'CIO'),
        ('CISO', 'CEO'),
        ('CDO', 'CSO'),
        ('CRO', 'CTO'),
        ('CSO', 'CMO'),
        ('CPO', 'COD'),
        ('CIO', 'CIO')
        # ADD
        ))
    timezone = models.CharField(max_length=50, blank=True, null=True,choices=(('UTC-12:00', 'UTC-12:00'),
    ('UTC-11:00', 'UTC-11:00'),
    ('UTC-10:00', 'UTC-10:00'),
    ('UTC-09:30', 'UTC-09:30'),
    ('UTC-09:00', 'UTC-09:00'),
    ('UTC-08:00', 'UTC-08:00'),
    ('UTC-07:00', 'UTC-07:00'),
    ('UTC-06:00', 'UTC-06:00'),
    ('UTC-05:00', 'UTC-05:00'),
    ('UTC-04:30', 'UTC-04:30'),
    ('UTC-04:00', 'UTC-04:00'),
    ('UTC-03:30', 'UTC-03:30'),
    ('UTC-03:00', 'UTC-03:00'),
    ('UTC-02:00', 'UTC-02:00'),
    ('UTC-01:00', 'UTC-01:00'),
    ('UTC+00:00', 'UTC+00:00'), 
    ('UTC+01:00', 'UTC+01:00'),
    ('UTC+02:00', 'UTC+02:00'),
    ('UTC+03:00', 'UTC+03:00'),
    ('UTC+03:30', 'UTC+03:30'),
    ('UTC+04:00', 'UTC+04:00'),
    ('UTC+04:30', 'UTC+04:30'),
    ('UTC+05:00', 'UTC+05:00'),
    ('UTC+05:30', 'UTC+05:30'),
    ('UTC+05:45', 'UTC+05:45'),
    ('UTC+06:00', 'UTC+06:00'),
    ('UTC+06:30', 'UTC+06:30'),
    ('UTC+07:00', 'UTC+07:00'), 
    ('UTC+08:00', 'UTC+08:00'),
    ('UTC+08:45', 'UTC+08:45'),
    ('UTC+09:00', 'UTC+09:00'),
    ('UTC+09:30', 'UTC+09:30'),
    ('UTC+10:00', 'UTC+10:00'),
    ('UTC+10:30', 'UTC+10:30'),
    ('UTC+11:00', 'UTC+11:00'),
    ('UTC+12:00', 'UTC+12:00'),
    ('UTC+12:45', 'UTC+12:45'),
    ('UTC+13:00', 'UTC+13:00'),
    ('UTC+14:00', 'UTC+14:00')))
    last_login = models.DateTimeField( blank=True, null=True)
    last_device = models.GenericIPAddressField(max_length=50, blank=True, null=True)
    last_ip = models.CharField( blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True,choices=( ('USD', 'USD'),  # Đô la Mỹ
    ('EUR', 'EUR'), 
    ('JPY', 'JPY'), 
    ('GBP', 'GBP'),  
    ('AUD', 'AUD'),  
    ('CAD', 'CAD'),  
    ('CHF', 'CHF'),  
    ('CNY', 'CNY'),  
    ('HKD', 'HKD'),  
    ('SGD', 'SGD'),  
    ('KRW', 'KRW'),  
    ('INR', 'INR'), 
    ('VND', 'VND'),  
    ('THB', 'THB'),  
    ('MYR', 'MYR'),  
    ('IDR', 'IDR'),  
    ('PHP', 'PHP'),  
    ('NZD', 'NZD'),  
    ('MXN', 'MXN'),  
    ('BRL', 'BRL'), 
    ('ZAR', 'ZAR'),  
    ('RUB', 'RUB'), 
    ('SAR', 'SAR'),  
    ('AED', 'AED'),  
    ('TRY', 'TRY'),  
    ('SEK', 'SEK'),  
    ('NOK', 'NOK'),  
    ('DKK', 'DKK'),  
    ('PLN', 'PLN'),  
    ('HUF', 'HUF'), 
    ('CZK', 'CZK'),  
    ('ILS', 'ILS'),  
    ('ARS', 'ARS'),
    ('CLP', 'CLP'),  
    ('COP', 'COP'),  
    ('EGP', 'EGP'),  
    ('PKR', 'PKR'),  
    ('BDT', 'BDT'),  
    ('NGN', 'NGN'), 
    ('KES', 'KES')))
    domain_user_id = models.CharField(max_length=50,  blank=True, null=True)
    domain_name = models.CharField(max_length=50,blank=True, null=True)
    plan_type = models.CharField(max_length=50,blank=True, null=True, choices=(('free', 'Free'),
    ('basic', 'Basic'),
    ('standard', 'Standard'),
    ('premium', 'Premium'),
    ('enterprise', 'Enterprise')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserShippingAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    address = models.TextField()
    address_type = models.CharField(max_length=50,choices=(('Home','Home'),('Office','Office'),('Orther','Orther')))
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True, choices=(('VN', 'Vietnam'),
        ('US', 'United States'),
        ('UK', 'United Kingdom'),
        ('FR', 'France'),
        ('DE', 'Germany'),
        ('JP', 'Japan'),
        ('KR', 'South Korea'),
        ('CN', 'China'),
        ('RU', 'Russia'),
        ('BR', 'Brazil'),
        ('VN','Viet Nam')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Modules(models.Model):
    id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=50, unique=True)
    module_icon = models.TextField()
    is_menu = models.BooleanField(default=True)
    is_active= models.BooleanField(default=True)
    module_url = models.TextField()
    parent_id=models.ForeignKey('self',on_delete=models.CASCADE, blank=True,null=True)
    module_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    is_view = models.BooleanField(default=False)
    is_add = models.BooleanField(default=False)
    is_edit = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    domain_user_id = models.CharField(max_length=50,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ActivityLog(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    activity = models.TextField()
    activity_type = models.CharField(max_length=50,  blank=True, null=True)
    activity_date = models.DateTimeField(auto_now_add=True)
    activity_ip = models.GenericIPAddressField()
    activity_device = models.CharField(max_length=50)
    domain_user_id = models.CharField(max_length=50,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class UserBillingAddress(models.Model):
