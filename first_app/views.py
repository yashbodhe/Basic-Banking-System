from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from first_app.models import User

def index(request):
	user_list=User.objects.all()
	params={'cos_list':user_list}
	return render(request,"index.html",params)


def View_all_Customers(request):
	user_list=User.objects.all()
	params={'cos_list':user_list}
	return render(request, 'View_all_Customers.html', params)

def Transfer_Money(request):
	user_list=User.objects.all()
	params={'cos_list':user_list}
	return render(request,"Transfer_Money.html",params)

def Transaction_Result(request):
	res=True
	user_list=User.objects.all()
	sender=request.POST['senderName']
	receiver=request.POST['receiverName']
	amount=float(request.POST['amount'])
	
	if sender!=receiver:
		senderObj,receiverObj=None,None
		for user in user_list:
			if user.ename==sender:
				senderObj=user
			elif user.ename==receiver:
				receiverObj=user
		if amount<=float(senderObj.ebal):
			tmp=float(senderObj.ebal)-amount
			senderObj.ebal=str(tmp)
			tmp=float(receiverObj.ebal)+amount
			receiverObj.ebal=str(tmp)
			senderObj.save()
			receiverObj.save()
		else:
			res=False
	else:
		res=False
	
	params={'result':res,'cos_list':user_list}
	return render(request,"transaction_res.html",params)
