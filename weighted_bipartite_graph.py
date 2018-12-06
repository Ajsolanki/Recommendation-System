import math
f= open('business_new.csv','rU')
data = [line.rstrip('\n') for line in f]

business=[]
for i in range(len(data)):
	temp=data[i].split(',')
	business.append(temp)
f.close()	
	
f1= open('users_new.csv','rU')
data = [line.rstrip('\n') for line in f1]

users=[]
for i in range(len(data)):
	temp=data[i].split(',')
	users.append(temp)
	
f1.close()


f2= open('review_new.csv','rU')
data = [line.rstrip('\n') for line in f2]

reviews=[]
for i in range(len(data)):
	temp=data[i].split(',')
	reviews.append(temp)
	
f2.close()

tempsum=0
match=0
total_reviews_used=0
square_error=0
absolute_error=0

def reccomendation_power(a,b,c,d):
	total_business_rating=0
	total_user_rating=1
	toreturn=0
	
	
	for o in range(1,len(reviews)):	
		if reviews[o][1]==a:	
			total_user_rating=total_user_rating+int(reviews[o][4])
		
		if reviews[o][2]==b:
			total_business_rating=total_business_rating+int(reviews[o][4])
		
	toreturn=toreturn+((c*d)/(total_user_rating*total_business_rating))
	return toreturn

user_rating_avg=float()
for i in range(1,len(reviews)):
	#print(i)
	user=reviews[i][1]
	business_t=reviews[i][2]
	rating_given=int(reviews[i][4])
	flag_users=False
	flag_business=False
	common_users=[]
	common_users_rating=[]
	rating=0
	for h in range(1,len(users)):
		if users[h][1]==user:
			user_rating_avg=float(users[h][8])
			break
			
	for j in range(1,len(business)):
		if business_t==business[j][1]:
			flag_business=True
			break
	if flag_business:
		for k in range(1,len(users)):
			if user==users[k][1]:
				flag_users=True
				break
		if flag_users:
			for l in range(1,len(reviews)):
				if reviews[l][2]==business_t:
					common_users.append(reviews[l][1])
					common_users_rating.append(int(reviews[l][4]))
			for m in range(len(common_users)):
				similarity=reccomendation_power(user,business_t,rating_given,common_users_rating[m])
				
				for n in range(1,len(users)):
					if common_users[m]==users[n][1]:
						this_user_avg=float(users[n][8])
						break
				rating=rating+(similarity*(common_users_rating[m]-this_user_avg))
	
	rating_temp=user_rating_avg+rating
	print("Predicted rating for user "+str(i)+" is :", rating_temp)
	square_error=square_error+(rating_given-rating_temp)*(rating_given-rating_temp)
	absolute_error=absolute_error+abs(rating_given-rating_temp)
	
	
root_mean_square_error=math.sqrt((square_error)/len(reviews))
mean_absolute_error=(absolute_error/len(reviews))
print("the root_mean_square_error is "+str(root_mean_square_error))


		
			











