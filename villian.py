from datetime import datetime
def villian(date):
    dateTimeObj = datetime.now()
    dat=dateTimeObj.strftime("%d-%b-%Y")
    mon=['jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec']
    dt=dat.split('-')
    print(dt[1].lower())
    # ds=list(dt[1])
    # first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    # last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    # dtm=list(map(int,dt))
    # if len(ds)>1:
    #     s=int(ds[1])
    # else:
    #     s=int(ds[0])
    # d=int(len(dt[1]))
    # return first[d]+' '+last[d] if len(str(dt[1]))>0 else first[s]+' '+last[s]

format_str = '%d/%m/%Y'
a=datetime.strptime("1/06/2000", format_str)
print(villian(a))