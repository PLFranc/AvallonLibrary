#Documentation API Bibliothèque d'Avallon

##I. le Set-up
* Afin d'utiliser ce programme merci de lancer l'environnement virtuel venv
* La BDD étant hébergé chez AWS RDS merci de me contacter en me précisant votre adresse IP pour que je vous y donnes accès.  
email: pierre-louis.franc@epfedu.fr
##II. Les URLs
###S'inscrire:
POST:  
/add_user  
input : {  
    "email":  
    "password":   
    "name":   
    "phone":  
}
###Rechercher un livre
GET:  
* par son titre: /get_book_by_title  
    input : {  
    "title":  
  }      
* par son auteur: /get_book_by_author  
 input : {  
    "author":  
  }
###Résrver un livre
PUT:  
/make_reservation  
input:  
{  
    "user_id":   
    "book_id":   
} 
###Remettre un livre
PUT:  
/brought_book
input:  
{  
    "book_id":  
} 
###Voir les livres disponibles
GET:  
/get_available_book
###Voir l'emplacement d'un livre
GET:  
/get_book_area  
input  :  
{  
    "book_id":  
}  
###Ajouter un livre
POST:  
/add_book  
input:{  
"title":  
"author"  
}  
###suivre les réservations
GET:  
/reservations
###Remettre un livre a sa place dans la bibliothèque
PUT:  
/store_book  
input:  
{  
    "area":    
    "rack":  
    "book_id":  
}  
