# StockMarketApp

## use python manage.py makemigrations and migrate commands for init

## use python manage.py createsuperuser to create admin user
   1. admin user can create new user. 
   2. can create stock in the system.
   To use above feature through UI goto /admin endpoint


## You can register/ login from the below endpoints

1. admin/
2. ^api/user/ ^login/$ [name='rest_login']
3. ^api/user/ ^logout/$ [name='rest_logout']
4. ^api/user/ ^user/$ [name='rest_user_details']
5. ^api/user/register/
6. ^api/account/
7. ^api/user/<int:id>/
  
## Following endpoints available for the logged in user
  1. api/stock/<stock_name> 
     --> To get all the details available for the given stock
  
  2. api/stock/ 
     --> to list all the stock available
