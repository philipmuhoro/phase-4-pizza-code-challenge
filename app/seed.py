from random import choice, choices, randint
import faker

from models import Restaurant,Restaurant_pizza,Pizza, db

fake = faker.Faker()

from app  import app

with app.app_context():
    
    Pizza.query.delete()
    Restaurant_pizza.query.delete()
    Restaurant.query.delete()

    for n in range(30):
        fake_name=  fake.name()
        address= fake.address()

        
        restaurant1 = Restaurant(name=fake_name ,address=address)
        db.session.add(restaurant1)
        db.session.commit()

    
    pizzas= ["Cheese Pizza", "Supreme Pizza", "Meat Pizza" , "Margherita Pizza", "BBQ Chicken Pizza", "Veggie Pizza", "Pepperoni Pizza"]
    sample_ingredients= ["pepperoni" , "mushroom" ,"mozzarella", "onion", "bacon", "oregano", "olives",  "anchovies",  "ham"]
    

    random_pizzas= []

    for n in range(len(pizzas)):
        other_pizza = choices(sample_ingredients , k=3)
        random_ingedients= ','.join(str(ingredient) for ingredient in other_pizza)
        random_pizza= Pizza(name= choice(pizzas), ingredients= random_ingedients)
        random_pizzas.append(random_pizza)

    print(random_pizzas)
    db.session.add_all(random_pizzas)
    db.session.commit()

    for record in range(15):
        rnd_rest=choice([x.id for x in Restaurant.query.all()])
        rnd_pizza= choice([p.id for p in  Pizza.query.all()])
        db.session.add(Restaurant_pizza(restaurant_id=rnd_rest, pizza_id=rnd_pizza, price= randint(1,30)))
        db.session.commit()

    