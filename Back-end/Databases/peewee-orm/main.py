import models
from typing import List
from datetime import time, date
import peewee
__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"



models.db.create_tables([ models.Ingredient, models.Dish, models.Rating, models.Restaurant, models.DishIngredient])

'''Ingredients'''


cheese = models.Ingredient.create(name="cheese", is_vegetarian=False, is_vegan=False, is_glutenfree= True )
tomatoes = models.Ingredient.create(name="Tomatoes", is_vegetarian=True, is_vegan=True, is_glutenfree= True )
veggie_mix = models.Ingredient.create(name="Veggie Mix", is_vegetarian=True, is_vegan=True, is_glutenfree= True )
meat = models.Ingredient.create(name="Steak", is_vegetarian=False, is_vegan=False, is_glutenfree= True )
bacon = models.Ingredient.create(name="Bacon", is_vegetarian=False, is_vegan=False, is_glutenfree= True )
pasta = models.Ingredient.create(name="Pasta", is_vegetarian=False, is_vegan=True, is_glutenfree= False )
cream = models.Ingredient.create(name="Cream", is_vegetarian=False, is_vegan=False, is_glutenfree= False )
salt = models.Ingredient.create(name="Salt", is_vegetarian=True, is_vegan=True, is_glutenfree= True )
potatoes = models.Ingredient.create(name="Potatoes", is_vegetarian=True, is_vegan=True, is_glutenfree= True )
curry = models.Ingredient.create(name="Curry", is_vegetarian=True, is_vegan=True, is_glutenfree= True )
bread = models.Ingredient.create(name="Bread", is_vegetarian=False, is_vegan=False, is_glutenfree= False )
eggs = models.Ingredient.create(name="Eggs", is_vegetarian=False, is_vegan=False, is_glutenfree= True )
beans = models.Ingredient.create(name="Beans", is_vegetarian=True, is_vegan=True, is_glutenfree= True )


'''Restaurants'''


big_burger = models.Restaurant.create(name="Big Burger", open_since=date(2019,5,22),opening_time=time(12,30),closing_time=time(23,30))
afonso = models.Restaurant.create(name="Afonsos", open_since=date(2019,5,22),opening_time=time(17,30),closing_time=time(3,30))
domino = models.Restaurant.create(name="Domino", open_since=date(2019,5,22),opening_time=time(11,30),closing_time=time(23,30))
house_of_s = models.Restaurant.create(name="House of Vegan", open_since=date(2019,5,22),opening_time=time(19,30),closing_time=time(23,30))
gaucho = models.Restaurant.create(name="Casa Gaucha", open_since=date(2019,5,22),opening_time=time(11,00),closing_time=time(00,30))
pancake = models.Restaurant.create(name="Pancake House", open_since=date(2009,3,27),opening_time=time(7,30),closing_time=time(17,00))
muki = models.Restaurant.create(name="Muki Muki", open_since=date(2019,5,22),opening_time=time(17,30),closing_time=time(23,30))
luigi = models.Restaurant.create(name="Luigi", open_since=date(1999,5,22),opening_time=time(13,30),closing_time=time(23,30))


'''Dishes'''

pizza = models.Dish.create(name="Pizza", served_at=domino, price_in_cents=13.99)
fries = models.Dish.create(name="Fries", served_at=afonso, price_in_cents=3.99)
burger = models.Dish.create(name="Burger", served_at=big_burger, price_in_cents=14.50)
veggie_soup = models.Dish.create(name="Veggie Soup", served_at=house_of_s, price_in_cents=23.99)
salad = models.Dish.create(name="Salad", served_at=house_of_s, price_in_cents=12.00)
churrasco = models.Dish.create(name="Churrasco", served_at=gaucho, price_in_cents=21.00)
breakfast = models.Dish.create(name="Breakfast", served_at=pancake, price_in_cents=13.99)
carbonara = models.Dish.create(name="Carbonara", served_at=luigi, price_in_cents=17.50)
massala = models.Dish.create(name="Massala", served_at=muki, price_in_cents=38.99)

