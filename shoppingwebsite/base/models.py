from django.db import models
import uuid  # Required for uuid.uuid4

# Section1 What is a Django Model? readme.md

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

# section-1a
# now when i call this module it will automaticalyy update the  uid and date and time 