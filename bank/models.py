from django.db import models

class Bank(models.Model):
    bank_id = models.IntegerField(primary_key=True, blank=True)
    name = models.CharField("Bank Name", max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class BranchDetails(models.Model):
    bank = models.ForeignKey("Bank", related_name="bank_details", on_delete=models.CASCADE, blank=True)
    branch = models.CharField(max_length=255, blank=True)
    ifsc = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '( ' + self.ifsc + ': ' + self.branch + ')'