pizza.ingredients.add([cheese, tomatoes, bacon, salt])
fries.ingredients.add([potatoes, salt])
burger.ingredients.add([bread, meat, bacon, cheese, salt, eggs])
veggie_soup.ingredients.add([veggie_mix, tomatoes, salt])
salad.ingredients.add([salt, tomatoes])
churrasco.ingredients.add([meat, beans, tomatoes, salt])
breakfast.ingredients.add([bacon, eggs,bread, salt])
carbonara.ingredients.add([pasta, bacon, cheese, cream, salt])
massala.ingredients.add([curry, veggie_mix, salt])


b = models.Rating.create(restaurant=big_burger, rating=9)
b = models.Rating.create(restaurant=big_burger, rating=6)
b = models.Rating.create(restaurant=big_burger, rating=6)

a = models.Rating.create(restaurant=afonso, rating=8)
a = models.Rating.create(restaurant=afonso, rating=2)
a = models.Rating.create(restaurant=afonso, rating=4)

d = models.Rating.create(restaurant=domino, rating=8)

v = models.Rating.create(restaurant=house_of_s, rating=1)

g = models.Rating.create(restaurant=gaucho, rating=10)
g = models.Rating.create(restaurant=gaucho, rating=10)
g = models.Rating.create(restaurant=gaucho, rating=7)

p = models.Rating.create(restaurant=pancake, rating=9)

b = models.Rating.create(restaurant=muki, rating=6)

b = models.Rating.create(restaurant=luigi, rating=7)
b1 = models.Rating.create(restaurant=luigi, rating=3)
b2 = models.Rating.create(restaurant=luigi, rating=5)
b3 = models.Rating.create(restaurant=luigi, rating=4)







def cheapest_dish() -> models.Dish:
    dishes_sorted = models.Dish.select().order_by(models.Dish.price_in_cents)
    cheapest = dishes_sorted[0]
    return  cheapest  
 

def vegetarian_dishes() -> List[models.Dish]:
    vege_list =[]
    all_dishes = models.Dish.select()
    for dish in all_dishes:
        all_ingre = []
        for ingr in dish.ingredients:
            all_ingre.append(ingr.is_vegetarian)
            
        if all(all_ingre):
            vege_list.append(dish)

    return list(set(vege_list))
    

def best_average_rating() -> models.Restaurant:
    
    query=models.Rating.select(models.Restaurant.name,
     peewee.fn.AVG(models.Rating.rating)
     .alias('R')).join(models.Restaurant).group_by(models.Restaurant.name).order_by(peewee.fn.AVG(models.Rating.rating).desc())
    
    my_list =[]
    for item in query:
        tpl = (item.restaurant.name,item.R)
        my_list.append(tpl)
    return my_list[0]


    # """You want to know what restaurant is best

    # # Query the database to retrieve the restaurant that has the highest
    # # rating on average
    # # """
    # ...



def add_rating_to_restaurant( ) -> None:
    the_restaurant = models.Restaurant.get()
    rating = models.Rating(restaurant=the_restaurant, rating=2, comment="OK")
    rating.save()
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    


def dinner_date_possible() -> List[models.Restaurant]:
    list_of_dinner_dates = []
    vegan_dish_list =[]
    all_dishes = models.Dish.select().join(models.Restaurant).where(models.Restaurant.opening_time < time(19) and models.Restaurant.closing_time > time(19))
    for dish in all_dishes:
        all_ingre = []
        for ingr in dish.ingredients:
            all_ingre.append(ingr.is_vegan)
            
        if all(all_ingre):
            vegan_dish_list.append(dish)

    for rest in list(set(vegan_dish_list)):
        list_of_dinner_dates.append(rest.served_at)
    return list(set(list_of_dinner_dates))



def add_dish_to_menu() -> models.Dish:
    add_new_dish = models.Dish.create(name="wakawaka", served_at=domino, price_in_cents=13.99)
    all_ingredients = models.Ingredient.select()
    if "Squid" not in [x.name for x in all_ingredients]:
        squid = models.Ingredient.create(name="Squid", is_vegetarian=True, is_vegan=True, is_glutenfree= True)
    add_new_dish.ingredients.add([models.Ingredient.get(name="cheese"), squid])
    return add_new_dish
    

    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
# print(add_dish_to_menu())

models.db.close()