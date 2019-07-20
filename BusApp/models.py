from django.db import models

# Create your models here.


class Department(models.Model):
    number = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    superior = models.ForeignKey("self", on_delete=models.PROTECT, default=1)
    charger = models.CharField(max_length=30, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=500, blank=True)

    @staticmethod
    def init_data():
        Department.objects.all().delete()
        d1 = Department(
            number=1,
            name=u"城市公交总公司")
        d1.superior = d1
        d1.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门'


class Site(models.Model):
    number = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=30)
    valid = models.BooleanField()
    sim = models.CharField(max_length=30)
    entrancen_lon = models.FloatField()
    entrance_lat = models.FloatField()
    entrancen_dir = models.FloatField()
    exit_lon = models.FloatField()
    exit_lat = models.FloatField()
    exit_dir = models.FloatField()
    distance = models.IntegerField()

    lines = models.ManyToManyField(
        'Line', through='Line2Site', related_name='site_lines')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'站点'
        verbose_name_plural = u'站点'


class Line(models.Model):
    number = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    bus_count = models.IntegerField()
    line_length = models.IntegerField()
    earliest_depart_time = models.TimeField()
    earliest_depart_time = models.TimeField()
    latest_arrive_time = models.TimeField()
    latest_arrive_time = models.TimeField()

    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    # starting = models.ForeignKey(Site, on_delete=models.PROTECT)
    # destination = models.ForeignKey(Site, on_delete=models.PROTECT)
    sites = models.ManyToManyField(
        'Site', through='Line2Site', related_name='sites')
    buses = models.ManyToManyField(
        'Bus', through='Bus2Line', related_name='buses')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'线路'
        verbose_name_plural = u'线路'


class Line2Site(models.Model):
    line = models.ForeignKey(Line, on_delete=models.PROTECT)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    site_order = models.IntegerField()

    class Meta:
        ordering = ['site_order', ]

    def __str__(self):
        return self.line.name + "-" + self.site.name

    class Meta:
        verbose_name = u'线路-站点'
        verbose_name_plural = u'线路-站点'


class Bus(models.Model):
    number = models.CharField(max_length=30)
    plate = models.CharField(max_length=255)
    onboard = models.DateTimeField()
    valid = models.BooleanField()

    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    lines = models.ManyToManyField(
        'Line', through='Bus2Line', related_name='bus_lines')

    def __str__(self):
        return self.plate

    class Meta:
        verbose_name = u'公交'
        verbose_name_plural = u'公交'


class Bus2Line(models.Model):
    # 0: all; 1: Mon. - Fri.; 2:Sat; 3:Sun; 4: Weekend; 5: holiday; 6:temporary1; 7:temporary2; 8:temporary3 ......
    schduel_type = models.IntegerField()
    start = models.TimeField()
    end = models.TimeField()
    line = models.ForeignKey(Line, on_delete=models.PROTECT)
    bus = models.ForeignKey(Bus, on_delete=models.PROTECT)

    def __str__(self):
        return self.line.name + '-' + self.bus.plate + ':' + self.start + '-' + self.end

    class Meta:
        verbose_name = u'公交 - 线路'
        verbose_name_plural = u'公交 - 线路'
