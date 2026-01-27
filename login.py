class login_page:
    App_name = "login_app"
    def __init__(self,name,phne):
        self.name = name
        self.phne = phne
    def info(self):
        print("name : ",self.name)
        print("phne : ",self.phne)

o1 = login_page("sachin",6784372384)
o2 = login_page("omee",4378478245)
o1.info()
o2.info()