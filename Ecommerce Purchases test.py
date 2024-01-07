import pandas as pd
ecom = pd.read_csv('Ecommerce Purchases.csv')
#"1:How many rows and columns are there?"
print(ecom.shape)
#"2:What is the average Purchase Price?"
ans=ecom['Purchase Price'].mean()
print('average purchase price = ',ans)
#"3:What were the highest and lowest purchase prices?"
mini=ecom['Purchase Price'].min()
maxi=ecom['Purchase Price'].max()
print('minimum purchase price =',mini)
print('Maximum purchase price =',maxi)
#"4:How many people have English 'en' as their Language of choice on the website?"
lcount=ecom[ecom['Language']=='en']
lrow,lcol=lcount.shape
print("English Users = ",lrow)
#"5:How many people have the job title of Lawyer ?"
jcount=ecom[ecom['Job']=='Lawyer']
lrow,lcol=jcount.shape
print("Lawyers = ",lrow)
#"6:How many people made the purchase during the AM or PM?"
apcount=ecom[ecom['AM or PM']=='AM']
lrow,lcol=apcount.shape
print("AM = ",lrow)
apcount=ecom[ecom['AM or PM']=='PM']
lrow,lcol=apcount.shape
print("PM = ",lrow)
"or"
ans=ecom['AM or PM'].value_counts()
print(ans)
#"What are the 5 most common Job Titles?"
ans=ecom['Job'].value_counts().head(5)
print(ans)
#"8:How many people have American Express as their"
" Credit Card Provider and made a purchase above $95"
ans=ecom[(ecom['CC Provider']=='American Express')&(ecom['Purchase Price']>95.0)]
lrow,lcol=ans.shape
print("American express user with above 95$ purchase = ",lrow)

lcount=ecom[ecom['Purchase Price']==ecom['Purchase Price'].max()]
print(lcount['CC Provider'])