from django.db import models

# Create your models here.
class Quote(models.Model):
    text=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Category(models.Model):
    title=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class RequestLog(models.Model):
    user_id=models.IntegerField()
    request_method=models.CharField(max_length=100)
    request_path=models.CharField(max_length=100)
    response_status=models.IntegerField()
    request_body=models.JSONField()
    remote_address=models.CharField(max_length=100)
    server_hostname=models.CharField(max_length=100)
    run_time=models.DecimalField(max_digits=5,decimal_places = 2)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request_method

class Faq(models.Model):
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    attachment=models.CharField(max_length=100)

    def __str__(self):
        return self.question

