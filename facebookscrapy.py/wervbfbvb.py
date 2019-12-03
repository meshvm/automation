import keys


#interest= (s[1])+"%20"+local for trial.py
class GrpNLocation:
    def IntrestLoc(self):
        s=[]
        local=[]
        self.s =list((keys.randomizer('interests')))
        self.local = keys.randomizer('location')
        print(str((s[1])+"%20"+local))
        return str((s[1])+"%20"+local)

    def category(self):
        # 
        location = self.local
        grp = self.s[1]
        print(location,grp)
        # group,location = (','.join(IntrestLoc()))
        # print(group,location)
if __name__ == "__main__":
    ref=GrpNLocation()
    ref.IntrestLoc()
    ref.category()