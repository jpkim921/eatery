# Eatery

A general restaurant website that uses the django framework. This django project to composed to two apps - the restaurant and customer apps. The restaurant app is for the staff to use and the customer to the consumer facing part.
It has all the basic pages such as the landing page, menu, ordering, and about. 


# Screenshots of website
![Screen Shot 2023-01-05 at 5 03 17 PM](https://user-images.githubusercontent.com/24558257/210888753-0845088f-46a9-452e-a245-d3c348885614.png)
![Screen Shot 2023-01-05 at 5 03 28 PM](https://user-images.githubusercontent.com/24558257/210888766-d2403da7-8726-4a24-bb82-f7139456e8fe.png)
![Screen Shot 2023-01-05 at 4 58 53 PM](https://user-images.githubusercontent.com/24558257/210888847-0e66e645-f1ed-408e-906c-db2c412826b2.png)
![Screen Shot 2023-01-05 at 4 58 18 PM](https://user-images.githubusercontent.com/24558257/210888821-261ee955-6a65-4951-9316-ac965a6b8a12.png)


# Setup
Follow the commands below to setup and start the server.

```
python3 -m venv venv
pip install -r requirements.txt
cd eatery
python manage.py makemigration
python manage.py migrate
python manage.py runserver
```



## Photo Credits:
 - Photo by Rachel Claire: https://www.pexels.com/photo/interior-design-of-asian-bar-5531434/
 - Photo by Markus Winkler: https://www.pexels.com/photo/pad-thai-in-white-ceramic-plate-12481161/
 - Photo by Rosali Iraheta: https://www.pexels.com/photo/round-food-with-bacon-166031/
 - Photo by Sebastian Coman Photography : https://www.pexels.com/photo/seared-scallops-3645126/
 - Photo by Thuyen Vu: https://www.pexels.com/photo/food-14816543/
 - Photo by Vidal Balielo Jr.: https://www.pexels.com/photo/brown-bread-on-white-ceramic-plate-14515103/
 - Photo by Pixabay: https://www.pexels.com/photo/chocolate-with-milted-chocolate-on-white-ceramic-plate-45202/
 - Photo by Alexander CueLove: https://www.pexels.com/photo/fruit-terrine-beside-gray-stainless-steel-fork-2273823/
 - Photo by Ainis Jankauskas: https://www.pexels.com/photo/2-whisky-glasses-filled-with-beverage-on-black-tray-169391/
 - Photo by Lisa Fotios: https://www.pexels.com/photo/pink-liquid-on-glass-109275/
 - Photo by Daniel Torobekov: https://www.pexels.com/photo/avocado-toasts-on-wooden-board-13689804/
 - Photo by Foodie Factor: https://www.pexels.com/photo/pastry-and-boiled-egg-on-plate-566566/
 - Photo by Polina Tankilevitch: https://www.pexels.com/photo/close-up-photo-of-variety-of-hummus-6419739/
 - Photo by Sebastian Coman Photography : https://www.pexels.com/photo/food-on-a-plate-3606800/
 - Photo by Nadin Sh: https://www.pexels.com/photo/food-dinner-lunch-chicken-14701402/
 - Photo by Mateusz Feliksik: https://www.pexels.com/photo/food-wood-dinner-lunch-13422431/
 - Photo by Oleksandr Pidvalnyi: https://www.pexels.com/photo/fried-chicken-with-green-leaf-vegetable-on-brown-wooden-round-plate-12960400/
 - Photo by Suzy Hazelwood: https://www.pexels.com/photo/cheesecake-1126359/
 - Photo by Quang Nguyen Vinh: https://www.pexels.com/photo/sliced-cake-on-white-saucer-2144112/
 - Photo by Susanne Jutzeler, suju-foto : https://www.pexels.com/photo/strawberries-1132558/
 - Photo by Abhinav Goswami: https://www.pexels.com/photo/sliced-cake-on-plate-291528/
 - Photo by Quang Nguyen Vinh: https://www.pexels.com/photo/slice-of-cake-on-saucer-2147857/
 - Photo by Alexander Grey: https://www.pexels.com/photo/five-assorted-color-rock-s-glasses-on-gray-surface-1196507/
 - Photo by Dimitris Binioris: https://www.pexels.com/photo/close-up-photo-of-cocktail-with-herb-3039671/
 - Photo by Toni Cuenca: https://www.pexels.com/photo/lemonade-on-brown-surface-616836/
 - Photo by ROMAN ODINTSOV: https://www.pexels.com/photo/mango-juice-in-clear-glass-bottle-4955257/
 - Photo by ROMAN ODINTSOV: https://www.pexels.com/photo/close-up-shot-of-a-glass-of-orange-juice-7494029/
 - Photo by Timur Weber: https://www.pexels.com/photo/clear-drinking-glasses-with-yellow-liquid-8679370/
 - Photo by Pixabay: https://www.pexels.com/photo/food-on-white-ceramic-spoon-39826/
 - Photo by Marion Pintaux: https://www.pexels.com/photo/man-holding-cooking-utensil-2670327/
 - Photo by Anna Tarazevich: https://www.pexels.com/photo/person-holding-chopsticks-and-green-plate-with-food-6937476/


## Todo:
 - [x] Need to create db to help populate the menu
 - [ ] Add drop down to menu navbar link - to show Breakfast, Lunch, Dinner
 - [x] Build out lunch, and dinner menus
 - [x] build out about us apge
 - [x] order page saves order to db
 - [ ] add timer to only load lunch or dinner items on the order page
 - [X] add dashboard for restaurant
 - [ ] add date field for dashboard to filter specific dates
 - [ ] add search field for dashboard
 - [x] add delete buttons for orders in dashboard
 - [-] create order details page
    - [] need to redo address area
 - [ ] need to redo the ordering process
    - [ ] order should be deleted by not paid

 - [ ] create a receipt system using NFTs. try a different chain?
