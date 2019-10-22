# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime
from django.db import models
from django.utils import timezone
from datetime import date
#from django.contrib.auth.models import Categories

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    sector = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.name

class Briefs(models.Model):
    brief_id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    #locationx = models.IntegerField(blank=True, null=True)
    locationx = models.ForeignKey('Locations', models.DO_NOTHING, db_column='locationx', blank=True, null=True)
    recommend = models.CharField(max_length=150, blank=True, null=True)
    #sector = models.IntegerField(blank=True, null=True)
    sector = models.ForeignKey('Sectors', models.DO_NOTHING, db_column='sector', blank=True, null=True)
    developer = models.ForeignKey('Developers', models.DO_NOTHING, db_column='developer', blank=True, null=True)
    #developer = models.IntegerField(blank=True, null=True)
    received = models.DateField(blank=True, null=True) #default=now()?  default=datetime.now()
    exempted = models.DateField(blank=True, null=True)
    tor = models.DateField(blank=True, null=True)
    approved = models.DateField(blank=True, null=True)
    #category_id = models.IntegerField(blank=True, null=True)
    sector2 = models.IntegerField(blank=True, null=True)
    #sector2 = models.ForeignKey('Sectors', models.DO_NOTHING, db_column='sector2', blank=True, null=True)
    #category = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey('Categories', models.DO_NOTHING, db_column='category', blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'briefs'

    def __str__(self):
        return self.title #or brief_id

class Assignment(models.Model):
    ass_id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today, blank=True, null=False)
    project = models.ForeignKey('Briefs', models.DO_NOTHING, db_column='project', blank=False, null=False)
    officer = models.ForeignKey('Officers', models.DO_NOTHING, db_column='officer', blank=False, null=False)
    stage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignment'

class Officers(models.Model):
    sname = models.CharField(max_length=50, blank=False, null=False)  # This field type is a guess.
    officer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'officers'

    def __str__(self):
        return self.sname

class Developers(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'developers'

    def __str__(self):
        return self.name

class Consultants(models.Model):
    consultant_id = models.AutoField(primary_key=True)
    consultant_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'consultants'
        
class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'

    def __str__(self):
        if self.name == "None":
           return ""
        elif self.name is None:
           return ""
        else:
           return "at " + self.name

class Sectors(models.Model):
    sector_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sectors'

    def __str__(self):
        return self.name

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



