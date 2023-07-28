
from peewee import *

db = SqliteDatabase(":memory:")
db.connect()



class Ingredient(Model):
    name = CharField()
    is_vegetarian = BooleanField()
    is_vegan = BooleanField()
    is_glutenfree = BooleanField()
    
    

    class Meta:
        database = db


class Restaurant(Model):
    name = CharField()
    open_since = DateField()
    opening_time = TimeField()
    closing_time = TimeField()

    class Meta:
        database = db


class Dish(Model):
    name = CharField()
    served_at = ForeignKeyField(model=Restaurant)
    price_in_cents = FloatField()
    ingredients = ManyToManyField(model=Ingredient, backref="dishes")

    class Meta:
        database = db


class Rating(Model):
    restaurant = ForeignKeyField(Restaurant)
    rating = IntegerField()
    comment = CharField(null=True)

    class Meta:
        database = db




DishIngredient = Dish.ingredients.get_through_model()