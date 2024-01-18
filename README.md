# BBB  

## BACK  
* cd BBB-Back/  
* Création de l’env : env py -m venv env  
* Activer l’environnement virtuel: source env/Scripts/activate  
* Installation des requierements : pip install -r requirements.txt  
* Run: py manage.py runserver  
  

## FRONT  
This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 11.2.6.  
cd BBB-Front/  
npm install  
npm start  
  
## BO  
[back_office](http://localhost:8000/admin/)  
user : bbbadmin  
mdp: adminadmin  

## MODIFICATION POUR MEP  
* Front  
proxy.conf.json target à modifier  
src/app/Components/galery-detail.ts lg 38 route à changer  
src/app/Components/technical-team.component.html lg12 à changer  
  
## DEPLOIEMENT  
* FRONT  
ng build --prod  
