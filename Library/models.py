from django.db import models
class StudentRegister(models.Model):
	studentfullname=models.CharField(max_length=100,null=False)
	emailid=models.CharField(max_length=30,null=False)
	mobilenumber=models.CharField(max_length=18,null=False)
	usn=models.CharField(max_length=15,null=False)
	department=models.CharField(max_length=100,null=False)

class StaffRegistration(models.Model):
	stafffullname=models.CharField(max_length=100,null=False)
	emailid=models.CharField(max_length=30,null=False)
	mobilenumber=models.CharField(max_length=18,null=False)
	department=models.CharField(max_length=100,null=False)
	stafftype=models.CharField(max_length=100,null=False)

class OperatorDetails(models.Model):
	fullname=models.CharField(max_length=100,null=False)
	emailid=models.CharField(max_length=30,null=False)
	mobilenumber=models.CharField(max_length=18,null=False)
	designation=models.CharField(max_length=30,null=False)
	password=models.CharField(max_length=30,null=False)

class BookDetails(models.Model):
	booktitle=models.CharField(max_length=50,null=False,default="")
	isbn=models.CharField(max_length=25,null=False,default="")
	author=models.CharField(max_length=50,null=False,default="")
	edition=models.CharField(max_length=10,null=False,default="")
	cost=models.CharField(max_length=10,null=False,default="")
	department=models.CharField(max_length=30,null=False,default="")
	quantity=models.CharField(max_length=30,null=False,default="")
	bookrow=models.CharField(max_length=50,null=False,default="")
	bookrack=models.CharField(max_length=50,null=False,default="")
	bookcolumn=models.CharField(max_length=50,null=False,default="")

class Issuebook(models.Model):
	bookstatus=models.CharField(max_length=100,null=False,default="")
	bookisbn=models.CharField(max_length=100,null=False,default="")
	facultyid=models.IntegerField(default=0)
	studentid=models.IntegerField(default=0)
	usn=models.CharField(max_length=100,null=False,default="")
	