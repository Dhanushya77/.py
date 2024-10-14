user=[{'id':100,'name':'dhan','email':'email1','password':'pas','ph_no':1234,'book':[]}]
book=[{'id':100,'name':'sample','stock':10,'price':10}]

def view_pro(users):
    print (users)
def view_book(books):
    print(books)
def return_book():
    id=int(input('enter id:'))
    f1=0
    for j in book:
            if j['id']==id and id in i['book']:
                f1=1
                j['stock']+=1
                i['book'].remove(id)
                if f1==0:
                    print('book not available')