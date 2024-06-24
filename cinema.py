class Star_Cinema:
    hall_list=[]
    

    def entry_hall(self,halls): 
        self.hall_list.append(halls)
    
    
        
        
        
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.seats={}
        self.show_list=[]
        self.entry_hall(self)
        
    def entry_show(self,id,movie_name,time):
        shows=(id,movie_name,time)
        self.show_list.append(shows)
        self.seats[id]=[[0 for _ in range(self.cols)]for _  in range(self.rows)]
    
    def view_available_seats(self,id): 
        if id in self.seats:
            print()
            for row in self.seats[id]:
                print(row)
            print()
        else:
            print("\nMovie Not found !Try Again\n")
           
                
                
   
   
    def book_seats(self,id,lsts): # lsts multiple tuple thakte pare .. jotogulo seat booked hobe totogulo tuple thkbe .. per tuple e 2 ta parameter thkbe row and colum
        if id in self.seats:
            for row,col in lsts:
                if self.seats[id][row-1][col-1]==0:
                    self.seats[id][row-1][col-1]=1
                    print(f"\nSeat ({row},{col}) has booked successfully !")
                else:
                    print("\nThis seat is already booked\n")
                    return
        else:
            print("\nInvalid show ID\n")
                
      
        self.view_available_seats(id)
            
            
            
    
    
    def view_show_list(self):
        print("--------------------------------------------------------")
        for id,movie,time in self.show_list:
            print(f"Show ID :{id}\tMovie Name :{movie}\tTime :{time}")
        print("--------------------------------------------------------")

       
      
        
    
           
      
cineplex=Hall(6,6,'abc')
cineplex.entry_show(11,'Toofan',"11.30 PM")
cineplex.entry_show(12,"rockstar",'2.00 PM')
cineplex.entry_show(33,"12th_fail",'7.00 PM')



    
while True:
    print("\n1. View All show today")
    print("2. View Available seats")
    print("3. Book Tickets")
    print("4. Exit\n")
    
    op=int(input("Enter choice :"))
    if op==1:
        # print(cineplex.view_show_list())
        cineplex.view_show_list()
    if op==2:
        id=int(input("enter show id :"))
        # print(cineplex.view_available_seats(id))
        cineplex.view_available_seats(id)
    if op==3:
        lst=[]  
        id=int(input("Enter show id :"))
        seats=int(input("Numbers of tickets :"))
        for i in range(seats):
            row=int(input(f"enter row for ticket {i+1}:"))
            col=int(input(f"enter col for ticket {i+1}:"))
            lst.append((row,col))
        cineplex.book_seats(id,lst)
    if op==4:
        break
        
        
        





