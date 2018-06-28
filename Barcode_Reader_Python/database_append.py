import json

data_format_prod = {
	'Prod_Name': "None", 'BBD': "None", 'Nutrients': [], 'Calories': 0, 'Cooked': False, 'Allergens': [], 'Problematic': False, 'Process': "None", 'ED': "None"
}

data_format_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}

data_1_prod = {
	'Prod_Name': "Delitos", 'BBD': "19.12.2018", 'Nutrients': ['Protein(1.52g)', 'Carbohydrate(14.6g)', 'Fibre(1.1g)', 'Soduium(0.18g)', 'Fat(10.2g)', 'Salt(2.3g)'],
	'Calories': 160, 'Cooked': True, 'Allergens': ['Lactose','Gluten', 'Nuts'], 'Problematic': False,
	'Process': 'Fried', 'ED': "02.09.2018"
}
data_2_prod = {
	'Prod_Name': "Delitos", 'BBD': "18.02.2018", 'Nutrients': ['Protein(1.52g)', 'Carbohydrate(14.6g)', 'Fibre(1.1g)', 'Soduium(0.18g)', 'Fat(10.2g)', 'Salt(2.3g)'], 'Calories': 153, 'Cooked': True, 'Allergens': ['Lactose','Gluten', 'Nuts'], 'Problematic': True, 'Process': 'Fried', 'ED': "12.03.2018"
}
data_3_prod = {
	'Prod_Name': "Delitos", 'BBD': "10.01.2019", 'Nutrients': ['Protein(1.52g)', 'Carbohydrate(14.6g)', 'Fibre(1.1g)', 'Soduium(0.18g)', 'Fat(10.2g)', 'Salt(2.3g)'], 'Calories': 155, 'Cooked': True, 'Allergens': ['Lactose','Gluten', 'Nuts'], 'Problematic': False, 'Process':'Fried' , 'ED': "20.02.2019"
}
data_4_prod = {
	'Prod_Name': "Delitos", 'BBD': "12.12.2018", 'Nutrients': ['Protein(1.52g)', 'Carbohydrate(14.6g)', 'Fibre(1.1g)', 'Soduium(0.18g)', 'Fat(10.2g)', 'Salt(2.3g)'], 'Calories': 161, 'Cooked': True, 'Allergens': ['Lactose','Gluten', 'Nuts'], 'Problematic': False, 'Process': 'Fried', 'ED': "12.02.2019"
}
data_5_prod = {
	'Prod_Name': "Delitos", 'BBD': "12.05.2018", 'Nutrients': ['Protein(1.52g)', 'Carbohydrate(14.6g)', 'Fibre(1.1g)', 'Soduium(0.18g)', 'Fat(10.2g)', 'Salt(2.3g)'], 'Calories': 167, 'Cooked': True, 'Allergens': ['Lactose','Gluten', 'Nuts'], 'Problematic': True, 'Process':'Fried', 'ED': "12.06.2018"
}

