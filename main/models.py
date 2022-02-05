from django.db import models

class groups(models.Model):
    group_name = models.CharField(max_length=200)
    group_link = models.CharField(max_length=100)
    group_category = models.CharField(max_length=100)

    # kaip db irasas bus uzvadintas. ar "default_group input 1" ar "dovanos" or bla.
    def __str__(self):
        return f"{self.group_category}: {self.group_name}"

    class Meta:
        ordering = ['group_category']
