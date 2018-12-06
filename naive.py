from __future__ import division
f= open('business.csv','rU')
data = [line.rstrip('\n') for line in f]

business=[]
for i in range(len(data)):
	temp=data[i].split(',')
	business.append(temp)
f.close()	
	
f1= open('user.csv','rU')
data = [line.rstrip('\n') for line in f1]

users=[]
for i in range(len(data)):
	temp=data[i].split(',')
	users.append(temp)
	
f1.close()


f2= open('review.csv','rU')
rev_data = [line.rstrip('\n') for line in f2]

reviews=[]
for i in range(len(rev_data)):
	temp=rev_data[i].split(',')
	reviews.append(temp)
	
f2.close()

tempsum=0
for i in range(1,len(business)):
	temp = business[i][9]
	temp = float(temp[1:-1])
	if 0.0<=temp<=5.0:
		
		tempsum= tempsum + temp
	else:
		continue
mu=tempsum/len(business)
print('mu is '+str(mu))

match=0
total_reviews_used=0
total_star_calc = 0
for i in range(1,len(reviews)):
	users_temp=reviews[i][1]
	business_temp=reviews[i][2]
	stars_temp=reviews[i][3]
	flag_users=False
	flag_business=False
	for j in range(1,len(business)):		
		if business_temp==business[j][0]:
			flag_business=True
			break
	if flag_business==True:
		for k in range(1,len(users)):
			if users_temp==users[k][0]:
				flag_users=True
				break
		if flag_users==True:
			temp = users[k][2]
			users_star = float(temp[1:-1])
			temp = business[j][9]
			business_star = float(temp[1:-1])
			#star_calc=mu+(float("{0:.3f}".format(float(users[k][1])))-mu)+(float(business[j][1])-mu)
			star_calc  = mu+(users_star-mu)+(float(business_star-mu))
			star_calc=int(round(star_calc))
			if star_calc>5 or star_calc<0:
				star_calc=5
			print("Given rating of user "+ str(k) +" to a business "+ str(j) + " :", star_calc)
			stars_temp = stars_temp[1:-1]
			total_star_calc = total_star_calc + star_calc	
	if flag_users:
		total_reviews_used=total_reviews_used+1
		if str(star_calc)==str(stars_temp):
			match=match+1
print("Total rating :", total_star_calc)
accuracy = float(match)/float(total_reviews_used)

print('accuracy = '+str(accuracy))			






		
			