data_6_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': "02.11.2018", 'Nutrients': ['Protein(6g)', 'Carbohydrate(6.8g)', 'Fibre(4g)', 'Sodium(2g)', 'Fat(18g)', 'Sugar(0.5)', 'Salt(0.40g)'],
	'Calories': 439, 'Cooked': True, 'Allergens': ['Lactose', 'Wheat', 'Soya'], 'Problematic': False,
	'Process': 'Baked', 'ED': "08.12.2018"
}
data_7_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': "20.07.2018", 'Nutrients': ['Protein(6g)', 'Carbohydrate(6.8g)', 'Fibre(4g)', 'Sodium(2g)', 'Fat(18g)', 'Sugar(0.5)', 'Salt(0.40g)'], 'Calories': 430, 'Cooked': True, 'Allergens': ['Lactose', 'Wheat', 'Soya'], 'Problematic': False, 'Process': 'Baked', 'ED': "20.09.2018"
}
data_8_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': "31.07.2018", 'Nutrients': ['Protein(6g)', 'Carbohydrate(6.8g)', 'Fibre(4g)', 'Sodium(2g)', 'Fat(18g)', 'Sugar(0.5)', 'Salt(0.40g)'], 'Calories': 441, 'Cooked': True, 'Allergens': ['Lactose', 'Wheat', 'Soya'], 'Problematic': False, 'Process': 'Baked', 'ED': "25.10.2018"
}
data_9_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': "11.06.2018", 'Nutrients': ['Protein(6g)', 'Carbohydrate(6.8g)', 'Fibre(4g)', 'Sodium(2g)', 'Fat(18g)', 'Sugar(0.5)', 'Salt(0.40g)'], 'Calories': 444, 'Cooked': True, 'Allergens': ['Lactose', 'Wheat', 'Soya'], 'Problematic': True, 'Process': 'Baked', 'ED': "12.07.2018"
}
data_10_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': "20.12.2018", 'Nutrients': ['Protein(6g)', 'Carbohydrate(6.8g)', 'Fibre(4g)', 'Sodium(2g)', 'Fat(18g)', 'Sugar(0.5)', 'Salt(0.40g)'], 'Calories': 429, 'Cooked': True, 'Allergens': ['Lactose', 'Wheat', 'Soya'], 'Problematic': False, 'Process': 'Baked', 'ED': "25.02.2019"
}
data_11_prod = {
	'Prod_Name': "Gluten Free Penne Rigate", 'BBD': "18.02.2019", 'Nutrients': ['Protein(6.5g)', 'Carbohydrate(78.7g)', 'Fiber(1.1g)', 'Fat(1.8g)', 'Salt(0.003g)'], 'Calories': 359,'Cooked': False, 'Allergens': ['Wheat'],
	'Problematic': False, 'Process': 'Klining', 'ED': '18.02.2020'
}
data_12_prod = {
	'Prod_Name': "Gluten Free Penne Rigate" , 'BBD': "15.05.2019", 'Nutrients': ['Protein(6.5g)', 'Carbohydrate(78.7g)', 'Fiber(1.1g)', 'Fat(1.8g)', 'Salt(0.003g)'], 'Calories': 351, 'Cooked': False, 'Allergens': ['Wheat'], 'Problematic': False, 'Process': 'Klining', 'ED': "19.11.2019"
}
data_13_prod = {
	'Prod_Name':  "Gluten Free Penne Rigate", 'BBD': "21.01.2019", 'Nutrients': ['Protein(6.5g)', 'Carbohydrate(78.7g)', 'Fiber(1.1g)', 'Fat(1.8g)', 'Salt(0.003g)'], 'Calories': 362, 'Cooked': False, 'Allergens': ['Wheat'], 'Problematic': False, 'Process': 'Klining', 'ED': "26.08.2019"
}
data_14_prod = {
	'Prod_Name':  "Gluten Free Penne Rigate", 'BBD': "22.11.2018", 'Nutrients': ['Protein(6.5g)', 'Carbohydrate(78.7g)', 'Fiber(1.1g)', 'Fat(1.8g)', 'Salt(0.003g)'], 'Calories': 350, 'Cooked': False, 'Allergens': ['Wheat'], 'Problematic': False, 'Process': 'Klining', 'ED': "22.11.2019"
}
data_15_prod = {
	'Prod_Name':  "Gluten Free Penne Rigate", 'BBD': "30.01.2019", 'Nutrients': ['Protein(6.5g)', 'Carbohydrate(78.7g)', 'Fiber(1.1g)', 'Fat(1.8g)', 'Salt(0.003g)'], 'Calories': 359, 'Cooked': False, 'Allergens': ['Wheat'], 'Problematic': False, 'Process': 'Klining', 'ED': "20.01.2020"
}

