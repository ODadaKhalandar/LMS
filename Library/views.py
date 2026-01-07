from django.shortcuts import render
from Library.models import *
def studentregister(request):
	msg=""
	if request.method=="POST":
		s=StudentRegister()
		s.studentfullname=request.POST["studentfullname"]
		s.emailid=request.POST["emailid"]
		s.mobilenumber=request.POST["moblienumber"]
		s.usn=request.POST["usn"]
		s.department=request.POST["department"]
		s.save()
		msg="Register Successfully"
	return render(request,"studentregister.html",{"msg":msg})

def studentregisterdisplay(request):
	msg=""
	if request.method=="POST":
		sid=request.POST["sid"]
		StudentRegister.objects.filter(id=sid).delete()
		msg="Record Deleted Successfully"
	data=StudentRegister.objects.all()
	return render(request,"studentregisterdisplay.html",{"msg":msg,"data":data})

def staffregistration(request):
	msg=""
	if request.method=="POST":
		s=StaffRegistration()
		s.stafffullname=request.POST["stafffullname"]
		s.emailid=request.POST["emailid"]
		s.mobilenumber=request.POST["moblienumber"]
		s.department=request.POST["department"]
		s.stafftype=request.POST["stafftype"]
		s.save()
		msg="Register Successfully"
	return render(request,"staffregistration.html",{"msg":msg})

def staffregistrationdisplay(request):
	msg=""
	if request.method=="POST":
		ssid=request.POST["ssid"]
		StaffRegistration.objects.filter(id=ssid).delete()
		msg="Record Deleted Successfully"
	data=StaffRegistration.objects.all()
	return render(request,"staffregistrationdisplay.html",{"msg":msg,"data":data})

def searchstudent(request):
	data=""
	msg=""
	if request.method=="POST":
		operation=request.POST["btnsubmit"]
		if operation=="X":
			ssid=request.POST["ssid"]
			StudentRegister.objects.filter(id=ssid).delete()
			msg="Record Deleted"
		elif operation=="Issue Book":
			if request.method=="POST":
				ib=Issuebook()
				ib.bookisbn=request.POST["isbnnumber"]
				ib.bookstatus='ISSUED'
				ib.studentid=request.POST["sid"]
				ib.usn=request.POST['txtusn']
				ib.save()
				msg="Book Issued"
			return render(request,"searchstudent.html",{"msg":msg})
		
		
		else:
			searchby=int(request.POST["searchby"])
			value=request.POST["value"]
			if searchby==1:
				data=StudentRegister.objects.filter(studentfullname__contains=value)
			elif searchby==2:
				data=StudentRegister.objects.filter(mobilenumber=value)
			elif searchby==3:
				data=StudentRegister.objects.filter(usn=value)
			if data.exists():
				pass
			else:
				msg="Record not found"
	return render(request,"searchstudent.html",{"data":data,"msg":msg})

def searchstaff(request):
	data=""
	msg=""
	if request.method=="POST":
		operation=request.POST["btnsubmit"]
		if operation=="X":
			mid=request.POST["msid"]
			StudentRegister.objects.filter(id=mid).delete()
			msg="Record Deleted"
		else:
			searchby=int(request.POST["searchby"])
			value=request.POST["value"]
			if searchby==1:
				data=StudentRegister.objects.filter(studentfullname__contains=value)
			elif searchby==2:
				data=StudentRegister.objects.filter(mobilenumber=value)
			if data.exists():
				pass
			else:
				msg="Record not found"
	return render(request,"searchstudent.html",{"data":data,"msg":msg})


#operator 


def operatorregister(request):
	msg=""
	if request.method=="POST":
		od=OperatorDetails()
		od.fullname=request.POST["fullname"]
		od.emailid=request.POST["emailid"]
		od.mobilenumber=request.POST["mobilenumber"]
		od.designation=request.POST["designation"]
		od.password=request.POST["password"]
		od.save()
		msg="Registration Successfully"
		
	return render(request,"operatorregister.html",{"msg":msg})

def OperatorData(request):
	msg=""
	if request.method=="POST":
		oid=request.POST["oid"]
		OperatorDetails.objects.filter(id=oid).delete()
		msg="Record Deleted Successfully"
	data=OperatorDetails.objects.all()
	return render(request,"OperatorData.html",{"msg":msg,"data":data})

def bookmaster(request):
	msg=""
	if request.method=="POST":
		bm=BookDetails()
		bm.booktitle=request.POST["booktitle"]
		bm.isbn=request.POST["isbn"]
		bm.author=request.POST["author"]
		bm.edition=request.POST["edition"]
		bm.department=request.POST["department"]
		bm.cost=request.POST["cost"]
		bm.quantity=request.POST["quantity"]
		bm.bookrow=request.POST["bookrow"]
		bm.bookrack=request.POST["bookrack"]
		bm.bookcolumn=request.POST["bookcolumn"]
		
		bm.save()
		msg="Registration Successfully"
		
	return render(request,"bookmaster.html",{"msg":msg})
	
def BookData(request):
	msg=""
	if request.method=="POST":
		bid=request.POST["bid"]
		BookDetails.objects.filter(id=bid).delete()
		msg="Record Deleted Successfully"
	data=BookDetails.objects.all()
	return render(request,"bookdata.html",{"msg":msg,"data":data})

def operatorsearch(request):
	data=""
	msg=""
	if request.method=="POST":
		operation=request.POST["btnsubmit"]
		if operation=="X":
			tsid=request.POST["tsid"]
			OperatorDetails.objects.filter(id=tsid).delete()
			msg="Record Deleted"
		else:
			search=int(request.POST["searchby"])
			value=request.POST["value"]
			if search==1:
				data=OperatorDetails.objects.filter(fullname__contains=value)
			elif search==2:
				data=OperatorDetails.objects.filter(emailid__contains=value)
			elif search==3:
				data=OperatorDetails.objects.filter(mobilenumber=value)
			elif search==4:
				data=OperatorDetails.objects.filter(designation=value)
			if data.exists():
				pass
			else:
				msg="Record not found"
	return render(request,"operatorsearch.html",{"data":data,"msg":msg})
				

def issuebook(request):
	msg=""
	if request.method=="POST":
		ib=Issuebook()
		ib.studentfullname=request.POST["studentfullname"]
		ib.mobilenumber=request.POST["mobilenumber"]
		ib.isbn=request.POST["isbn"]
		ib.bookstatus=request.POST["bookstatus"]
		ib.bookisbn=request.POST["bookisbn"]
		ib.save()
		msg="BOOK ISSUED"
	return render(request,"issuebook.html",{"msg":msg,})	
