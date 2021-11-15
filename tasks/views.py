from django.shortcuts import render
from django.http import HttpResponse
from marshmallow import Schema,fields,post_load, ValidationError
from django.contrib.auth.models import User,auth
# Create your views here.

def item(request):
    return render(request,"home.html")
def additem(request):
    if request.method == 'POST':
        val = request.POST["item"]
        user = User.objects.create_user(item = val,status = 'pending')
        user.save()
        print("valid data")
    else:    
        return render(request,"valid.html")  

 #'''
#class Item:
#    def __init__(self,item):
#        self.item = item
#class ItemSchema(Schema):
#    item = fields.String()
 #   def create_item(self, item, **kwargs):
  #      return Item(**item)
#input_data = {}
#value = additem()
#input_data['itemval'] = value

#try:
 #schema = ItemSchema()
 #item = schema.load(input_data)
#except ValidationError as err:
 #   print(err)
  #  print(err.valid_data)'''