data_16_prod = {
	'Prod_Name': "EGE Gluten Free Corn Starch", 'BBD': '27.03.2019', 'Nutrients': ['Fat(0.3g)', 'Carbohydrate(87.9g)', 'Protein(0.3g)'], 'Calories': 360,'Cooked': False, 'Allergens': ['Corn'],
	'Problematic': False, 'Process': 'Scalping', 'ED': '20.02.2020'
}
data_17_prod = {
	'Prod_Name': "EGE Gluten Free Corn Starch", 'BBD': "20.01.2019", 'Nutrients': ['Fat(0.3g)', 'Carbohydrate(87.9g)', 'Protein(0.3g)'], 'Calories': 361, 'Cooked': False, 'Allergens': ['Corn'], 'Problematic': False, 'Process': 'Scalping', 'ED': "20.01.2020"
}
data_18_prod = {
	'Prod_Name': "EGE Gluten Free Corn Starch", 'BBD': "12.08.2018", 'Nutrients': ['Fat(0.3g)', 'Carbohydrate(87.9g)', 'Protein(0.3g)'], 'Calories': 362, 'Cooked': False, 'Allergens': ['Corn'], 'Problematic': False, 'Process': 'Scalping', 'ED': "12.07.2019"
}
data_19_prod = {
	'Prod_Name': "EGE Gluten Free Corn Starch", 'BBD': "17.07.2018", 'Nutrients': ['Fat(0.3g)', 'Carbohydrate(87.9g)', 'Protein(0.3g)'], 'Calories': 364, 'Cooked': False, 'Allergens': ['Corn'], 'Problematic': False, 'Process': 'Scalping', 'ED': "19.07.2019"
}
data_20_prod = {
	'Prod_Name': "EGE Gluten Free Corn Starch", 'BBD': "25.07.2018", 'Nutrients': ['Fat(0.3g)', 'Carbohydrate(87.9g)', 'Protein(0.3g)'], 'Calories': 360, 'Cooked': False, 'Allergens': ['Corn'], 'Problematic': False, 'Process': 'Scalping', 'ED': "26.07.2019"
}

data_21_prod = {
	'Prod_Name': "Tropical Heat Peanuts", 'BBD': '04.02.2019', 'Nutrients': ['Protein(25.9g)', 'Carbohydrate(27.2g)', 'Sugar(10.8g)', 'Saturated Fat(8.3g)', 'Mono-unsaturated Fat(24.4g)', 'Poly-unsaturated Fat(14.4g)', 'Fibre(6.5g)','Salt(2.25g)'], 'Calories': 602,'Cooked': False, 'Allergens': ['Peanuts'],
	'Problematic': False, 'Process': 'Roasted', 'ED': '09.03.2020'
}
data_22_prod = {
	'Prod_Name': "Tropical Heat Peanuts", 'BBD': "19.01.2019", 'Nutrients': ['Protein(25.9g)', 'Carbohydrate(27.2g)', 'Sugar(10.8g)', 'Saturated Fat(8.3g)', 'Mono-unsaturated Fat(24.4g)', 'Poly-unsaturated Fat(14.4g)', 'Fibre(6.5g)','Salt(2.25g)'], 'Calories': 602, 'Cooked': False, 'Allergens': ['Peanuts'], 'Problematic': False, 'Process': 'Roasted', 'ED': "19.05.2019"
}
data_23_prod = {
	'Prod_Name': "Tropical Heat Peanuts", 'BBD': "15.04.2018", 'Nutrients': ['Protein(25.9g)', 'Carbohydrate(27.2g)', 'Sugar(10.8g)', 'Saturated Fat(8.3g)', 'Mono-unsaturated Fat(24.4g)', 'Poly-unsaturated Fat(14.4g)', 'Fibre(6.5g)','Salt(2.25g)'], 'Calories': 610, 'Cooked': False, 'Allergens': ['Peanuts'], 'Problematic': True, 'Process': 'Roasted', 'ED': "19.07.2018"
}
data_24_prod = {
	'Prod_Name': "Tropical Heat Peanuts", 'BBD': "14.04.2018", 'Nutrients': ['Protein(25.9g)', 'Carbohydrate(27.2g)', 'Sugar(10.8g)', 'Saturated Fat(8.3g)', 'Mono-unsaturated Fat(24.4g)', 'Poly-unsaturated Fat(14.4g)', 'Fibre(6.5g)','Salt(2.25g)'], 'Calories': 608, 'Cooked': False, 'Allergens': ['Peanuts'], 'Problematic': False, 'Process': 'Roasted', 'ED': "16.08.2018"
}
data_25_prod = {
	'Prod_Name': "Tropical Heat Peanuts", 'BBD': "24.03.2018", 'Nutrients': ['Protein(25.9g)', 'Carbohydrate(27.2g)', 'Sugar(10.8g)', 'Saturated Fat(8.3g)', 'Mono-unsaturated Fat(24.4g)', 'Poly-unsaturated Fat(14.4g)', 'Fibre(6.5g)','Salt(2.25g)'], 'Calories': 604, 'Cooked': False, 'Allergens': ['Peanuts'], 'Problematic': True, 'Process': 'Roasted', 'ED': "20.06.2018"
}



