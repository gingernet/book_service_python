from django.db import models


IS_DEL_CHOICES = [(x, x) for x in ['Yes', 'No']]


class BaseModelManager(models.Manager):
    def all_to_dict(self):
        queryset = self.get_queryset()
        return [obj.to_dict() for obj in queryset.all()]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, self.id)


class BookUser(BaseModel):
    name = models.CharField(max_length=64, default='', verbose_name=u'用户名称')
    phone = models.CharField(max_length=200, default='1', verbose_name=u'电话号码')
    created_time = models.CharField(max_length=200, default='1', verbose_name=u'电话号码')

    class Meta:
        verbose_name = "通信录用户"
        verbose_name_plural = "通信录用户"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "created_at": self.created_at,
        }


