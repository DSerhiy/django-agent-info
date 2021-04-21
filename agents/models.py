from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)

    def get_country_json(self):
        data = {
            "id": self.pk,
            "name": self.name,
        }
        return data

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']


class TimeZone(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Time Zone'
        verbose_name_plural = 'Time Zones'
        ordering = ['name']


class Port(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(to=Country, on_delete=models.PROTECT)
    time_zone = models.ForeignKey(to=TimeZone, on_delete=models.PROTECT)

    def get_port_json(self):
        data = {
            "id": self.pk,
            "name": self.name,
        }
        return data

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Port'
        verbose_name_plural = 'Ports'
        ordering = ['name']


class Agent(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    appointments = models.PositiveSmallIntegerField(null=True, blank=True)
    loading_activity = models.PositiveSmallIntegerField(null=True, blank=True)
    discharging_activity = models.PositiveSmallIntegerField(null=True, blank=True)
    country_of_registry = models.ForeignKey(to=Country, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'
        ordering = ['name']


class AgentCargo(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveSmallIntegerField()
    agent = models.ForeignKey(to=Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AgentCargo'
        verbose_name_plural = 'AgentCargos'
        ordering = ['agent__name']


class AgentVesselType(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveSmallIntegerField()
    agent = models.ForeignKey(to=Agent, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'AgentVesselType'
        verbose_name_plural = 'AgentVesselType'
        ordering = ['agent__name']

    def __str__(self):
        return self.name


class ContactDetails(models.Model):
    agent = models.ForeignKey(to=Agent, on_delete=models.CASCADE)
    port = models.ForeignKey(to=Port, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    main_email = models.EmailField(max_length=254, blank=True, null=True)
    website = models.CharField(max_length=254, blank=True, null=True)

    def get_agent_json(self):
        data = {
            "id": self.pk,
            "name": self.agent.name,
            "email": self.main_email,
            "phone": self.phone,
            "website": self.website,
            "appointments": self.agent.appointments,
        }
        return data

    def __str__(self):
        return f'{self.agent} @ {self.port}'

    class Meta:
        verbose_name = 'Contact Detail'
        verbose_name_plural = 'Contact Details'
        ordering = ['port']


class Email(models.Model):
    email = models.EmailField(max_length=254)
    contact_details = models.ForeignKey(to=ContactDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