data_1_proc = {
	'Harvested': {'Date': '06.05.2018', 'Location': 'India', 'Product': 'Potatoe','Problematic':False},
	'Transport1': {'Duration': 19, 'Moved to,from': 'India-Gee Tee Industries', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Gee Tee Industries', 'Processes': 'Peeling, Slicing, Frying','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Gee Tee Industries-Gee Tee Industries', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Gee Tee Industries', 'Material': 'Polypropylene', 'Cancerogen': False,'Problematic': False}
}
data_2_proc = {
	'Harvested': {'Date': '14.08.2017', 'Location': 'China', 'Product': 'Potatoe','Problematic':False},
	'Transport1': {'Duration': 24, 'Moved to,from': 'China-Gee Tee Industries', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Gee Tee Industries', 'Processes': 'Peeling, Slicing, Frying','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Gee Tee Industries-Gee Tee Industries', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Gee Tee Industries', 'Material': 'Polypropylene', 'Cancerogen': True,'Problematic':True}
}
data_3_proc = {
	'Harvested': {'Date': '15.06.2018', 'Location': 'India', 'Product': 'Potatoe','Problematic':False},
	'Transport1': {'Duration': 25, 'Moved to,from': 'India-Gee Tee Industries', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Gee Tee Industries', 'Processes': 'Peeling, Slicing, Frying','Problematic':False},
	'Transport2': {'Duration': 2, 'Moved to,from': 'Gee Tee Industries-Gee Tee Industries', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Gee Tee Industries', 'Material': 'Polypropylene', 'Cancerogen':False,'Problematic':False}
}
data_4_proc = {
	'Harvested': {'Date': '19.06.2017', 'Location': 'Turkey', 'Product': 'Potatoe','Problematic':False},
	'Transport1': {'Duration': 19, 'Moved to,from': 'Turkey-Gee Tee Industries', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Gee Tee Industries', 'Processes': 'Peeling, Slicing, Frying','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Gee Tee Industries-Gee Tee Industries', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Gee Tee Industries', 'Material': 'Polypropylene', 'Cancerogen': False,'Problematic':False}
}
data_5_proc = {
	'Harvested': {'Date': '27.07.2017', 'Location': 'Turkey', 'Product': 'Potatoe','Problematic':False},
	'Transport1': {'Duration': 16, 'Moved to,from': 'Turkey-Gee Tee Industries', 'Condition': False, 'Stopped': True,'Problematic': True},
	'Process': {'Location': 'Gee Tee Industries', 'Processes': 'Peeling, Slicing, Frying','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Gee Tee Industries-Gee Tee Industries', 'Condition':True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Gee Tee Industries', 'Material': 'Polypropylene', 'Cancerogen': False,'Problematic':False}
}
data_6_proc = {
	'Harvested': {'Date': '14.05.2017', 'Location': 'Turkey', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 23, 'Moved to,from': 'Turkey-Galletas Gullon SA', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Galletas Gullon SA', 'Processes': 'Kneading, Moulding, Baking, Cooling','Problematic':False},
	'Transport2': {'Duration': 7, 'Moved to,from': 'Galletas Gullon SA-Greif Packaging Spain SA', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Greif Packaging Spain SA', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_7_proc = {
	'Harvested': {'Date': '15.05.2018', 'Location': 'China', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 21, 'Moved to,from': 'China-Galletas Gullon SA', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Galletas Gullon SA', 'Processes': 'Kneading, Moulding, Baking, Cooling','Problematic':True},
	'Transport2': {'Duration': 0, 'Moved to,from': 'Galletas Gullon SA-Galletas Gullon SA', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Galletas Gullon SA', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_8_proc = {
	'Harvested': {'Date': '17.04.2018', 'Location': 'Russia', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 24, 'Moved to,from': 'Russia-Galletas Gullon SA', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Galletas Gullon SA', 'Processes': 'Kneading, Moulding, Baking, Cooling','Problematic':False},
	'Transport2': {'Duration': 6, 'Moved to,from': 'Galletas Gullon SA-Greif Packaging Spain SA', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Greif Packaging Spain SA', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_9_proc = {
	'Harvested': {'Date': '12.03.2018', 'Location': 'India', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 26, 'Moved to,from': 'India-Galletas Gullon SA', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Galletas Gullon SA', 'Processes': 'Kneading, Moulding, Baking, Cooling','Problematic':False},
	'Transport2': {'Duration': 8, 'Moved to,from': 'Galletas Gullon SA-Greif Packaging Spain SA', 'Condition': False, 'Stopped': False,'Problematic':True},
	'Packaging': {'Location': 'Greif Packaging Spain SA', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_10_proc = {
	'Harvested': {'Date': '14.06.2018', 'Location': 'Ukraine', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 14, 'Moved to,from': 'Ukraine-Galletas Gullon SA', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Galletas Gullon SA', 'Processes': 'Kneading, Moulding, Baking, Cooling','Problematic':False},
	'Transport2': {'Duration': 9, 'Moved to,from': 'Galletas Gullon SA-Greif Packaging Spain SA', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Packaging': {'Location': 'Greif Packaging Spain SA', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_11_proc = {
	'Harvested': {'Date': '15.06.2017', 'Location': 'Russia', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 29, 'Moved to,from': 'Russia-Barilla', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Barilla', 'Processes': 'Pressing, Moulding, Klining, Ensiling ','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Barilla-Barilla', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Barilla', 'Material': 'Carton', 'Cancerogen': True,'Problematic':True}
}
data_12_proc = {
	'Harvested': {'Date': '12.08.2018', 'Location': 'India', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 25, 'Moved to,from': 'India-Barilla', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Barilla', 'Processes': 'Pressing, Moulding, Klining, Ensiling','Problematic':True},
	'Transport2': {'Duration': 0.5, 'Moved to,from': 'Barilla-Barilla', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Barilla', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_13_proc = {
	'Harvested': {'Date': '23.03.2018', 'Location': 'Turkey', 'Product': 'Wheat','Problematic':True},
	'Transport1': {'Duration': 24, 'Moved to,from': 'Turkey-Barilla', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Barilla', 'Processes': 'Pressing, Moulding, Klining, Ensiling','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Barilla-Barilla', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Barilla', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_14_proc = {
	'Harvested': {'Date': '24.06.2018', 'Location': 'Russia', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 31, 'Moved to,from': 'Russia-Barilla', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Barilla', 'Processes': 'Pressing, Moulding, Klining, Ensiling','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Barilla-Barilla', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Barilla', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_15_proc = {
	'Harvested': {'Date': '12.07.2018', 'Location': 'Russia', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 23, 'Moved to,from': 'Russia-Barilla', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Barilla', 'Processes': 'Pressing, Moulding, Klining, Ensiling','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Barilla-Barilla', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Barilla', 'Material': 'Carton', 'Cancerogen': False,'Problematic':True}
}
data_16_proc = {
	'Harvested': {'Date': '16.08.2017', 'Location': 'USA', 'Product': 'Corn','Problematic':False},
	'Transport1': {'Duration': 28, 'Moved to,from': 'USA-EGE Gluten Free Food Product Company', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'EGE Gluten Free Food Product Company', 'Processes': 'Cleaning, Maceration, Core Scalping, Bran Scalping, Protein Scalping, Starch Purification','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'EGE Gluten Free Food Product Company-Starpak Packaging Company', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Starpak Packaging Company', 'Material': 'Recyclable Plastic', 'Cancerogen': False,'Problematic':False}
}
data_17_proc = {
	'Harvested': {'Date': '20.06.2018', 'Location': 'USA', 'Product': 'Corn','Problematic':False},
	'Transport1': {'Duration': 29, 'Moved to,from': 'USA-EGE Gluten Free Food Product Company', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'EGE Gluten Free Food Product Company', 'Processes': 'Cleaning, Maceration, Core Scalping, Bran Scalping, Protein Scalping, Starch Purification','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': 'EGE Gluten Free Food Product Company-EGE Gluten Free Food Product Company', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'EGE Gluten Free Food Product Company', 'Material': 'Recyclable Plastic', 'Cancerogen': False,'Problematic':False}
}
data_18_proc = {
	'Harvested': {'Date': '16.06.2018', 'Location': 'India', 'Product': 'Corn','Problematic':False},
	'Transport1': {'Duration': 21, 'Moved to,from': 'India-EGE Gluten Free Food Product Company', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'EGE Gluten Free Food Product Company', 'Processes': 'Cleaning, Maceration, Core Scalping, Bran Scalping, Protein Scalping, Starch Purification','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': 'EGE Gluten Free Food Product Company-EGE Gluten Free Food Product Company', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'EGE Gluten Free Food Product Company', 'Material': 'Recyclable Plastic', 'Cancerogen': False,'Problematic':False}
}
data_19_proc = {
	'Harvested': {'Date': '14.06.2018', 'Location': 'Turkey', 'Product': 'Corn','Problematic':True},
	'Transport1': {'Duration': 4, 'Moved to,from': 'Turkey-EGE Gluten Free Food Product Company', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': 'EGE Gluten Free Food Product Company', 'Processes': 'Cleaning, Maceration, Core Scalping, Bran Scalping, Protein Scalping, Starch Purification','Problematic':False},
	'Transport2': {'Duration': 2, 'Moved to,from': 'EGE Gluten Free Food Product Company-Starpak Packaging Company', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Starpak Packaging Company', 'Material': 'Recyclable Plastic', 'Cancerogen': False,'Problematic':False}
}
data_20_proc = {
	'Harvested': {'Date': '01.06.2018', 'Location': 'Turkey', 'Product': 'Corn','Problematic':False},
	'Transport1': {'Duration': 8, 'Moved to,from': 'Turkey-EGE Gluten Free Food Product Company', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'EGE Gluten Free Food Product Company', 'Processes': 'Cleaning, Maceration, Core Scalping, Bran Scalping, Protein Scalping, Starch Purification','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': 'EGE Gluten Free Food Product Company-EGE Gluten Free Food Product Company', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'EGE Gluten Free Food Product Company', 'Material': 'Non-recyclable Plastic', 'Cancerogen': True,'Problematic':True}
}
data_21_proc = {
	'Harvested': {'Date': '02.04.2018', 'Location': 'Kenya', 'Product': 'Peanuts','Problematic':False},
	'Transport1': {'Duration': 8, 'Moved to,from': 'Kenya-Deepa Industries LTD', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Deepa Industries LTD', 'Processes': 'Peeling, Roasting, Salting','Problematic':False},
	'Transport2': {'Duration': 0.5, 'Moved to,from': 'Deepa Industries LTD-Deepa Industries LTD', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Deepa Industries LTD', 'Material': 'Plastic', 'Cancerogen': False,'Problematic':False}
}
data_22_proc = {
	'Harvested': {'Date': '18.06.2018', 'Location': 'Kenya', 'Product': 'Peanuts','Problematic':False},
	'Transport1': {'Duration': 7, 'Moved to,from': 'Kenya-Deepa Industries LTD', 'Condition': False, 'Stopped': False,'Problematic':True},
	'Process': {'Location': 'Deepa Industries LTD', 'Processes': 'Peeling, Roasting, Salting','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Deepa Industries LTD-Deepa Industries LTD', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Deepa Industries LTD', 'Material': 'Plastic', 'Cancerogen': True,'Problematic':True}
}
data_23_proc = {
	'Harvested': {'Date': '19.08.2018', 'Location': 'Kenya', 'Product': 'Peanuts','Problematic':False},
	'Transport1': {'Duration': 9, 'Moved to,from': 'Kenya-Deepa Industries LTD', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': 'Deepa Industries LTD', 'Processes': 'Peeling, Roasting, Salting','Problematic':True},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Deepa Industries LTD-Deepa Industries LTD', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Deepa Industries LTD', 'Material': 'Plastic', 'Cancerogen': False,'Problematic':False}
}
data_24_proc = {
	'Harvested': {'Date': '12.09.2017', 'Location': 'China', 'Product': 'Peanuts','Problematic':False},
	'Transport1': {'Duration': 19, 'Moved to,from': 'China-Deepa Industries LTD', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': 'Deepa Industries LTD', 'Processes': 'Peeling, Roasting, Salting','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Deepa Industries LTD-Deepa Industries LTD', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Deepa Industries LTD', 'Material': 'Plastic', 'Cancerogen': False,'Problematic':False}
}
data_25_proc = {
	'Harvested': {'Date': '19.10.2017', 'Location': 'India', 'Product': 'Peanuts','Problematic':False},
	'Transport1': {'Duration': 15, 'Moved to,from': 'India-Deepa Industries LTD', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': 'Deepa Industries LTD', 'Processes': 'Peeling, Roasting, Salting','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Deepa Industries LTD-Deepa Industries LTD', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Deepa Industries LTD', 'Material': 'Plastic', 'Cancerogen': True,'Problematic':True}
}




Products = [data_1_prod, data_2_prod, data_3_prod, data_4_prod, data_5_prod, data_6_prod, data_7_prod, data_8_prod, data_9_prod, data_10_prod, data_11_prod, data_12_prod, data_13_prod, data_14_prod, data_15_prod, data_16_prod, data_17_prod, data_18_prod, data_19_prod, data_20_prod, data_21_prod, data_22_prod, data_23_prod, data_24_prod, data_25_prod]
Processes = [data_1_proc, data_2_proc, data_3_proc,data_4_proc, data_5_proc, data_6_proc, data_7_proc, data_8_proc, data_9_proc, data_10_proc, data_11_proc, data_12_proc, data_13_proc, data_14_proc, data_15_proc, data_16_proc, data_17_proc, data_18_proc, data_19_proc, data_20_proc, data_21_proc, data_22_proc, data_23_proc, data_24_proc, data_25_proc]

for i in range(len(Products)):
	with open('../database/content/Products/'+str(i+1) + '.json', 'w') as outfile:
		json.dump(Products[i], outfile)
		outfile.close()


for i in range(len(Processes)):
	with open('../database/content/Processes/'+str(i+1) + '.json', 'w') as outfile:
		json.dump(Processes[i], outfile)
		outfile.close()
