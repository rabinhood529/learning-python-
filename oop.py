class Server:
  def __init__(self,name,status):
    self.name=name
    self.status=status

    def check_health(self):
      if self.status.lower()=="down":
        print(f"{self.name} is broken! ")
        self.status="Fixed"
      else:
        print(f"{self.name} is running fine")

      def report(self):
        print(f"server{self.name} status is {self.status}")


      s1=Server("Auth-01","Down")
      s1.check_health() 
      s1.report()


